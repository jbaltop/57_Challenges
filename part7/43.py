import os


def main():
    messages = {
        "site": "Site name: ",
        "author": "Author: ",
        "js": "Do you want a folder for JavaScript(Y/n)? ",
        "css": "Do you want a folder for CSS(Y/n)? ",
        "m1": "Created ./{}/",
        "m2": "Created ./{}/js/",
        "m3": "Created ./{}/css/",
        "m4": "Created ./{}/index.html",
    }

    site = input(messages["site"])
    author = input(messages["author"])
    js = input(messages["js"])
    css = input(messages["css"])

    os.mkdir("./{}".format(site))
    print(messages["m1"].format(site))

    if js.lower() != "n":
        os.mkdir("./{}/js".format(site))
        print(messages["m2"].format(site))

    if css.lower() != "n":
        os.mkdir("./{}/css".format(site))
        print(messages["m3"].format(site))

    content = (
        '<!doctype html>\n<html>\n  <head>\n    <meta name="author" content="'
        + author
        + '">\n    <title>"'
        + site
        + '"</title>\n  </head>\n</html>'
    )

    fout = open("{}/index.html".format(site), "wt", encoding="utf-8")
    fout.write(content)
    fout.close()
    print(messages["m4"].format(site))


main()
