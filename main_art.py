from PIL import Image
import numpy as np

## 1) Uploading image to work with
im = Image.open("ascii-pineapple.jpg")
# print(im.format, im.size, im.mode)
# im.show()
print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))


## 2) Converting image's pixel data into a 2D array of colors
pixel_array = np.asarray(im)

# Prints the arrays of a 2D array
# for i in range(len(pixel_array)):
#     for j in range(len(pixel_array[i])):
        # print(pixel_array[i][j])

# # Creating and printing a 2D array of tuples
# tup_array = []
# for i in range(len(pixel_array)):
#     row = []
#     for j in range(len(pixel_array[i])):
#         row.append(tuple(pixel_array[i][j]))
#     tup_array.append(row)

# print("Iterating through pixel contents:")

# # Printing just the tuples from tuple array
# for i in range(1):
#     for j in range(len(tup_array[i])):
#         print(tup_array[i][j])

## 3) Converting RGB matrix into a Brightness matrix
# Creating and printing a 2D array of average of colors
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