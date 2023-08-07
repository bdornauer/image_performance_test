import os
import sys

def change_current_image_format(new_format):
    #read files
    file_image_format= open("current_format.txt", "r")
    file_index_html = open("index.html", "r")

    current_format_data = file_image_format.read()
    current_index_html_data = file_index_html.read()

    file_image_format.close()
    file_index_html.close()

    #write
    file_image_format = open("current_format.txt", "w")
    file_index_html = open("index.html", "w")

    file_image_format.write(new_format)
    file_index_html.write(current_index_html_data.replace(current_format_data, new_format))

    file_image_format.close()
    file_index_html.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        change_current_image_format(sys.argv[1])
    else:
        print("Invalid")