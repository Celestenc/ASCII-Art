from PIL import Image
import numpy as np

# Uploading image to work with
ima = Image.open("mickey.jpeg")
im = ima.resize((round(ima.size[0]*0.125), round(ima.size[1]*0.125)))
print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))


# Converting image's pixel data into an ASCII color-array
pixel_array = np.asarray(im)
bright_arr = []
ascii_str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_str_length = len(ascii_str)
key = 255/(ascii_str_length - 1)

print("Length of ascii_str:", ascii_str_length)
for x in range(len(pixel_array)):
    row_array = []
    for y in range(len(pixel_array[x])):
        avg = (sum(pixel_array[x][y]))/3
        index = round(avg/key)
        index = min(index, (ascii_str_length - 1))
        row_array.append(ascii_str[index] * 3) 
    bright_arr.append(row_array)
 
color_input = str(input("Matrix color? (y/n)" ))

green = False
if color_input == "y":
    green = True

# Printing the ASCII Image in green or default
for i in range(len(bright_arr)):
    for j in range(len(bright_arr[i])):
        if green:
            print("\033[32m" + bright_arr[i][j], end = "")
        else:
            print(bright_arr[i][j], end = "")
    print("")

