from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint("storage", __name__, url_prefix="/storage", static_folder="../static")

@blueprint.route("/")
@login_required
def storage():
    """List of disks and info"""
    return render_template("storage/storage.html")