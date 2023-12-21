from flask import Flask, render_template, request

ToDos = ["Buy gifts for family", "take time off from work"]

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
      new_todo = request.form["new_todo"]
      ToDos.append(new_todo)
      return render_template("todo.html.jinja", ToDos=ToDos)



