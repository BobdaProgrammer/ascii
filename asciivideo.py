from PIL import Image
import cv2
import os
def resize_img(image):
    resized_img = image.resize((NEW_WIDTH,NEW_HEIGHT)) 
    return resized_img

def grey(img):
    return img.convert("L")

def ascii(img):
    pixels = img.getdata()
    chars = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return chars

cam_port = 0
cam = cv2.VideoCapture(cam_port) 
try:
    while True:
        
        result, image = cam.read()
        cv2.imwrite("cam.png", image)
        if result:
            img = Image.open("cam.png")
            ASCII_CHARS=["@","#","S","%", "?", "*","+",";",":",",","."]
            NEW_WIDTH=img.size[0]//4
            NEW_HEIGHT=img.size[1]//10
            img = resize_img(img)
            img = grey(img)
            chars = ascii(img)
            pixelCount = len(chars)
            final = "\n".join([chars[i:i+NEW_WIDTH] for i in range(0,pixelCount, NEW_WIDTH) ])
            print(final)
except KeyboardInterrupt:
    os.remove("cam.png")