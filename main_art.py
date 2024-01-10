from PIL import Image
import numpy as np

## 1) Uploading image to work with
im = Image.open("ascii-pineapple.jpg")
# print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))


## 4) Converting image's pixel data into an ASCII color-array + printing

pixel_array = np.asarray(im)

bright_arr = []
key = 255/65
ascii_str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_str_length = len(ascii_str)
print("Length of ascii_str:", ascii_str_length) 
for i in range(len(pixel_array)):
    row = []
    for j in range(len(pixel_array[i])):
        avg = (sum(pixel_array[i][j]))/3
        index = round(avg/key)
        index = min(index, 64)
        row.append(ascii_str[index])
    bright_arr.append(row)

print("Iterating through pixel contents:")

# Printing just the tuples from tuple array
for i in range(len(bright_arr)):
    for j in range(len(bright_arr[i])):
        print(bright_arr[i][j])
