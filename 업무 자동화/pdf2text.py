import pdfplumber

def get_text(page):
    text = page.extract_text() # 한 페이지의 텍스트 추출
    return text

def pdf2text(fname):
    pdf = pdfplumber.open(fname)    # pdf 파일 열기
    pages = pdf.pages               # 페이지 추출
    text = ""
    for pg in pages:                # 모든 페이지에 대해서
        text += get_text(pg)
    return text


if __name__ == '__main__':
    excel_fname= pdf2text('C:\\RPA\\TEST\\정보공개서\\test.pdf')