from flask import Flask, jsonify, abort, request
from flask_restful import Resource, Api
from resources.API import API as API
import resources.Analysis as Service


app = Flask(__name__)
api = Api(app)


api.add_resource(API,'/zenhealth/API')

if __name__ == '__main__':
    app.run(debug=True)
