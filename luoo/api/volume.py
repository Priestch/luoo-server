# -*- coding: utf-8 -*-
from flask import jsonify, request

from luoo.api.response_handler import error
from luoo.forms import VolumeForm
from luoo.models import Volume, Tag
from . import api_bp
from luoo.schema.volume import volume_schema, tag_schema


def get_pagination_props(pagination):
    return {
        "total": pagination.total,
        "pages": pagination.pages,
        "page": pagination.page,
        "per_page": pagination.per_page,
    }


@api_bp.route("/volumes/<int:volume_id>")
def get_volume(volume_id):
    volume = Volume.query.get_or_404(volume_id)
    dumped = volume_schema.dump(volume)
    return jsonify(dumped)


@api_bp.route("/volumes")
def get_volumes():
    form = VolumeForm.from_request_args(request.args)
    if not form.validate():
        error(form.errors)
    volume_pagination = Volume.query.paginate(
        page=form.data["page"], per_page=form.data["per_page"]
    )
    data = get_pagination_props(volume_pagination)
    data["items"] = volume_schema.dump(volume_pagination.items, many=True)
    return jsonify(data)


@api_bp.route("/tags")
def get_tags():
    tags = Tag.query.all()
    dumped = tag_schema.dump(tags, many=True)
    return jsonify(dumped)
