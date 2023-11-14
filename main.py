from jpgpng.convert import jpg_to_png, png_to_jpg


if __name__ == "__main__" :
    input_file = 'bg.jpg'
    output_file = 'image.png'
    jpg_to_png(input_file, output_file)
    input_file1 = 'background.png'
    output_file1 = 'image1.jpg'
    png_to_jpg(input_file1, outpout_file1)
