from flask import Flask, jsonify, request, render_tempalte, make_response
import os

# https 만을 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    # host = "161.122.37.174"
    # port = "8480"
    app.run(host=host, port=port)