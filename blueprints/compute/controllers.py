from flask import Blueprint, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound

default = Blueprint('default', __name__)
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard',
                      template_folder='../../templates', static_folder='../../static')
compute = Blueprint('compute', __name__, url_prefix='/dashboard/compute',
                    template_folder='../templates', static_folder='../static')


@default.route('/')
def go_home():
    return redirect(url_for('compute.cio_now_template'))


@compute.route('/cio-now-template')
def cio_now_template():
    return render_template('cio-now-template.html')


@compute.route('/requirements')
def show_dashboard():
    return render_template('blueprints/compute/gather_requirements.html')
