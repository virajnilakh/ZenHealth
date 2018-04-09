from flask import Flask
from flask_restful import Api
from resources.API import API as API


app = Flask(__name__)
api = Api(app)


api.add_resource(API,'/zenhealth/API')

if __name__ == '__main__':
    app.run(debug=True)
