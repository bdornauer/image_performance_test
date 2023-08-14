from PIL import Image
import pillow_avif
import os
from tqdm import tqdm

input_directory = "unconverted"
output_directory = "converted"
set_of_formats = ["PNG", "JPEG", "WEBP", "TIFF", "AVIF"]
image_width_height = [[1280, 720], [640, 360], [320, 180], [320, 180], [300, 225], [300, 225], [240, 180], [240, 180],
                      [240, 180], [1, 1], [32, 32], [64, 64], [150, 150], [150, 150], [200, 200], [225, 300],
                      [180, 240]]  # [width, height]


def main():
    id = 0
    dir = os.listdir(input_directory)
    progress_bar = tqdm(total=len(dir))

    for file in dir:
        filename = os.path.splitext(file)[0]
        file_type = os.path.splitext(file)[1]
        id += 1
        input_path = os.path.join(input_directory, file)
        for image in image_width_height:
            for desired_format in set_of_formats:
                convert_image(input_path, output_directory, id,
                              desired_format, image[0], image[1])
        progress_bar.update(1)


def convert_image(input_path, output_directory, image_id, desired_format, width, height):
    image = Image.open(input_path)

    image = image.resize((width, height))
    output_directory = os.path.join(
        output_directory, f"image_{image_id}_{width}x{height}.{desired_format.lower()}")
    image.save(output_directory, format=desired_format)

if __name__ == "__main__":
    main()
