import random
import argparse
import sys

import uni_image
from unicorns import *


def main():
    parser = argparse.ArgumentParser(description='Displays unicorns if you are feeling down, or just like unicorns')
    parser.add_argument('-t', '--text', action='store_true', help='shows a text based image in the shell')
    parser.add_argument('-i', '--image', action='store_true', help='opens an image of a unicorn')

    args = parser.parse_args()

    # if args.command is None:
    #     parser.parse_args(['-h'])
    #     sys.exit()

    unicorn_list = [fat_unicorn, full_unicorn, basic_unicorn, chubby_unicorn, unicorn_head]
    pic_list = uni_image.load_images_from_folder("res/")

    if args.text:
        print(random.choice(unicorn_list))

    elif args.image:
        uni_im = random.choice(pic_list)
        uni_im.show()

    else:
        parser.parse_args(['-h'])
        sys.exit()


if __name__ == '__main__':
    main()
