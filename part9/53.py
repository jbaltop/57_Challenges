import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, render_template, request
import time
import configparser


def run_server():
    app = Flask(__name__, template_folder="../templates")

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "GET":
            todo_list = read_todo()
            return render_template("53.html", todo_list=todo_list)
        if request.method == "POST":
            update_todo(request.form)
            todo_list = read_todo()
            return render_template("53.html", todo_list=todo_list)

    app.run(port=8000)


def read_todo():
    todo_db = db.reference("todo").get()
    todo_list2 = []
    if todo_db != None:
        todo_list = [todo_db[todo] for todo in todo_db]
        dnt_list = [item["date_and_time"] for item in todo_list]
        dnt_list.sort()
        todo_dict = {item["date_and_time"]: item["todo"] for item in todo_list}
        todo_list2 = [todo_dict[dnt] for dnt in dnt_list]
    todo_list3 = [item[i] for item in todo_list2 for i in range(0, len(item))]
    return todo_list3


def update_todo(result):
    new_todo_list = result["new_todos"].split("\r\n")
    while "" in new_todo_list:
        new_todo_list.remove("")
    add_todo(new_todo_list)

    result_dict = dict(result)
    todo_db = db.reference("todo").get()
    if "todo" in result_dict:
        done_todo_list = result_dict["todo"]
        for todo in done_todo_list:
            remove_todo(todo, todo_db)


def add_todo(new_todo_list):
    if new_todo_list != []:
        root = db.reference("/")
        root.child("todo").push(
            {
                "date_and_time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
                "todo": new_todo_list,
            }
        )


def remove_todo(done_todo, todo_db):
    todo_dict = {
        todo_db[item]["todo"][i]: item
        for item in todo_db
        for i in range(0, len(todo_db[item]["todo"]))
    }
    todo_list = todo_db[todo_dict[done_todo]]["todo"]
    todo_list.remove(done_todo)
    if len(todo_list) == 0:
        db.reference("/todo/").child(todo_dict[done_todo]).delete()
    else:
        db.reference("/todo/").child(todo_dict[done_todo]).update({"todo": todo_list})


def main():
    config = configparser.ConfigParser()
    config.read("../private/53.ini")

    key = config["firebase"]["key_path"]
    database_url = config["firebase"]["database_url"]
    cred = credentials.Certificate(key)
    myapp = firebase_admin.initialize_app(cred, {"databaseURL": database_url})

    run_server()


main()
