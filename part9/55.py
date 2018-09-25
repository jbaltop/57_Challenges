from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db
import string
import random
import configparser


def run_server():
    app = Flask(__name__, template_folder="../templates")

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            text_dict = read_text()
            url_list = [[url, text_dict[url][1]] for url in text_dict]
            return render_template("55_index.html", url_list=url_list)
        if request.method == "POST":
            new_text_title = request.form["new_text_title"]
            new_text_content = request.form["new_text_content"]
            new_content_list = new_text_content.split("\r\n")
            while new_content_list[-1] == "":
                del new_content_list[-1]
            while True:
                url = make_url()
                if is_url_exist(url):
                    continue
                else:
                    break
            save_text(url, new_text_title, new_content_list)
            return redirect(url_for("view", url=url))

    @app.route("/text/<url>", methods=["GET", "POST"])
    def view(url):
        if request.method == "GET":
            text_dict = read_text()
            title = text_dict[url][1]
            content_list = text_dict[url][2]
            return render_template(
                "55_view.html", title=title, content_list=content_list
            )
        if request.method == "POST":
            return redirect(url_for("edit", url=url))

    @app.route("/edit/<url>", methods=["GET", "POST"])
    def edit(url):
        if request.method == "GET":
            text_dict = read_text()
            title = text_dict[url][1]
            content_list = text_dict[url][2]
            return render_template(
                "55_edit.html", title=title, content_list=content_list
            )
        if request.method == "POST":
            changed_title = request.form["title"]
            changed_content = request.form["content"]
            changed_content_list = changed_content.split("\r\n")
            while changed_content_list[-1] == "":
                del changed_content_list[-1]
            update_text(url, changed_title, changed_content_list)
            return redirect(url_for("view", url=url))

    app.run(port=8000)


def save_text(url, title, content_list):
    root = db.reference("/")
    root.child("text").push({"url": url, "title": title, "content": content_list})


def is_url_exist(url):
    text_dict = read_text()
    url_list = [url for url in text_dict]
    if url in url_list:
        return True
    return False


def make_url():
    characters = list(string.ascii_letters) + list(string.digits)
    random_string_list = []
    for i in range(8):
        n = random.randint(0, 61)
        random_string_list.append(characters[n])
    random_string = "".join(random_string_list)
    return random_string


def read_text():
    text_db = db.reference("text").get()
    if text_db != None:
        text_dict = {
            text_db[item]["url"]: [
                item,
                text_db[item]["title"],
                text_db[item]["content"],
            ]
            for item in text_db
        }
        return text_dict
    return {}


def update_text(url, changed_title, changed_content_list):
    text_dict = read_text()
    db.reference("/text/").child(text_dict[url][0]).update(
        {"title": changed_title, "content": changed_content_list}
    )


def delete_text(url):
    text_dict = read_text()
    db.reference("/text/").child(text_dict[url][0]).delete()


def main():
    config = configparser.ConfigParser()
    config.read("../private/55.ini")

    key = config["firebase"]["key_path"]
    database_url = config["firebase"]["database_url"]
    cred = credentials.Certificate(key)
    myapp = firebase_admin.initialize_app(cred, {"databaseURL": database_url})

    run_server()


main()
