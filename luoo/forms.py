from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class BaseForm(FlaskForm):
    @classmethod
    def from_request_args(cls, args):
        return cls(args)


class PaginationForm(BaseForm):
    page = IntegerField("Page", validators=[DataRequired()])
    per_page = IntegerField("Page Size", validators=[DataRequired()], default=20)


class VolumeForm(PaginationForm):
    pass
