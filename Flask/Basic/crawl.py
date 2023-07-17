from flask import Flask
import requests

app = Flask(__name__)

@app.route('/google')
def get_goole():
    response = requests.get('http://www.google.co.kr')
    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')