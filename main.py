from flask import Flask, render_template

app = Flask(__name__)

Tasklist = [["Walk Dog", True],["Wash Dishes", False],[ "Take Out Trash", True]]


@app.route("/")
def home():
    return render_template("tasklist.html", TaskList=Tasklist)

app.run()