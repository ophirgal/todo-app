
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, flash, abort, Blueprint
from flask import current_app, session
from flask import send_file, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
import bll


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

user_db = {"ophir":{"username": "ophir", "hash": 'scrypt:32768:8:1$qvW3uLcVtYS0f2Px$7cde64a3d3e00f6988b12a07e5a13d569cdcb86c410242d8d917b4d1ea27aec4f008a5e522d27dbdb77467760d400630bd9bf773f9496d46a7ef4946b756fccd'}}
# password --> lucky123

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        given_username = request.form['username']
        if given_username not in user_db:
            return redirect(url_for("index"))

        stored_hash = user_db[given_username]["hash"]

        if check_password_hash(stored_hash, request.form['password']):
            session["username"] = given_username
            return redirect(url_for("index"))
    
    return render_template("login.html")

@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))