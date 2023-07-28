import pandas as pd


def create_pivot_table(data_frame, rows, columns, values, filters=None):
    try:
        # 피벗테이블 생성
        pivot_table = pd.pivot_table(data_frame, index=rows, columns=columns, values=values, aggfunc='sum',
                                     fill_value=0)

        # 필터 적용
        if filters:
            for column, value in filters.items():
                pivot_table = pivot_table[pivot_table[column] == value]

        return pivot_table

    except KeyError:
        # 필터 대상 아이템이 없는 경우 예외 처리
        print("필터 대상 아이템이 없습니다.")
        return None


# 예시 데이터 프레임
data = {
    'Category': ['A', 'A', 'B', 'B', 'C'],
    'Product': ['P1', 'P2', 'P1', 'P2', 'P1'],
    'Sales': [100, 150, 200, 120, 300]
}
df = pd.DataFrame(data)

# 피벗테이블 생성과 필터 설정
rows = 'Category'
columns = 'Product'
values = 'Sales'
filters = {'Product': 'P3'}  # 존재하지 않는 필터 대상 아이템으로 설정

pivot_table_result = create_pivot_table(df, rows, columns, values, filters)

if pivot_table_result is not None:
    print(pivot_table_result)