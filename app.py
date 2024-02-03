

!pip install rembg

import rembg
from PIL import Image

def remove_background(input_image_path, output_image_path):
    with open(input_image_path, "rb") as f:
        input_image = f.read()

    output_image = rembg.remove(input_image)

    with open(output_image_path, "wb") as f:
        f.write(output_image)

if __name__ == "__main__":
    input_image_path = "input_image.jpg" #please add  image that to be checked in input image path.
    output_image_path = "output_image.png"

    remove_background(input_image_path, output_image_path)