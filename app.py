# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "fin  - khadijaa nassimaaaa"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simule une base de données
tasks = ["Installer Jenkins", "Configurer Docker", "Réussir le pipeline","Visualiser le chngement "]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)