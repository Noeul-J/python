from flask import Flask
from flask import request

api = Flask(import_name=__name__)       # 현재 파일 참조


@api.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', None)

    if name is None:
        result_str = 'Hello. no name'
    else:
        result_str = 'Hello. ' + name

    return result_str


@api.route('/get_csv', methods=['GET'])
def get_csv():
    import pandas as pd

    df_sample = pd.read_csv('sample.csv')
    dict_sample = df_sample.to_dict()

    return dict_sample


if __name__ == '__main__':
    api.run(debug=True, port=8000)      # 디버그 모드 활성화

