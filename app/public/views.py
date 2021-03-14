from flask import Blueprint, render_template

public = Blueprint('public', __name__, url_prefix='/',template_folder='templates')

@public.route('/')
def public_index():
    return render_template('public/index.html')
