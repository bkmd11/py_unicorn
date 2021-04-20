import random
import argparse
import sys

from pprint import pprint

from unicorns import uni_google, uni_image, uni_corns
from unicorns.uni_corns import *


def main():
    parser = argparse.ArgumentParser(description='Displays unicorns if you are feeling down, or just like unicorns')
    parser.add_argument('-t', '--text', action='store_true', help='shows a text based image of a unicorn')
    parser.add_argument('-i', '--image', action='store_true', help='opens an image of a unicorn')
    parser.add_argument('-r', '--random', action='store_true', help='randomly shows some time of unicorn')
    parser.add_argument('-g', '--google', action='store_true', help='googles "{description} unicorn"')
    parser.add_argument('-kw', '--keyword', metavar='key word for specific unicorn', nargs='?',
                        help='takes a key word to find a specific unicorn')

    args = parser.parse_args()

    unicorn_list = [fat_unicorn, majestic_unicorn, basic_unicorn, chubby_unicorn, head_unicorn]
    pic_list = uni_image.load_images_from_folder()
    google_list = ['fat', 'chubby', 'majestic', 'prancing', 'rude', 'sexy', 'ripped', 'swole', 'cat', 'salty']
    random_list = [unicorn_list, pic_list, google_list]

    if args.text:
        if args.keyword:
            uni = globals().get(f'{args.keyword}_unicorn')
            if uni:
                print(uni)
            else:
                for i in uni_corns.__text_keywords():
                    print(i)
        else:
            print(random.choice(unicorn_list))
    elif args.image:
        if args.keyword:
            image = uni_image.load_keyword_image(args.keyword)
            try:
                image.show()
            except AttributeError:
                for i in image:
                    print(i)
        else:
            uni_im = random.choice(pic_list)
            uni_im.show()
    elif args.google:
        if args.keyword:
            uni_google.uni_launch(args.keyword)
        else:
            word = random.choice(google_list)
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
