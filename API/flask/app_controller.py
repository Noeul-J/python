from flask import Flask, request, json, jsonify

app = Flask(import_name=__name__)


@app.route("/test", methods=['POST'])
def test():
    params = request.form.get('name', None)
    print("받은 json 데이터 ", params)

    response = {
        "result": "ok"
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=8000)