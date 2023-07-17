from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('variable.html', name=user, id=230433)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')