from flask import Flask
from flask import request
from flask import jsonify

api = Flask(import_name=__name__)


@api.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        name = request.args.get('name', None)
    elif request.method == 'POST':
        name = request.form.get('name', None)
    else:
        name = None

    if name is None:
        result_str = 'Hello. No name'
    else:
        result_str = 'Hello. ' + name

    return jsonify({'result': result_str})      # dictionary를 JSON 타입으로 변환


@api.route('/get_csv', methods=['GET'])
def get_csv():
    import pandas as pd

    df_sample = pd.read_csv('sample.csv')
    dict_sample = df_sample.to_dict()

    return jsonify({'csv': dict_sample, 'date': 20230704})


if __name__ == '__main__':
    api.run(debug=True, port=8000)