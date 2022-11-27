from rembg import remove
from PIL import Image
from pathlib import Path
import os


def delete_all_imgs(image_name):
    path_input, path_output = "./input_imgs", "./output_imgs"
    os.remove(path_input + image_name)
    os.remove(path_output + image_name)


def remove_bg(image_name):
    file_path = f"./input_imgs/{image_name}"

    input_path = Path(file_path)
    file_name = input_path.stem

    output_path = f'./output_imgs/{file_name}_output.png'

    input_img = Image.open(input_path)
    output_img = remove(input_img)
    output_img.save(output_path)
