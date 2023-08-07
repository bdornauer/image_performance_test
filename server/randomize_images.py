import os
import random

image_formats = ["PNG", "JPEG", "WEBP", "TIFF", "AVIF"]
image_header_size = [1280, 720]

image_width_height = [[640, 360], [320, 180], [320, 180], [300, 225], [300, 225], [240, 180], [240, 180],
                      [240, 180], [150, 150], [150, 150], [200, 200], [225, 300], [180, 240]]  # [width, height]
image_footer_logo_sizes = [[1, 1], [32, 32], [64, 64]]


def randomize_images(image_format):
    os.system("rm assets/images/*")
    with open("template.html", "r") as file:
        data = file.read()
        random.shuffle(image_width_height)
        random.shuffle(image_footer_logo_sizes)
        image_counter = 1

        # Header
        data = replace_tag_with_image_tag(image_header_size, data, image_counter, image_format)
        image_counter += 1

        # Body
        for size in image_width_height:
            data = replace_tag_with_image_tag(size, data, image_counter,image_format)
            image_counter += 1

        # Footer
        for size in image_footer_logo_sizes:
            data = replace_tag_with_image_tag(size, data, image_counter,image_format)
            image_counter += 1

    with open("index.html", "w") as file:
        file.write(data)


def replace_tag_with_image_tag(size, data, image_number, image_format):
    image_to_replace = f"<!-- Image {image_number} -->"
    random_image_selected = select_random_image(size[0], size[1], image_format)
    replace_text = create_image_file_tag(size[0], size[1], random_image_selected, "A short descrition of the image")
    data = data.replace(image_to_replace, replace_text)
    return data


def select_random_image(width, height, image_format):
    image_name = f"image_{random.randint(1, 1000)}_{width}x{height}.{image_format.lower()}"
    #copy images from folder converted to assets folder
    os.system(f"cp converted/{image_name} assets/images/{image_name}")
    return image_name


def create_image_file_tag(width, height, image_name, alt_text):
    image_file_tag = f'<img src="/assets/images/{image_name}" alt="{alt_text}" width="{width}" height="{height}">'
    return image_file_tag


if __name__ == '__main__':
    randomize_images("PNG")
    print("Done")
