import os
from PIL import Image


def load_images_from_folder(folder):
    """ I load all the images in the res folder"""
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images