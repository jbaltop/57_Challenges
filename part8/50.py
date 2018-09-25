import urllib.request
import json
import re
import configparser


def main():
    config = configparser.ConfigParser()
    config.read("../private/50.ini")

    apikey = config["themoviedb"]["key"]

    messages = {
        "api": "\nEnter your API key: ",
        "name": "\nEnter the name of the movie: ",
        "title": "\nTitle: {}",
        "year": "\nYear: {}",
        "rating": "\nRating: {}",
        "overview": "\nOverview: {}",
        "m1": "\n\nYou should watch this movie right now!",
        "m2": "\n\nYou shouldn't watch this movie.",
    }

    name = input(messages["name"])
    name = re.sub(" ", "+", name)

    url = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}"
    full_url = url.format(apikey, name)

    movie_json = urllib.request.urlopen(full_url).read().decode("utf-8")

    movie_dictionary = json.loads(movie_json)

    title = movie_dictionary["results"][0]["title"]
    release_date = movie_dictionary["results"][0]["release_date"]
    year = release_date[0:4]
    rating = movie_dictionary["results"][0]["vote_average"]
    overview = movie_dictionary["results"][0]["overview"]

    message = (
        messages["title"].format(title)
        + messages["year"].format(year)
        + messages["rating"].format(rating)
        + messages["overview"].format(overview)
    )

    if rating >= 8:
        message = message + messages["m1"]
    elif rating < 5:
        message = message + messages["m2"]

    message = message + "\n"

    print(message)


main()
