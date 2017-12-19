from flask import Flask, render_template, request, session, flash, redirect, jsonify, json, Response
from flask_restful import Resource, Api
from resources.Analysis import Analysis as Service
import app

service = Service()

class API(Resource):

    @app.route("/ping")
    def getPing(self):
        print("ping successfull")
        return json.dumps({'status': 'ok', 'message': 'Starbucks API service :v1'})

    @app.route("/low")
    def getLow(self):
        lowbucket = service.getLowBucket()
        resp = Response(json.dumps(lowbucket.to_json()))
        #resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp

    @app.route("/medium")
    def getMedium(self):
        mediumbucket = service.getMediumBucket()
        resp = Response(json.dumps(mediumbucket.to_json()))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp

    @app.route("/high")
    def getHigh(self):
        highbucket = service.getHighBucket()
        resp = Response(json.dumps(highbucket.to_json()))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Content-Type'] = 'application/json'
        return resp

    def post(self):
        return {'status': 'approved'}

    @app.route("/<int:id>")
    def put(self):
        return {'status': 'updated', 'name': 'amz'}

    @app.route("/<int:id>")
    def delete(self):
        return {'status': 'deleted'}