from flask import Flask, json, Response, request
from resources.API import API as ZenhealthService
#from flask_cors import CORS
import os

app = Flask(__name__)
app.debug = True
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

@app.route("/v1/zenloop/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status': 'ok', 'message': 'Zenhealth API service :v1'})

@app.route("/v1/zenloop/test", methods=['GET'])
def test():

    args = request.args
    print(args)  # For debugging
    userid = args['userid']
    timeslot = int(args['timeslot'])
    bglevel = float(args['bglevel'])
    sugarConsumed = float(args['sugarConsumed'])
    recommendations = service.test(userid, timeslot, bglevel, sugarConsumed)
    resp = Response(json.dumps(recommendations))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'app/json'
    return resp


@app.route("/v1/zenloop/foodRecommendations", methods=['GET'])
def getFoodRecommendations():

    args = request.args
    print(args)  # For debugging
    userid = args['userid']
    timeslot = int(args['timeslot'])
    bglevel = float(args['bglevel'])
    sugarConsumed = float(args['sugarConsumed'])
    recommendations = service.getResults(userid, timeslot, bglevel, sugarConsumed)
    resp = Response(json.dumps(recommendations))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'app/json'
    return resp


# @app.before_first_request
# def getFoodRecommendations():
#
#     args = request.args
#     print(args)  # For debugging
#     userid = args['userid']
#     timeslot = int(args['timeslot'])
#     bglevel = float(args['bglevel'])
#     sugarConsumed = float(args['sugarConsumed'])
#     recommendations = service.getFoodRecom(userid, timeslot, bglevel, sugarConsumed)
#     resp = Response(json.dumps(recommendations))
#         # resp.headers['Access-Control-Allow-Origin'] = '*'
#     resp.headers['Content-Type'] = 'app/json'
#     return resp
#
#
# @app.before_first_request
# def getFoodRecommendations():
#
#     args = request.args
#     print(args)  # For debugging
#     userid = args['userid']
#     timeslot = int(args['timeslot'])
#     bglevel = float(args['bglevel'])
#     sugarConsumed = float(args['sugarConsumed'])
#     recommendations = service.getFoodRecom(userid, timeslot, bglevel, sugarConsumed)
#     resp = Response(json.dumps(recommendations))
#         # resp.headers['Access-Control-Allow-Origin'] = '*'
#     resp.headers['Content-Type'] = 'app/json'
#     return resp

if __name__ == "__main__":
    print("running on 0.0.0.0")
    app.run(debug=True)