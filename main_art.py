from PIL import Image

# Uploading image to work with
im = Image.open("ascii-pineapple.jpg")
# print(im.format, im.size, im.mode)
# im.show()
print("Successfully loaded image!\n" + "Image size: " + str(im.size[0]) +  " x " + str(im.size[1]))