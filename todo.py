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
Cursor = connect.cursor()

Cursor.execute("SELECT `description` FROM `todos`")

results = Cursor.fetchall()

ToDos = results

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
      if request.method == 'POST':
            new_todo = request.form["new_todo"]
            ToDos.append(new_todo)
      return render_template("todo.html.jinja", ToDos=ToDos)

@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
      del ToDos[todo_index]
      return redirect('/')

