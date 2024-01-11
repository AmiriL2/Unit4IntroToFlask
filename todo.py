from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
import pymysql
import pymysql.cursors
from pprint import pprint as print
from werkzeug.security import generate_password_hash, check_password_hash

connect = pymysql.connect(
    database="alayne_todos",
    user="alayne",
    password="228043303",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

users = {
    "Amiri": generate_password_hash("supersecretpassword")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    


if __name__ == '__main__':
    app.run()

@app.route("/", methods=['GET', 'POST'])
@auth.login_required
def index():
      if request.method == 'POST':
            new_todo = request.form["new_todo"]

            Cursor = connect.cursor()
            Cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}') ")
            Cursor.close()
            connect.commit()

      Cursor = connect.cursor()
      Cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")
      results = Cursor.fetchall()
      Cursor.close()
      return render_template("todo.html.jinja", ToDos=results), "Hello, {}!".format(auth.username())

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
@auth.login_required
def todo_delete(todo_index):
      Cursor = connect.cursor()
      Cursor.execute(f"DELETE FROM `todos` WHERE `id`= {todo_index}")
      Cursor.close()
      connect.commit()
      return redirect('/')

@app.route('/complete_todo/<int:todo_index>', methods=['POST'])
@auth.login_required
def complete_todo(todo_index):
      Cursor = connect.cursor()
      Cursor.execute(f"UPDATE `todos` SET `complete` = 1 WHERE `id` = {todo_index}")
      Cursor.close()
      connect.commit()
      return redirect('/')

@app.route('/uncomplete_todo/<int:todo_index>', methods=['POST'])
@auth.login_required
def uncomplete_todo(todo_index):
      Cursor = connect.cursor()
      Cursor.execute(f"UPDATE `todos` SET `complete` = 0 WHERE `id` = {todo_index}")
      Cursor.close()
      connect.commit()
      return redirect('/')