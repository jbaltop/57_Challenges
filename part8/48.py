import urllib.request
import json
import numpy
import configparser


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius)


def degree_to_azimuth(degree):
    azimuths = {
        0: "north",
        22.5: "north-northeast",
        45: "northeast",
        67.5: "east-norteast",
        90: "east",
        112.5: "east-southeast",
        135: "southeast",
        157.5: "south-southeast",
        180: "south",
        202.5: "south-southwest",
        225: "southwest",
        247.5: "west-southwest",
        270: "west",
        292.5: "west-northwest",
        315: "northwest",
        337.5: "north-northwest",
        360: "north",
    }

    a = numpy.array(
        [
            0,
            22.5,
            45,
            67.5,
            90,
            112.5,
            135,
            157.5,
            180,
            202.5,
            225,
            247.5,
            270,
            292.5,
            315,
            337.5,
            360,
        ]
    )
    idx = (numpy.abs(a - degree)).argmin()
    nearest_degree = a[idx]
    azimuth = azimuths[nearest_degree]
    return azimuth


def main():
    message_template = {
        "city": "\n{} weather: ",
        "temp": "\ntemperature: {}\u00b0C",
        "temp_min": "\nlowest temperature: {}\u00b0C",
        "temp_max": "\nhighest temperature: {}\u00b0C",
        "pressure": "\npressure: {}hPa",
        "humidity": "\nhumidity: {}%",
        "wind_speed": "\nwind speed: {}m/s",
        "wind_direction": "\nwind direction: {}",
    }

    config = configparser.ConfigParser()
    config.read("../private/48.ini")
    APIKEY = config["openweathermap"]["key"]

    city_name = input("\nWhere are you? ")

    api_url = "http://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}"
    full_api_url = api_url.format(city_name, APIKEY)

    weather_json = urllib.request.urlopen(full_api_url).read().decode("utf-8")

    weather_dictionary = json.loads(weather_json)

    city_name = weather_dictionary["city"]["name"]
    temp = kelvin_to_celsius(weather_dictionary["list"][0]["main"]["temp"])
    temp_min = kelvin_to_celsius(weather_dictionary["list"][0]["main"]["temp_min"])
    temp_max = kelvin_to_celsius(weather_dictionary["list"][0]["main"]["temp_max"])
    pressure = weather_dictionary["list"][0]["main"]["pressure"]
    humidity = weather_dictionary["list"][0]["main"]["humidity"]
    wind_speed = weather_dictionary["list"][0]["wind"]["speed"]
    azimuth = degree_to_azimuth(weather_dictionary["list"][0]["wind"]["deg"])

    message = (
        message_template["city"].format(city_name)
        + message_template["temp"].format(temp)
        + message_template["temp_min"].format(temp_min)
        + message_template["temp_max"].format(temp_max)
        + message_template["pressure"].format(pressure)
        + message_template["humidity"].format(humidity)
        + message_template["wind_speed"].format(wind_speed)
        + message_template["wind_direction"].format(azimuth)
    )

    print(message)


main()
