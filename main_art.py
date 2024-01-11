from PIL import Image
import numpy as np

# Uploading image to work with
ima = Image.open("mickey.jpeg")
im = ima.resize((round(ima.size[0]*0.0625), round(ima.size[1]*0.0625)))
print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))


# Converting image's pixel data into an ASCII color-array
pixel_array = np.asarray(im)
bright_arr = []
ascii_str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_str_length = len(ascii_str)
key = 255/(ascii_str_length - 1)


mapping_input = str(input("Choose brightness mapping: (average/luminosity/min_max): "))

invert_input = str(input("Invert? (y/n)" ))

# Populating array with filtered RGB values
for x in range(len(pixel_array)):
    row_array = []
    for y in range(len(pixel_array[x])):

        # Handling filters
        if mapping_input == "average":
            avg = (sum(pixel_array[x][y]))/3
            index = min(round(avg/key), (ascii_str_length - 1))
        elif mapping_input == "min_max":
            min_max = ((min(pixel_array[x][y].astype(int)) + max(pixel_array[x][y].astype(int)))/2)
            index = min(round(min_max/key), (ascii_str_length - 1))
        else:
            lumin = (pixel_array[x][y][0] * 0.21) + (pixel_array[x][y][1] * 0.72) + (pixel_array[x][y][2] * 0.07)
            index = min(round(lumin/key), (ascii_str_length - 1))

        # Handling Inversion
        if invert_input == "y":
            index = ascii_str_length - 1 - index

        row_array.append(ascii_str[index] * 3) 

    bright_arr.append(row_array)
 

color_input = str(input("Matrix color? (y/n)" ))

# Printing the ASCII Image in green or default
for i in range(len(bright_arr)):
    for j in range(len(bright_arr[i])):
        if color_input == "y":
            print("\033[32m" + bright_arr[i][j], end = "")
        else:
            print(bright_arr[i][j], end = "")
    print("")
