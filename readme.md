# AsciiFun
## image -> ascii
#### How to run:
```
python asciiImage.py <image_name>
```

#### How the algorithm works:
- find image
- divides the image width by 20
- divides the image height by 40
- resizes image
- turn image to greyscale
- calculate the amount you need to divide the pixel brightness by with
    1. do 255 divide by the number of ascii characters you have -1 (because it is acounting for the array starting at zero so the max number is one less than the length of the array)
    2. in this case 255/10 (255/(11-1)) = 25
- integer divide the brightness of each pixel by the number calculated in the previous step. This is the index of the corrosponding ascii character to the brightness in the list
- write that ascii char to a long array
- add all the characters together into one string and add enters (`\n`) every time you reach the width of the image. for example if the new ascii image had a width of 100. add an enter every 100 characters so the image is not just one long line but a image with height
- save to a txt file

## ascii video
#### How to run:
```
python asciivideo.py
```

#### How the algorithm works:
- use cv2 to get webcam image
- save to a file
- use the same process as in [the image to ascii algorithm](#how-the-algorithm-works) to turn the image into ascii
- print the ascii
- repeat proccess until keyboard interupt.