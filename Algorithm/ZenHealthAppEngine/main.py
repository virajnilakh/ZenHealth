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
from google.cloud import storage
import pickle

# app = Flask(__name__)
# app.debug = True
service = ZenhealthService()
#CORS(app)



MODEL_BUCKET = os.environ['MODEL_BUCKET']
USER_MODEL_FILENAME = os.environ['MODEL_FILENAME']
RECOMMENDER_MODEL_FILENAME = os.environ['MODEL_FILENAME']
USER_MODEL = None
RECOMMENDER_MODEL = None


# API list

'''
GET     /v1/zenhealth/ping
        Ping the applciation to test its access

'''

@app.before_first_request
def _load_models():
    global USER_MODEL
    global RECOMMENDER_MODEL
    client = storage.Client()
    bucket = client.get_bucket(MODEL_BUCKET)
    blob = bucket.get_blob(USER_MODEL_FILENAME)
    user = blob.download_as_string()

    # Note: Change the save/load mechanism according to the framework
    # used to build the model.
    USER_MODEL = pickle.loads(user)
    blob = bucket.get_blob(RECOMMENDER_MODEL_FILENAME)
    recom = blob.download_as_string()

    # Note: Change the save/load mechanism according to the framework
    # used to build the model.
    RECOMMENDER_MODEL = pickle.loads(recom)


def getAPP():
    return app

@app.route("/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status': 'ok', 'message': 'Zenhealth API service :v1'})

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

@app.route("/getFoodRecommendations", methods=['GET'])
def foodRecommendations():

    args = request.args
    print(args)  # For debugging
    uname = args['uname']
    timeslot = int(args['timeslot'])
    bglevel = float(args['bglevel'])
    sugarConsumed = float(args['sugarConsumed'])
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

    app.run(host='0.0.0.0', port=8080, debug=True)