from PIL import Image
import numpy as np

# Uploading image to work with
ima = Image.open("ascii-pineapple.jpg")
im = ima.resize((round(ima.size[0]*0.25), round(ima.size[1]*0.25)))
print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))


# Converting image's pixel data into an ASCII color-array
pixel_array = np.asarray(im)
bright_arr = []
ascii_str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_str_length = len(ascii_str)
key = 255/(ascii_str_length - 1)


mapping_input = str(input("Choose brightness mapping: (average/luminosity/min_max)"))

for x in range(len(pixel_array)):
    row_array = []
    for y in range(len(pixel_array[x])):
        avg = (sum(pixel_array[x][y]))/3
        min_max = ((min(pixel_array[x][y]) + max(pixel_array[x][y]))/2)
        lumin = (pixel_array[x][y][0] * 0.21) + (pixel_array[x][y][1] * 0.72) + (pixel_array[x][y][2] * 0.07)
        if mapping_input == "average":
            index = min(round(avg/key), (ascii_str_length - 1))
        elif mapping_input == "min_max":
            index = min(round(min_max/key), (ascii_str_length - 1))
        else:
            index = min(round(lumin/key), (ascii_str_length - 1))
        row_array.append(ascii_str[index] * 3) 

    bright_arr.append(row_array)
 
print("RGB: " + str(pixel_array[0][0]) + "R: " + str(pixel_array[0][0][0]) + "G: " + str(pixel_array[0][0][1]) + "B: " + str(pixel_array[0][0][2]))
color_input = str(input("Matrix color? (y/n)" ))

# Printing the ASCII Image in green or default
for i in range(len(bright_arr)):
    for j in range(len(bright_arr[i])):
        if color_input == "y":
            print("\033[32m" + bright_arr[i][j], end = "")
        else:
            print(bright_arr[i][j], end = "")
    print("")
