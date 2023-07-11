from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.conn import get_db
from app.crud import crud_test
from app.apis import test   # main Logic

router = APIRouter(
    prefix="/items",    # url 앞에 고정적으로 붙는 경로 추가
)   # Route 분리


@router.get('test_route') # Route Path
def test_index(db: Session = Depends(get_db)):

    res = test.test_index(db=db)    #apis 호출

    return{
        "res": res,
    }   # 결과

