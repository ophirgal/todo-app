import unittest
from pathlib import Path

from api import app
from flask import current_app, session

from bll import get_tasks

class TestBasicAPI(unittest.TestCase):
    client = app.test_client()
    
    @classmethod
    def setUpClass(cls):
        app.testing = True

    def test_homepage(self):
        response = self.client.get("/")

        self.assertIsNotNone(response)
        self.assertIn("<h1>Task Manager</h1>", response.get_data(as_text=True))

    def test_create_task_check_redirection(self):
        with app.app_context():
            image_path = Path(current_app.static_folder) / "images/food.jpg"

        response = self.client.post("/tasks/create", data={
            "task": "my boring task",
            "imageFile": image_path.open("rb")
        })

        tasks = get_tasks()
        first_task = tasks[2]
        self.assertEqual(first_task[1], "my boring task")
        self.assertIn("<h1>Redirecting...</h1>", response.get_data(as_text=True))
        self.assertEqual(response.status_code, 302)

    def test_create_task_check_after_redirection(self):
        image_path = Path(r"C:\Users\jbt\Documents\flask_24_04_25\todo_flask_app_continued\ui\static\images\food.jpg")

        response = self.client.post("/tasks/create", follow_redirects=True, data={
            "task": "my boring task",
            "imageFile": image_path.open("rb")
        })

        tasks = get_tasks()
        first_task = tasks[2]
        self.assertEqual(first_task[1], "my boring task")
        self.assertIn("<h1>Task Manager</h1>", response.get_data(as_text=True))
       
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.history), 1)
        
        self.assertEqual(response.request.path, "/")   
    
    def test_login_success(self):
        with self.client:
            self.client.post("/auth/login", data={
                "username": "ophir",
                "password": "lucky123"
            })
            
            # print("session['username'] ==", session['username'])
            self.assertEqual(session["username"], "ophir")
        
    def test_logout_success(self):
        with self.client.session_transaction() as session:
            session["username"] = "ophir"
        
            response = self.client.post("/auth/logout")

            # find Set-Cookie header -- check that its cookie is expired
            
            cookie_headers = list(filter(lambda x: x[0] == "Set-Cookie", response.headers))
            self.assertTrue(len(cookie_headers) == 1)
            self.assertTrue("Expires=Thu, 01 Jan 1970 00:00:00 GMT" in cookie_headers[0][1])
    

