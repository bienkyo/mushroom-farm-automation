from flask import Blueprint, render_template
dash = Blueprint('dashboard', __name__)

@dash.route('/')
def dashboard():
    return render_template('dashboard/dashboard.html')
