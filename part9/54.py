from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, db
import string
import random
from urllib.request import urlopen
import configparser


def run_server():
    app = Flask(__name__, template_folder="../templates")

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            return render_template("54_1.html")
        if request.method == "POST":
            original_url = request.form["original_url"]
            if is_url_valid(original_url):
                if is_original_url_exist(original_url):
                    shortened_url = get_shortened_url(original_url)
                else:
                    while True:
                        shortened_url = shorten_url()
                        if is_shortened_url_exist(shortened_url):
                            continue
                        else:
                            break
                    save_url(original_url, shortened_url)
                full_shortened_url = request.host + "/" + shortened_url
                return render_template(
                    "54_2.html",
                    original_url=original_url,
                    shortened_url=full_shortened_url,
                )
            else:
                return render_template("54_3.html")

    @app.route("/<shortened_url>")
    def goto(shortened_url):
        if is_shortened_url_exist(shortened_url):
            increase_used_time(shortened_url)
            return redirect(get_original_url(shortened_url))
        else:
            return "Shortened URL does not exist."

    @app.route("/<shortened_url>/stats")
    def stats(shortened_url):
        url_list = read_url()
        url_dict = {
            url["shortened_url"]: [url["original_url"], url["used_times"]]
            for url in url_list
        }
        original_url = url_dict[shortened_url][0]
        used_times = url_dict[shortened_url][1]
        return render_template(
            "54_4.html",
            original_url=original_url,
            shortened_url=shortened_url,
            used_times=used_times,
        )

    app.run(port=8000)


def shorten_url():
    characters = list(string.ascii_letters) + list(string.digits)
    random_string_list = []
    for i in range(8):
        n = random.randint(0, 61)
        random_string_list.append(characters[n])
    random_string = "".join(random_string_list)
    return random_string


def is_url_valid(original_url):
    try:
        urlopen(original_url)
        return True
    except:
        return False


def is_shortened_url_exist(shortened_url):
    url_list = read_url()
    shortened_url_list = [url["shortened_url"] for url in url_list]
    if shortened_url in shortened_url_list:
        return True
    return False


def is_original_url_exist(original_url):
    url_list = read_url()
    original_url_list = [url["original_url"] for url in url_list]
    if original_url in original_url_list:
        return True
    return False


def save_url(original_url, shortened_url):
    root = db.reference("/")
    root.child("url").push(
        {"original_url": original_url, "shortened_url": shortened_url, "used_times": 0}
    )


def read_url():
    url_db = db.reference("url").get()
    if url_db != None:
        url_list = [url_db[url] for url in url_db]
        return url_list
    return []


def get_original_url(shortened_url):
    url_list = read_url()
    url_dict = {url["shortened_url"]: url["original_url"] for url in url_list}
    original_url = url_dict[shortened_url]
    return original_url


def get_shortened_url(original_url):
    url_list = read_url()
    url_dict = {url["original_url"]: url["shortened_url"] for url in url_list}
    shortened_url = url_dict[original_url]
    return shortened_url


def increase_used_time(shortened_url):
    url_db = db.reference("url").get()
    url_dict = {
        url_db[item]["shortened_url"]: [item, url_db[item]["used_times"]]
        for item in url_db
    }
    db.reference("/url/").child(url_dict[shortened_url][0]).update(
        {"used_times": url_dict[shortened_url][1] + 1}
    )


def main():
    config = configparser.ConfigParser()
    config.read("../private/54.ini")

    key = config["firebase"]["key_path"]
    database_url = config["firebase"]["database_url"]
    cred = credentials.Certificate(key)
    myapp = firebase_admin.initialize_app(cred, {"databaseURL": database_url})

    run_server()


main()
