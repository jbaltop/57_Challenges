import time
from flask import Flask
from flask_restful import Resource, Api


class UTCTime(Resource):
    def get(self):
        return {
            "current_time": "{}".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            )
        }


def main():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(UTCTime, "/time")
    app.run(port=8008)


main()
