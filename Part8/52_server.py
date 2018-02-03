#!/usr/local/bin/python3

import time
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import flask_jsonpify

app = Flask(__name__)
api = Api(app)

class UTCTime(Resource):
	def get(self):
		return {"current_time": "{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))}

api.add_resource(UTCTime, '/time')

if __name__ == '__main__':
	app.run(port=8008)
