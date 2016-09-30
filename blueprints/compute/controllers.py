from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

compute = Blueprint('compute_dashboard', __name__)


@compute.route('/test')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
