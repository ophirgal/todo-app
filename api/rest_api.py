from flask import jsonify, Blueprint, request
import bll

rest_api_bp = Blueprint("rest", __name__, url_prefix="/api/v1/tasks")


# CRUD

# CREATE -- POST
# READ   -- GET 
# UPDATE -- PUT
# DELETE -- DELETE

@rest_api_bp.get("/")
def get_all_tasks():
    tasks = bll.get_tasks()
    # print(tasks)
    http_response = jsonify(tasks)
    # print(type(http_response.data.decode()), http_response.data.decode())
    return http_response


@rest_api_bp.put("/")
def update_task_by_id():
    data = request.get_json()
    print(data)

    # logic to call BLL function to update the relevant task in the database...

    return jsonify(data)
