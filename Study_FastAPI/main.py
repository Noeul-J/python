from fastapi import FastAPI

app = FastAPI()

# 경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언할 때, "쿼리" 매개변수로 자동 해석


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get('/items/')
def read_items(skip: int=0, limit: int=10):
    return fake_items_db[skip : skip + limit]