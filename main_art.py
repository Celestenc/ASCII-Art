from PIL import Image
import numpy as np

## 1) Uploading image to work with
ima = Image.open("ascii-pineapple.jpg")
im = ima.resize((round(ima.size[0]*0.5), round(ima.size[1]*0.5)))
print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))


## 4) Converting image's pixel data into an ASCII color-array + printing
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
 

## 5 Printing the ASCII Image!
for i in range(len(bright_arr)):
    for j in range(len(bright_arr[i])):
        print(bright_arr[i][j], end = "")
    print("")
