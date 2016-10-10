from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateTeam(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    group = StringField('name')
    description = StringField('name')


class CreateVirtualRequirements(FlaskForm):
    pass


class CreatePhysicalRequirements(FlaskForm):
    pass