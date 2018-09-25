import urllib.request
import xml.etree.ElementTree as etree
from flask import Flask, render_template, request


def flickr_search(search_word):

    url = "https://api.flickr.com/services/feeds/photos_public.gne?tags={}".format(
        search_word
    )

    image_xml = urllib.request.urlopen(url).read().decode("utf-8")

    return image_xml


def make_image_xml_file(image_xml):
    fout = open("49.xml", "wt", encoding="utf-8")
    fout.write(image_xml)
    fout.close


def parse_xml():
    tree = etree.parse("49.xml")
    root = tree.getroot()

    all_links = tree.findall("//{http://www.w3.org/2005/Atom}link")

    link_list = []
    for link in all_links:
        if link.attrib["rel"] == "enclosure":
            link_list.append(link.attrib["href"])

    return link_list


def run_server():
    app = Flask(__name__, template_folder="../templates")

    @app.route("/")
    def home():
        return render_template("49_input.html")

    @app.route("/search", methods=["POST"])
    def search():
        search_word = request.form["search_word"]
        make_image_xml_file(flickr_search(search_word))
        link_list = parse_xml()
        return render_template(
            "49_output.html", keyword=search_word, link_list=link_list
        )

    app.run(port=8001)


def main():
    run_server()


main()
