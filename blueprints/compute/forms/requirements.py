from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired


_submit = SubmitField('Save')


class CreateTeam(FlaskForm):
    name = StringField('Team Name', validators=[DataRequired()])
    group = StringField('Team Group')
    description = TextAreaField('Team Description')
    submit_team = _submit


class CreateVirtualRequirements(FlaskForm):
    name = StringField('Requirement Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    vm_type = StringField('VM Type')
    environment = StringField('Environment')
    os_type = StringField('OS Type')
    cluster = StringField('Cluster Name')
    vcpus = IntegerField('No of vCPUs', validators=[DataRequired()])
    ram = IntegerField('RAM (MB)', validators=[DataRequired()])
    storage = IntegerField('Disk Space (GB)', validators=[DataRequired()])
    # Number of VM Units will be calculated
    submit_vm_requirements = _submit


class CreatePhysicalRequirements(FlaskForm):
    name = StringField('Label ID', validators=[DataRequired(message='Please enter a unique device label name')])
    description = TextAreaField('Description', validators=[DataRequired()])
    model_name = StringField('Chasis Model', validators=[DataRequired()])
    vendor = StringField('Vendor', validators=[DataRequired])
    part_number = StringField('Part Num', validators=[DataRequired()])
    procs = StringField('Processors', validators=[DataRequired()])
    ram = StringField('RAM (GB)', validators=[DataRequired()])
    storage = IntegerField('Storage Space (GB)', validators=[DataRequired()])
    hypervisor = SelectField('Hypervisor Type', choices=[('esxi', 'ESXI'), ('rhel', 'RHEL')])
    os_type = StringField('Operating System')
    power_draw = FloatField('Power Rating (KW)')
    mgmt_ports = IntegerField('OOB MGMT Ports', validators=[DataRequired])
    rus = StringField('Size (RUs)', validators=[DataRequired()])

    # Todo: Create a separate table for SFPs and link it to the physical server
    sfp_count = IntegerField('Num of SFPs')
    sfp_type = StringField('SFP Type', validators=[DataRequired()])
    sfp_part_number = StringField('SFP Part Number')
    sfp_network_ports = StringField('Ports per SFP')

    submit_bm_requirements = _submit


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