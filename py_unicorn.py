import random
import uni_image

from unicorns import *

unicorn_list = [fat_unicorn, full_unicorn, basic_unicorn, chubby_unicorn, unicorn_head]

pic_list = uni_image.load_images_from_folder("res/")

if __name__ == '__main__':
    uni = random.choice(pic_list)
    uni.show()
