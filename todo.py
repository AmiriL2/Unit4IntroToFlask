from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print

connect = pymysql.connect(
    database="alayne_todos",
    user="alayne",
    password="228043303",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
      if request.method == 'POST':
            new_todo = request.form["new_todo"]
            Cursor = connect.cursor()
            Cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}') ")
            Cursor.close()
            connect.commit()
      Cursor = connect.cursor()

      Cursor.execute("SELECT * FROM `todos`")

      results = Cursor.fetchall()
      Cursor.close()
      return render_template("todo.html.jinja", ToDos=results)

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
      Cursor = connect.cursor()
      Cursor.execute(f"DELETE FROM `todos` WHERE `id`= {todo_index}")
      Cursor.close()
      connect.commit()
      return redirect('/')

