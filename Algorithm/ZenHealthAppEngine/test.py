from flask import Flask, request
app = Flask(__name__)


@app.route('/' , methods=['POST'])
def test():
    userid = request.get_json()['X']
    print(userid)  # For debugging
    return 'Success!' + userid

if __name__ == '__main__':
   app.run(debug = True)