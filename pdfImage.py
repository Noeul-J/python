import fitz     # pip install PyMuPDF
import io
import os
from PIL import Image    # pip install pillow
from pdf2image import convert_from_path, convert_from_bytes      # pip install pdf2image
import sys

def save_Image(saveImgPath, assetId):
    # file = "C:\RPA\SCN1_Macquarie\OUTPUT\\221230\\7609\\7609.pdf"
    file = os.path.join(saveImgPath, assetId + ".pdf")

    # open the file
    pdf_file = fitz.open(file)
    images = convert_from_path(file)

    # PDF page 만큼 반복
    for page_index in range(len(pdf_file)):

        # 해당 페이지 이미지 읽어오기
        image_list = pdf_file.get_page_images(page_index)

        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
            images[page_index-1].save()

        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(f"{saveImgPath}{assetId}_{page_index}.jpeg", "jpeg")



if __name__ == '__main__':
    # assetId = sys.argv[1]
    # saveImgPath = sys.argv[2]

    # saveImgPath = 'C:\RPA\SCN1_Macquarie\OUTPUT\\221230\\7609\\'
    saveImgPath = 'C:\RPA\\'
    assetId = 'testPDF'

    save_Image(saveImgPath, assetId)
    print("이미지 저장 완료")

