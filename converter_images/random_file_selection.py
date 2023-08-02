import os
import random
import shutil


def random_image_selection(source, dest, number):
    files = os.listdir(source)
    random_files = random.sample(files, number)
    # Copy the randomly selected files to the destination directory
    for file in random_files:
        shutil.copy(os.path.join(source, file), dest)
    # and give a new file name which is a counter starting from 1
    for i, file in enumerate(os.listdir(dest)):
        os.rename(os.path.join(dest, file), os.path.join(
            dest, "img_"+str(i+1)+".jpg"))


if __name__ == "__main__":
    random_image_selection("./1024x768", "./unconverted", 1000)
