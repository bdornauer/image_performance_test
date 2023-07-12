from PIL import Image
import os


input_directory = "uncoverted"
output_directory = "converted"
set_of_formats = ["PNG", "JPEG", "WEBP", "TIFF"]
scaling_factors = [0.1,0.25, 0.5, 0.75, 1.0]
compression_level = 50


def main():
    # go through each image in the folder converted
    # it to a jpg and save it in the folder unconverted
    for file in os.listdir(input_directory):
        filename = os.path.splitext(file)[0]
        file_type = os.path.splitext(file)[1]

        input_path = os.path.join(input_directory, file)
        for scaling_factor in scaling_factors:
            new_filname = f"{filename}_factor_{scaling_factor}x"
            for desired_format in set_of_formats:
                output_path = os.path.join(
                    output_directory, f"{new_filname}.{desired_format.lower()}")
                convert_image(input_path, output_path,
                              desired_format, scaling_factor)


def convert_image(input_path, output_path, format, scaling_factor):
    image = Image.open(input_path)
    image = image.resize(
        (round(image.size[0]*scaling_factor), round(image.size[1]*scaling_factor)))
    image.save(output_path, format=format, quality=compression_level)


if __name__ == "__main__":
    main()
