import random
import argparse
import sys

from unicorns import uni_google, uni_image
from unicorns.uni_corns import *


def main():
    parser = argparse.ArgumentParser(description='Displays unicorns if you are feeling down, or just like unicorns')
    parser.add_argument('-t', '--text', action='store_true', help='shows a text based image of a unicorn')
    parser.add_argument('-i', '--image', action='store_true', help='opens an image of a unicorn')
    parser.add_argument('-r', '--random', action='store_true', help='randomly shows some time of unicorn')
    parser.add_argument('-g', '--google', metavar='description of unicorn', nargs='?', help='googles "{description} unicorn"')

    args = parser.parse_args()

    unicorn_list = [fat_unicorn, full_unicorn, basic_unicorn, chubby_unicorn, unicorn_head]
    pic_list = uni_image.load_images_from_folder("res/")
    google_list = ['fat', 'chubby', 'majestic', 'prancing', 'rude', 'sexy', 'ripped', 'swole', 'cat', 'salty']
    random_list = [unicorn_list, pic_list, google_list]

    if args.text:
        print(random.choice(unicorn_list))
    elif args.image:
        uni_im = random.choice(pic_list)
        uni_im.show()
    elif args.google:
        word = args.google
        uni_google.uni_launch(word)
    elif args.random:
        choice = random.choice(random_list)

        if choice == unicorn_list:
            print(random.choice(unicorn_list))
        elif choice == pic_list:
            uni_im = random.choice(pic_list)
            uni_im.show()
        else:
            word = random.choice(google_list)
            uni_google.uni_launch(word)
    else:
        parser.parse_args(['-h'])
        sys.exit()


if __name__ == '__main__':
    main()
