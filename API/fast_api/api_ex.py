# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI

api = FastAPI()


@api.get('/random_number')
def random_no():
    import random
    val_random_number = random.randint(1, 10)

    return val_random_number


@api.get('/hello')
def hello(name=None):
    if name is None:
        result_str = 'Hello. no name'
    else:
        result_str = 'Hello. ' + name

    return result_str


@api.get('/get_csv')
def get_csv():
    import pandas as pd
    csv_file = 'sample.csv'

    df_sample = pd.read_csv(csv_file)
    dict_sample = df_sample.to_dict()       # DataFrame을 dictionary로 바꿔서 return

    return dict_sample

