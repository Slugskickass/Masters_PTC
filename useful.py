from PIL import Image
import numpy as np
import os

def loadtiffs(file_name):
    img = Image.open(file_name)
    print('The Image is', img.size, 'Pixels.')
    print('With', img.n_frames, 'frames.')

    imgArray = np.zeros((img.size[1], img.size[0], img.n_frames), np.uint16)
    for I in range(img.n_frames):
        img.seek(I)
        imgArray[:, :, I] = np.asarray(img)
    img.close()
    return(imgArray)

def get_file_list(dir):
    file_list = []
    for file in os.listdir(dir):
        if file.endswith(".tiff"):
            file_name = dir + '/' +file
            file_list.append(file_name)
    return file_list

def createback(file):
    data = loadtiffs(file)
    data = np.mean(data, axis=2)
    return data