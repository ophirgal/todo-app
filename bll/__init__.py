import dal
from pathlib import Path
from flask import current_app
from werkzeug.utils import secure_filename

# Fetch tasks from the database
def get_tasks():
    return dal.get_tasks()

# Add a new task to the database
def add_task_to_db(title, file):    
    image_path = Path(current_app.static_folder) / "images" / secure_filename(file.filename)
    file.save(image_path)

    dal.add_task_to_db(title, file.filename)

def delete_task_by_id(id):
    dal.delete_task_by_id(id)


# from flask import make_response

# view function 
# response = make_response(...)
# response.set_cookie("")

# from datetime import timedelta
# app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

# return response

