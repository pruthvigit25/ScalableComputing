import csv
import os
import numpy
import random
import string
import cv2
import argparse
import captcha.image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', help='Width of captcha image', type=int)
    parser.add_argument('--height', help='Height of captcha image', type=int)
    parser.add_argument('--length', help='Length of captchas in characters', type=int)
    parser.add_argument('--count', help='How many captchas to generate', type=int)
    parser.add_argument('--output-dir', help='Where to store the generated captchas', type=str)
    parser.add_argument('--output-csv', help='csv to store the generated captchas', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    args = parser.parse_args()

    if args.width is None:
        print("Please specify the captcha image width")
        exit(1)

    if args.height is None:
        print("Please specify the captcha image height")
        exit(1)

    if args.length is None:
        print("Please specify the captcha length")
        exit(1)

    if args.count is None:
        print("Please specify the captcha count to generate")
        exit(1)

    if args.output_dir is None:
        print("Please specify the captcha output directory")
        exit(1)

    if args.output_csv is None:
        print("Please specify the captcha output csv list file")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    captcha_generator = captcha.image.ImageCaptcha(width=args.width, height=args.height)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    captcha_symbols = captcha_symbols.replace(' ', '')  # remove spaces in the symbols file
    symbols_file.close()

    print("Generating captchas with symbol set {" + captcha_symbols + "}")

    if not os.path.exists(args.output_dir):
        print("Creating output directory " + args.output_dir)
        os.makedirs(args.output_dir)

    with open(args.output_csv, "w") as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        for i in range(args.count):
            # random_str = ''.join([random.choice(captcha_symbols) for j in range(args.length)])
            random_str = ''.join([random.choice(captcha_symbols) for j in range(random.choice(range(1, args.length+1)))])
            space_length = args.length-len(random_str)  # 6 minus current length
            # insert space randomly into string
            for n in range(space_length):
                index = random.randint(0, len(random_str))
                random_str = "".join([random_str[:index], ' ', random_str[index:]])
            image_path = os.path.join(args.output_dir, str(i) + '.png')
            if os.path.exists(image_path):
                version = 1
                while os.path.exists(os.path.join(args.output_dir, random_str + '_' + str(version) + '.png')):
                    version += 1
                image_path = os.path.join(args.output_dir, random_str + '_' + str(version) + '.png')

            # write file name and image content into csv
            writer.writerow([str(i) + '.png', random_str])

            image = numpy.array(captcha_generator.generate_image(random_str))
            cv2.imwrite(image_path, image)

if __name__ == '__main__':
    main()


