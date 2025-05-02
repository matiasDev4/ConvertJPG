import pydicom 
import sys
from PIL import Image
import numpy as np
import pathlib
import threading
import os
import docx2pdf as dx

from pdf2image import convert_from_path

get_download_folder = pathlib.Path.home() / 'downloads' 
folder_save_dicom = get_download_folder / 'IMAGENES DICOM'
folder_save_dicom.mkdir(parents=True, exist_ok=True)

folder_save_images = get_download_folder / 'IMAGENES WORD Y PDF'
folder_save_images.mkdir(parents=True, exist_ok=True)


def get_poppler():
    if getattr(sys, 'frozen', False):
        path = sys._MEIPASS
        return os.path.join(path, 'poppler', 'bin')
    else:
        return os.path.abspath(os.path.join('.', 'poppler', 'bin'))

def convert_dicom_to_image(file_path: str):
    try:
        ds = pydicom.dcmread(file_path)
        
        image = ds.pixel_array.astype(float)
        shape = image.shape 
        filename = pathlib.Path(file_path).stem
        match len(shape):
            case 2:
                get_image_normalized = normalized_image(image)
                get_image_normalized.save(f'{folder_save_dicom}/{filename.lower()}.jpg')

            case 3:
                for img in range(image.shape[0]):
                    images = image[img]
                    get_image_normalized = normalized_image(images)
                    get_image_normalized.save(f'{folder_save_dicom}/{filename.lower()}_{img + 1:03d}.jpg')
                    return image.shape
        

    except Exception as e:
        print(e)

def normalized_image(image):
    scale_image = (image / image.max()) * 255.0
    scal_img = scale_image.astype(np.uint8)
    out_image = Image.fromarray(scal_img)
    return out_image

def convert_pdf_to_image(path: str, filename):
    poppler_path = get_poppler()
    

    pdf = convert_from_path(path, dpi=150, poppler_path=poppler_path)

    for index, pages in enumerate(pdf):
        pages.save(folder_save_images / f'{filename}_{index+1}.jpg', 'JPEG')

def convert_word_to_image(path: str, filename):
    get_pdf = dx.convert(path)
    print(path)
    print(get_pdf)
    pdf = convert_from_path(get_pdf)
    print(pdf)
    for index, pages in enumerate(pdf):
        pages.save(folder_save_images / f'{filename}_{index + 1}.jpg', 'JPEG')

        
