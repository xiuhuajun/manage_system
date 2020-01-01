from flask import Blueprint, render_template, current_app
from App.models import db
from App.models import User
first = Blueprint('first', __name__)


@first.route('/hi/')
def index():
    # return render_template('index.html')
    current_app.logger.info('access success')
    return 'hello'
