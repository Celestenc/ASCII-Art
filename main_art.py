from PIL import Image
import numpy as np

## 1) Uploading image to work with
im = Image.open("ascii-pineapple.jpg")
print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))


## 3) Converting image's pixel data into a 2D array of colors
pixel_array = np.asarray(im)

bright_arr = []
for i in range(len(pixel_array)):
    row = []
    for j in range(len(pixel_array[i])):
        row.append((sum(pixel_array[i][j]))//3)
    bright_arr.append(row)

print("Iterating through pixel contents:")

# Printing just the tuples from tuple array
for i in range(len(bright_arr)):
    for j in range(len(bright_arr[i])):
        print(bright_arr[i][j])