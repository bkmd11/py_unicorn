import random
from PIL import Image
from unicorns import *

unicorn_list = [fat_unicorn, full_unicorn, basic_unicorn, chubby_unicorn, unicorn_head]

if __name__ == '__main__':
    im = Image.open('res/creep_uni.jpg')
    im.show()
