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


def save_image(save_img_path, asset_id):
    # file = "C:\RPA\SCN1_Macquarie\OUTPUT\\221230\\7609\\7609.pdf"
    file = os.path.join(save_img_path, asset_id + "_01.pdf")
    print(file)

    # open the file
    pdf_file = fitz.open(file)
    # images = convert_from_path(file)

    # img_save_start = False
    img_count = 2

    # PDF page 만큼 반복
    for page_index in range(len(pdf_file)):

        # 해당 페이지 이미지 읽어오기
        image_list = pdf_file.get_page_images(page_index)

        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index + 1}")

            for image_index, img in enumerate(image_list, start=1):
                xref = img[0]
                base_image = pdf_file.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))
                if img_count < 10:
                    img_count = '0' + str(img_count)
                image.save(f"{save_img_path}{asset_id}_{img_count}.jpeg", "jpeg")
                img_count = int(img_count) + 1
                # img_save_start = True
        else:
            print("[!] No images found on page", (page_index + 1))
            # if not img_save_start :
            #     images[page_index].save(f"{saveImgPath}{assetId}_{img_count}.jpeg", "jpeg")
            # img_count = int(img_count) + 1


if __name__ == '__main__':
    asset_id_from_wd = sys.argv[1]
    save_img_path_from_wd = sys.argv[2]

    # save_img_path_from_wd = 'C:\\RPA\\TEST\\'
    # asset_id_from_wd = '204911'

    save_image(save_img_path_from_wd, asset_id_from_wd)
    print("이미지"" 저장 완료")
