import sqlite3

DB_FILE = "tasks.db"

# Database initialization
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0,
            filename TEXT
        )
        """)
        conn.commit()


# Fetch tasks from the database
def get_tasks():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, filename FROM tasks WHERE completed = 0")
        return cursor.fetchall()  # Returns a list of tuples (id, title)

# Add a new task to the database
def add_task_to_db(title, filename):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        print('DAL: filename', filename)
        cursor.execute("INSERT INTO tasks (title, filename) VALUES (?, ?)", (title, filename))
        conn.commit()

def delete_task_by_id(id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = (?)", (id,))
        conn.commit()