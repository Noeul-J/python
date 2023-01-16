"""
[PDF에서 이미지 출력]
if 이미지가 없으면 해당 페이지 이미지화 해서 저장
else 이미지 부분만 이미지 파일로 저장

<라이브러리>
fitz ---- pip install PyMuPDF
PIL  ---- pip install pillow
pdf2image --- pip install pdf2image

poppler 에러 발생 시(anaconda 사용 시)
conda install -c conda-forge poppler
"""

import fitz
import io
import os
from PIL import Image
from pdf2image import convert_from_path
import sys

def save_Image(saveImgPath, assetId):
    # file = "C:\RPA\SCN1_Macquarie\OUTPUT\\221230\\7609\\7609.pdf"
    file = os.path.join(saveImgPath, assetId + ".pdf")

    # open the file
    pdf_file = fitz.open(file)
    images = convert_from_path(file)

    img_save_start = False

    # PDF page 만큼 반복
    for page_index in range(len(pdf_file)):

        # 해당 페이지 이미지 읽어오기
        image_list = pdf_file.get_page_images(page_index)

        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")

            for image_index, img in enumerate(image_list, start=1):
                xref = img[0]
                base_image = pdf_file.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image = Image.open(io.BytesIO(image_bytes))
                image.save(f"{saveImgPath}{assetId}_{page_index}_{image_index}.jpeg", "jpeg")
                img_save_start = True
        else:
            print("[!] No images found on page", page_index)
            if not img_save_start :
                images[page_index].save(f"{saveImgPath}{assetId}_{page_index}.jpeg", "jpeg")


if __name__ == '__main__':
    # assetId = sys.argv[1]
    # saveImgPath = sys.argv[2]

    saveImgPath = 'C:\RPA\\TEST\\'
    assetId = '204911_01'

    save_Image(saveImgPath, assetId)
    print("이미지 저장 완료")

