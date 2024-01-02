from flask import Flask, render_template, request, redirect

ToDos = ["Buy gifts for family", "take time off from work"]

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