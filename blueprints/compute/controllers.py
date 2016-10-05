from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

compute = Blueprint('compute_dashboard', __name__)


@compute.route('/dashboard/cio-now-template')
def show():
    try:
        return render_template('CIO Now.html')
    except TemplateNotFound:
        abort(404)


@compute.route('/dashboard/requirements')
def show_dashboard():
    try:
        return render_template('blueprints/compute/gather_requirements.html')
    except TemplateNotFound:
        abort(404)
