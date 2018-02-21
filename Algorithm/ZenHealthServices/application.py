from flask import Flask, render_template, request, session, flash, redirect, jsonify, json, Response
from flask.views import MethodView
import uuid
from resources.Analysis import Analysis as ZenhealthService
#from flask_cors import CORS

application = Flask(__name__)
application.debug = True
service = ZenhealthService()
#CORS(application)
# API list

'''
GET     /v1/zenhealth/ping
        Ping the applciation to test its access

'''


@application.route("/v1/zenhealth/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status': 'ok', 'message': 'Zenhealth API service :v1'})


@application.route("/v1/zenhealth/low", methods=['GET'])
def getLow():
        lowbucket = service.getLowBucket()
        resp = Response(json.dumps(lowbucket.to_json()))
        #resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp


@application.route("/v1/zenhealth/medium", methods=['GET'])
def getMedium():
        mediumbucket = service.getMediumBucket()
        resp = Response(json.dumps(mediumbucket.to_json()))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp


@application.route("/v1/zenhealth/high", methods=['GET'])
def getHigh():
        highbucket = service.getHighBucket()
        resp = Response(json.dumps(highbucket.to_json()))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp

if __name__ == "__main__":
    print("running on 0.0.0.0")
    application.run(debug=True)