import os
import datetime
from flask import Blueprint, render_template, abort, redirect, url_for, request, jsonify
from jinja2 import TemplateNotFound

from ..compute.forms import requirements as req_forms

default = Blueprint('default', __name__)
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard',
                      template_folder='../../templates', static_folder='../../static')
compute = Blueprint('compute', __name__, url_prefix='/dashboard/compute',
                    template_folder='../templates', static_folder='../../static')


@default.route('/')
def go_home():
    return redirect(url_for('compute.cio_now_template'))


@compute.route('/cio-now-template')
def cio_now_template():
    return render_template('cio-now-template.html')


@compute.route('/requirements')
def show_dashboard():
    return render_template(
        'blueprints/compute/submit_requirements.html',
        forms=req_forms.GetForms(),
        app_name='UHA PIC',
        page_name='Team Requirements',
        last_modified_user='Delancy, Adrian P.',
        last_modified_date=datetime.datetime.now()
    )


@compute.route('/requirements/create-team', methods=['POST'])
def create_team():
    form = req_forms.CreateTeam()
    submitted = form.validate_on_submit()
    if not submitted:
        return jsonify(message='Form data not submitted properly'), 400
    print form.data
    return jsonify(message='Success'), 201
