from PIL import Image
import os
from tqdm import tqdm

input_directory = "uncoverted"
output_directory = "converted"
set_of_formats = ["PNG", "JPEG", "WEBP", "TIFF"]
scaling_factors = [0.1, 0.25, 0.5, 0.75, 1.0]
compression_level = 50


def main():
    id = 0
    dir = os.listdir(input_directory)
    progress_bar = tqdm(total=len(dir))
    
    for file in dir:
        filename = os.path.splitext(file)[0]
        file_type = os.path.splitext(file)[1]
        id += 1
        input_path = os.path.join(input_directory, file)
        for scaling_factor in scaling_factors:
            for desired_format in set_of_formats:
                # output_path = os.path.join(
                #     output_directory, f"{new_filname}.{desired_format.lower()}")
                convert_image(input_path, output_directory, id,
                              desired_format, scaling_factor)
        progress_bar.update(1)


def convert_image(input_path, output_directory, image_id, desired_format, scaling_factor):
    image = Image.open(input_path)
    image = image.resize(
        (round(image.size[0]*scaling_factor), round(image.size[1]*scaling_factor)))
    xvalue = image.width
    yvalue = image.height
    output_directory = os.path.join(
        output_directory, f"image_{image_id}_{xvalue}x{yvalue}.{desired_format.lower()}")
    image.save(output_directory, format=desired_format,
               quality=compression_level)


if __name__ == "__main__":
    main()
