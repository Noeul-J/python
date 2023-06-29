import pandas as pd
import difflib

# 파일명
file_name = 'ocr_result.xlsx'

# 엑셀 파일 읽기
ocr = pd.read_excel(file_name, sheet_name='OCR_결과')
answer = pd.read_excel(file_name, sheet_name='정답지_결과')

# print(ocr)
# print()
# print(answer)

# 데이터 프레임 생성
similar_list = []


# 셀 비교
for col in ocr.columns:
    for row in range(0, len(ocr)-1):
        if ocr[col][row] == answer[col][row]:
            similar = 1.0
            # print(similar)
        else:
            ocr_bytes = bytes(str(ocr[col][row]), 'utf-8')
            answer_bytes = bytes(str(answer[col][row]), 'utf-8')
            ocr_bytes_list = list(ocr_bytes)
            answer_bytes_list = list(answer_bytes)

            sm = difflib.SequenceMatcher(None, answer_bytes_list, ocr_bytes_list)
            similar = sm.ratio()

            # print(similar)

        similar_list.append(similar)

    if col == '생산자' and row == len(ocr)-1:
        similar_df = pd.DataFrame(similar_list)
        # similar_df.append(similar_list)
        similar_list = []
        display(similar_df.to_string())
        break



