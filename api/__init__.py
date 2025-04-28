from flask import Flask, render_template, request, redirect, url_for, flash, abort
import bll
from api.task_views import task_bp
from api.rest_api import rest_api_bp
from api.auth_views import auth_bp

import secrets

app = Flask(__name__, template_folder="../ui/templates", static_folder="../ui/static")
app.secret_key = secrets.token_hex(16)  # Needed for flash messages

app.register_blueprint(task_bp)
app.register_blueprint(rest_api_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def index():
    tasks = bll.get_tasks()  # Get tasks from the database
    return render_template("index.html", tasks=tasks) 

@app.route('/search', methods=['GET'])
def search_tasks():
    # search_text = request.form.get('searchText')
    search_text = str(request.args['searchText'])

    # print(search_text)

    # search_result = bll.search_tasks_by_title(search_text)  # Get tasks from the database

    search_result = []

    for task in bll.get_tasks():
        # print(task[1])
        if search_text.lower() in task[1].lower():
            search_result.append(task)

    print(search_result)

    return render_template("index.html", tasks=search_result)

@app.route("/rest-tasks")
def rest_tasks():
    return render_template("rest_client.html") 


@app.errorhandler(400)
def handle_bad_request(error):
    print(type(error))
    return render_template("bad_request.html", error=error), 400

@app.errorhandler(404)
def handle_bad_request(error):
    return render_template("404.html", error=error), 404

@app.errorhandler(Exception)
def catch_all_errors(error):
    print(type(error))
    return str(error), 500