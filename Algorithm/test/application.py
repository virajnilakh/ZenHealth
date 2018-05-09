from flask import Flask, json, Response, request


app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status': 'ok', 'message': 'Zenhealth API service :v1'})


if __name__ == "__main__":
    print("running on 0.0.0.0")
    app.run(debug=True,host='0.0.0.0')