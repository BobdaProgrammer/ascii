import sys
from PIL import Image

def resize_img(image):
    resized_img = image.resize((NEW_WIDTH,NEW_HEIGHT)) 
    return resized_img

def grey(img):
    return img.convert("L")

def ascii(img):
    pixels = img.getdata()
    chars = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return chars

img = Image.open(sys.argv[1])
ASCII_CHARS=["@","#","$","%", "?", "*","+",";",":",",","."]
NEW_WIDTH=img.size[0]//20
NEW_HEIGHT=img.size[1]//40
chars = ascii(grey(resize_img(img)))
pixelCount = len(chars)
final = "\n".join([chars[i:i+NEW_WIDTH] for i in range(0,pixelCount, NEW_WIDTH) ])
file = open(sys.argv[1].split(".")[0]+".txt", "w")
file.write(final)