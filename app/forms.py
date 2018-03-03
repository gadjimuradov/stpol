from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from app.models import Work, Team
from app import  db

BaseModelForm = model_form_factory(FlaskForm)


class WorkForm(BaseModelForm):
    class Meta:
        model = Work


class TeamForm(BaseModelForm):
    class Meta:
        model = Team