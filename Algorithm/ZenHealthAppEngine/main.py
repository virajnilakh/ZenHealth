from flask import Flask, json, Response, request
from resources.API import API as ZenhealthService
#from flask_cors import CORS

app = Flask(__name__)
app.debug = True
service = ZenhealthService()
#CORS(app)
# API list

'''
GET     /v1/zenhealth/ping
        Ping the applciation to test its access

'''


@app.route("/v1/zenhealth/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status': 'ok', 'message': 'Zenhealth API service :v1'})

@app.route("/v1/zenhealth/foodRecommendations", methods=['GET'])
def getFoodRecommendations():

    args = request.args
    print(args)  # For debugging
    userid = args['userid']
    timeslot = int(args['timeslot'])
    bglevel = float(args['bglevel'])
    sugarConsumed = float(args['sugarConsumed'])
    recommendations = service.getFoodRecom(userid, timeslot, bglevel, sugarConsumed)
    resp = Response(json.dumps(recommendations))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'app/json'
    return resp

#----------------------------------------------------------------
# @app.route("/v1/zenhealth/low", methods=['GET'])
# def getLow():
#         lowbucket = service.getLowBucket()
#         resp = Response(json.dumps(lowbucket.to_json()))
#         #resp.headers['Access-Control-Allow-Origin'] = '*'
#         resp.headers['Content-Type'] = 'app/json'
#         return resp
#
#
#
# @app.route("/v1/zenhealth/medium", methods=['GET'])
# def getMedium():
#         mediumbucket = service.getMediumBucket()
#         resp = Response(json.dumps(mediumbucket.to_json()))
#         # resp.headers['Access-Control-Allow-Origin'] = '*'
#         resp.headers['Content-Type'] = 'app/json'
#         return resp
#
#
# @app.route("/v1/zenhealth/high", methods=['GET'])
# def getHigh():
#         highbucket = service.getHighBucket()
#         resp = Response(json.dumps(highbucket.to_json()))
#         # resp.headers['Access-Control-Allow-Origin'] = '*'
#         resp.headers['Content-Type'] = 'app/json'
#         return resp

if __name__ == "__main__":
    print("running on 0.0.0.0")
    app.run(debug=True)