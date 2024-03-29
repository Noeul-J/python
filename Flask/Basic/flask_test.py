from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# 200 : 정상
# 400 : 유효하지 않은 파라미터 또는 잘못된 요청
# 401 : 승인되지 않은 액세스
# 403 : 액세스 금지
# 404 : 리소스를 찾을 수 없음
# 500 : 내부 서버 오류


@app.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    if request.method == 'POST':
        print('POST')
        data = request.get_json()
        print(data['email'])
    if request.method == 'GET':
        print('GET')
        user = request.args.get('email')
        print(user)
    if request.method == 'PUT':
        print('PUT')
        user = request.args.get('email')
        print(user)
    if request.method == 'DELETE':
        print('DELETE')
        user = request.args.get('email')
        print(user)
        
    return make_response(jsonify(status=True), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
