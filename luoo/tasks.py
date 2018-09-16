from __future__ import absolute_import, unicode_literals

import datetime
import re

from bs4 import BeautifulSoup, NavigableString, Tag as bsTag

from luoo.models import Volume, VolumeAuthor, Tag
from . import db, celery
from .http import get

volume_url_pattern = re.compile("vol/index/(\d+)$")
volume_cover_pattern = re.compile("pics/vol/(.+?)!/fwfh/640x452$")
author_pattern = re.compile("author/(\d+)$")
author_avatar_pattern = re.compile("pics/avatars/(.+?)!/fwfh/128x128$")
volume_tag_pattern = re.compile("music/(\w+?)$")


def parse_volume_id(url):
    result = volume_url_pattern.search(url)
    return int(result.groups()[0])


def parse_volume_cover_name(url):
    result = volume_cover_pattern.search(url)
    return result.groups()[0]


def parse_author_id(url):
    result = author_pattern.search(url)
    return result.groups()[0]


def parse_tag_name(url):
    result = volume_tag_pattern.search(url)
    if result is not None:
        return result.groups()[0]
    return ""


def parse_author_avatar(url):
    result = author_avatar_pattern.search(url)
    return result.groups()[0]


def parse_paragraph(item):
    if isinstance(item, bsTag):
        if item.name == "br":
            return
        text = item.text.strip()
        if item.name == "p" and len(text) == 0:
            return
        return text

    if isinstance(item, NavigableString):
        text = item.strip()
        if len(text) > 0:
            return text
        return


def parse_volume_description_paragraphs(children):
    paragraphs = []
    for child in children:
        paragraph = parse_paragraph(child)
        if paragraph:
            paragraphs.append(paragraph)
    return paragraphs


class VolumePage:
    author = None
    volume = None
    tags = None

    def __init__(self, volume_url):
        self.volume_url = volume_url
        resp = get(volume_url)
        self.soup = BeautifulSoup(resp.content, "lxml")
        self.meta_element = self.soup.select_one(".vol-meta")

    def start_crawl(self):
        self.author = self.parse_author()
        self.volume = self.parse_volume()
        self.tags = self.parse_tags()

    def parse_volume(self):
        volume_id = parse_volume_id(self.volume_url)
        vol_name = self.soup.select_one(".vol-name")
        volume_number = vol_name.select_one(".vol-number").text
        volume_title = vol_name.select_one(".vol-title").text

        volume_prev = parse_volume_id(
            self.soup.select_one("#volCoverWrapper .nav-prev").attrs["href"]
        )
        volume_next = parse_volume_id(
            self.soup.select_one("#volCoverWrapper .nav-next").attrs["href"]
        )
        cover_url = self.soup.select_one("#volCoverWrapper img").attrs["src"]
        volume_cover = parse_volume_cover_name(cover_url)

        volume_created_at = self.meta_element.select_one(".vol-date").text

        children = self.soup.select_one(".vol-desc").children
        paragraphs = parse_volume_description_paragraphs(children)

        return {
            "id": volume_id,
            "vol_number": volume_number,
            "name": volume_title,
            "description": paragraphs,
            "author_id": self.author["id"],
            "prev": volume_prev,
            "next": volume_next,
            "cover": volume_cover,
            "created_at": datetime.datetime.strptime(volume_created_at, "%Y-%m-%d"),
        }

    def parse_author(self):
        author_element = self.meta_element.select_one(".vol-author")
        author_name = author_element.text
        author_id = parse_author_id(author_element.attrs["href"])
        author_avatar = parse_author_avatar(
            self.meta_element.select_one(".author-avatar").attrs["src"]
        )
        return {"id": author_id, "name": author_name, "avatar": author_avatar}

    def parse_tags(self):
        tags = []
        for ele in self.soup.select(".vol-tags .vol-tag-item"):
            if isinstance(ele, bsTag) and ele.name == "a":
                if ele.text.startswith("#"):
                    alias = ele.text[1:]
                else:
                    alias = ele.text
                tag = {"name": parse_tag_name(ele.attrs["href"]), "alias": alias}
                tags.append(tag)
        return tags


@celery.task
def crawl_volume_songs(volume_url):
    volume_page = VolumePage(volume_url)
    volume_page.start_crawl()

    author = VolumeAuthor.query.get(volume_page.author["id"])
    if author is None:
        author = VolumeAuthor(**volume_page.author)
        db.session.add(author)
    db.session.add(author)
    volume = Volume(**volume_page.volume)
    db.session.add(volume)
    for item in volume_page.tags:
        tag = Tag.query.filter_by(alias=item["alias"]).first()
        if tag is None:
            tag = Tag(**item)
            volume.tags.append(tag)

    db.session.commit()
