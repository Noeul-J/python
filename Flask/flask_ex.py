from flask import Flask, make_response, jsonify, request


app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello world</h1>"


@app.route('/hello')
def hello_flask():
    return "<h1>Hello Flash!</h1>"


@app.route('/profile/<string:username>')
def get_profile(username):
    return "<h3>Hello " + username + " !</h3>"


@app.route('/id/<int:user_id>')
def hello_first(user_id):
    return "user id: %d " % user_id         # %d는 int, %f는 float, %s는 string

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify(success=True), 200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")