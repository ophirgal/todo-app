
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, flash, abort, Blueprint
from flask import current_app
from flask import send_file, send_from_directory
from werkzeug.utils import secure_filename
import bll


task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@task_bp.route("/create", methods=["POST"])
def add_task():
    task_title = request.form.get("task")
    task_image_file = request.files.get('imageFile')
    
    # best practice - validate file type
    # do validation...
    # task_image_file.filename.split(".")[1] == "jpg" ... 
    
    if not task_title:
        flash("Task cannot be empty!", "error")
        # return redirect(url_for("index"))

    if len(task_title) > 20:
        abort(400, description="task description is too long")
        # whatever is after abort() call -- will not be executed!!

    bll.add_task_to_db(task_title, task_image_file)
    flash("Task added successfully!", "success")

    return redirect(url_for("index"))


@task_bp.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):

    # delete the specified task from the database
    bll.delete_task_by_id(id)
    flash(f"You deleted task #{id}", "success")

    return redirect(url_for("index"))


@task_bp.route("/update/<int:id>", methods=["POST"])
def update_task(id):
    
    # update the specified task from the database
    # ... 

    return redirect(url_for("index"))

@task_bp.route("/images/<string:filename>")
def get_image(filename):
    print('filename', filename)
    directory = Path(current_app.static_folder) / "images"
    return send_from_directory(directory, filename)