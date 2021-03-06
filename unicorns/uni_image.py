import os
from PIL import Image

FOLDER = 'unicorns/res/'
# TODO: probably should use pathlib for this


def load_images_from_folder():
    """ I load all the images in the res folder"""
    images = []
    for filename in os.listdir(FOLDER):
        img = Image.open(os.path.join(FOLDER, filename))
        if img is not None:
            images.append(img)
    return images


def load_keyword_image(word):
    """I attempt to find an image with a key word"""
    jpg = '{}_uni.jpg'.format(word)
    png = '{}_uni.png'.format(word)

    files = os.listdir(FOLDER)
    if jpg in files:
        return Image.open(os.path.join(FOLDER, jpg))
    elif png in files:
        return Image.open(os.path.join(FOLDER, png))
    else:
        error_message = keyword_options()
        error_message.insert(0, 'Unicorn not found try:')
        return error_message


def keyword_options():
    words = []
    files = os.listdir(FOLDER)
    for i in files:
        keyword = i.split('_')
        words.append(keyword[0])
    return words
