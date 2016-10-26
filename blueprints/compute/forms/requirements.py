from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,  SubmitField, IntegerField
from wtforms.validators import DataRequired


_submit = SubmitField('Save')


class CreateTeam(FlaskForm):
    name = StringField('Team Name', validators=[DataRequired()])
    group = StringField('Team Group')
    description = TextAreaField('Team Description')
    submit = _submit


class CreateVirtualRequirements(FlaskForm):
    name = StringField('Requirement Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    vm_type = StringField('VM Type')
    os_type = StringField('OS Type')
    cluster = StringField('Cluster Name')
    vcpus = IntegerField('No of vCPUs', validators=[DataRequired()])
    ram = IntegerField('RAM (MB)', validators=[DataRequired()])
    # Number of VM Units will be calculated
    submit = _submit


class CreatePhysicalRequirements(FlaskForm):
    submit = _submit


class GetForms(object):
    def __init__(self):
        self.create_team = create_team()
        self.create_virtual = create_virtual()
        self.create_physical = create_physical()


def create_team():
    return CreateTeam()


def create_virtual():
    return CreateVirtualRequirements()


def create_physical():
    return CreatePhysicalRequirements()