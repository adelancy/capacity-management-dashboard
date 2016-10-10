from flask import Blueprint, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound

default = Blueprint('default', __name__, template_folder='../templates')
compute = Blueprint('compute', __name__, url_prefix='/dashboard', template_folder='../../templates')


@default.route('/')
def go_home():
    return redirect(url_for('blueprints/compute/gather_requirements.html'))


@compute.route('/cio-now-template')
def show():
    try:
        return render_template('CIO Now.html')
    except TemplateNotFound:
        abort(404)


@compute.route('/dashboard/requirements')
def show_dashboard():
    return render_template('blueprints/compute/gather_requirements.html')
