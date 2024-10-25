import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_command_line_arg()

    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_file = Image.open("shirt.png")
    shirt_size = shirt_file.size
    muppet = ImageOps.fit(image_file, shirt_size)
    muppet.paste(shirt_file, shirt_file)
    muppet.save(sys.argv[2])


def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if not check_extensions(file1[1]):
        sys.exit("Invalid Input")
    if not check_extensions(file2[1]):
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extensions(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
