import random

from bs4 import BeautifulSoup
from requests import Session

from luoo.constants import LUOO_MUSIC_URL, LUOO_BASE
from luoo.http import get
from luoo.tasks import crawl_volume_songs

session = Session()

crawl_timeout = None


def random_timeout():
    global crawl_timeout
    if crawl_timeout is None:
        crawl_timeout = 1
    else:
        crawl_timeout = crawl_timeout + random.randint(3, 8)
    return crawl_timeout


def crawl_music_page():
    resp = get(LUOO_MUSIC_URL)
    if resp.status_code == 200:
        return BeautifulSoup(resp.content, "lxml")


def get_paginator_url(page):
    return "{}/tag/?p={}".format(LUOO_BASE, page)


def crawl_page_volume_urls(volume_page):
    resp = get(get_paginator_url(volume_page))
    page_soup = BeautifulSoup(resp.content, "lxml")
    volume_list = page_soup.select(".vol-list .item a.cover-wrapper")
    return [volume.attrs["href"] for volume in volume_list]


def collect_volume_urls_from_pages():
    pages = collect_pages()
    volume_urls = []
    for page in pages[:1]:
        volume_urls.extend(crawl_page_volume_urls(page))
    return volume_urls


def collect_max_page():
    soup = crawl_music_page()
    max_page_element = soup.select(".paginator .page")[-1]
    return int(max_page_element.text)


def collect_pages():
    max_page = collect_max_page()
    pages = list(range(1, max_page + 1))
    random.shuffle(pages)
    return pages


def main():
    volume_urls = collect_volume_urls_from_pages()
    for volume_url in volume_urls[:10]:
        countdown = random_timeout()
        crawl_volume_songs.apply_async((volume_url,), countdown=countdown)


if __name__ == "__main__":
    main()
