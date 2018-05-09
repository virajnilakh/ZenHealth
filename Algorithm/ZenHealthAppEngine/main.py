'''

Main file to be deployed on app engine.
Main entry to analysis

'''

from flask import Flask, json, Response, request
from resources.Service import Service\
    as ZenhealthService
import os
import logging
from resources.connection import app

# app = Flask(__name__)
# app.debug = True
service = ZenhealthService()
#CORS(app)



# USER_MODEL_BUCKET = os.environ['MODEL_BUCKET']
# USER_MODEL_FILENAME = os.environ['MODEL_FILENAME']
# USER_MODEL = None
# RECOMMENDER_MODEL = None


# API list

'''
GET     /v1/zenhealth/ping
        Ping the applciation to test its access

'''

# @app.route("/v1/zenloop/ping", methods=['GET'])
# def testPing():
#     print("ping successfull")
#     return json.dumps({'status': 'ok', 'message': 'Zenhealth API service :v1'})
#
# @app.route("/v1/zenloop/test", methods=['GET'])
# def test():
#
#     args = request.args
#     print(args)  # For debugging
#     userid = args['userid']
#     timeslot = int(args['timeslot'])
#     bglevel = float(args['bglevel'])
#     sugarConsumed = float(args['sugarConsumed'])
#     recommendations = service.test(userid, timeslot, bglevel, sugarConsumed)
#     resp = Response(json.dumps(recommendations))
#         # resp.headers['Access-Control-Allow-Origin'] = '*'
#     resp.headers['Content-Type'] = 'app/json'
#     return resp


def getAPP():
    return app


@app.route("/recommendFood", methods=['POST'])
def getFoodRecommendations():


    uname = request.get_json()['uname']
    timeslot = int(request.get_json()['timeslot'])
    bglevel = float(request.get_json()['bglevel'])
    sugarConsumed = float(request.get_json()['sugarConsumed'])
    recommendations = service.getResults(uname, timeslot, bglevel, sugarConsumed)
    resp = Response(json.dumps(recommendations))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'app/json'
    return resp


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == "__main__":
    print("running on 0.0.0.0")

    app.run(debug=True)