from PIL import Image
import pillow_avif
import os
from tqdm import tqdm

# compare ssim
from SSIM_PIL import compare_ssim
from PIL import Image


input_directory = "unconverted"
output_directory = "converted"
set_of_formats = ["PNG", "JPEG", "WEBP", "AVIF"]
image_width_height = [[1280, 720], [640, 360], [320, 180], [320, 180], [300, 225], [300, 225], [240, 180], [240, 180],
                      [240, 180], [1, 1], [32, 32], [64, 64], [
                          150, 150], [150, 150], [200, 200], [225, 300],
                      [180, 240]]  # [width, height]


def ssim(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Compare images using OpenCL by default
    value = compare_ssim(image1, image2)
    return value


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


def convert_image(input_path, directory, image_id, desired_format, new_width, new_height):
    image = Image.open(input_path)

    # crop image if width or height is smaller than new_width or new_height in the cente
    image_new = image.resize((new_width, new_height))

    # save image to compare
    image_to_compare_path = os.path.join(
        directory, f"image_{image_id}_{new_width}x{new_height}.png")
    output_directory = os.path.join(
        directory, f"image_{image_id}_{new_width}x{new_height}.{desired_format.lower()}")

    if desired_format == "PNG" or new_width == 1 or new_height == 1:
        image_new.save(output_directory, format=desired_format, optimize=True)
    else:
        quality = 100
        while True:
            try:
                print("Quality: ", quality, " SSIM: ", ssim_value, "Path", output_directory)
                image_new.save(output_directory,
                           format=desired_format, quality=quality)
            except:
                image_new.save(output_directory,
                           format=desired_format)
            ssim_value = ssim(image_to_compare_path, output_directory)
            if ssim_value < 0.95 or quality == 1:
                break
            else:
                quality -= 1

# renname all files with image_number to image_number.png in folder converted
def rename_files():
    dir = os.listdir("unconverted")
    counter = 1
    for file in dir:
        filename = os.path.splitext(file)[0]
        file_type = os.path.splitext(file)[1]
        os.rename(os.path.join("unconverted", file), os.path.join("unconverted", "image_" + "_" + str(counter) +file_type))
        counter += 1



if __name__ == "__main__":
    #rename_files()
    main()
