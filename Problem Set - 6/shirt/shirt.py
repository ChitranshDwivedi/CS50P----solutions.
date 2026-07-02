import sys
import os


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


input_ext = sys.argv[1].lower()
output_ext = sys.argv[2].lower()

if not input_ext.endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid input")

if not output_ext.endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")

input_name, input_extension = os.path.splitext(input_ext)
output_name, output_extension = os.path.splitext(output_ext)

if input_extension != output_extension:
    sys.exit("Input and output have different extensions")

if not os.path.exists(sys.argv[1]):
    sys.exit("Input does not exist")

from PIL import Image, ImageOps

with Image.open(sys.argv[1]) as input_image, Image.open("shirt.png") as shirt_image:
    input_image = ImageOps.fit(input_image, shirt_image.size)
    input_image.paste(shirt_image, shirt_image)
    input_image.save(sys.argv[2])
