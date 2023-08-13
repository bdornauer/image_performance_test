from SSIM_PIL import compare_ssim
from PIL import Image
import pillow_avif


def ssim(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Compare images using OpenCL by default
    value = compare_ssim(image1, image2)
    print(value)


if __name__ == '__main__':
    ssim("./converted/image_2_1280x720.png",
         "./converted/image_2_1280x720.avif")
