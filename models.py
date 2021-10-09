import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")



class Todos:
    def create_connection(db_path):
   """ create a database connection to the SQLite database
       specified by db_path
   :param db_path: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_path)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_todos(conn, todos):
   """
   Create a new todos into the Todos table
   :param conn:
   :param todos:
   :return: projekt id
   """
   sql = '''INSERT INTO Projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, todos)
   conn.commit()
   return cur.lastrowid
    def __init__(self):
        try:
            with open("database,db", "r") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    def all(self):
        return self.todos

    def get(self, id):
        return self.todos[id]

    def create(self, data):
        data.pop('csrf_token')
        self.todos.append(data)

    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()


todos = Todos()
