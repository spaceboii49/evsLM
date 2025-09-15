import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import re
import pickle

def data_loader():
    if os.path.exists('data/evs.pkl'):
        file = open('data/evs.pkl', 'rb')
        data = pickle.load(file)
        file.close()
        return data
    data = []
    for i in range(2, 3):
        filePath = rf"./data/{i}.pdf"
        doc = convert_from_path(filePath)
        path, fileName = os.path.split(filePath)
        fileBaseName, fileExtension = os.path.splitext(fileName)
        for page_number, page_data in enumerate(doc):
            txt = pytesseract.image_to_string(page_data).encode("utf-8")
            # print("Page # {} - {}".format(str(page_number), txt))
            txt = txt.decode("utf-8")
            data.append(re.sub(r'\s', ' ', txt).strip())
    try:
        file = open('data/evs.pkl', 'wb')
        pickle.dump(data, file)
        file.close()
    except Exception as e:
        print(f"error while saving data: {e}")
    return data