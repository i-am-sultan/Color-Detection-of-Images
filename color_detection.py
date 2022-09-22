import cv2
import numpy as np
import pandas as pd
import argparse

# Creating argument parser to take image path from command line
# ap = argparse.ArgumentParser()
# ap.add_argument('-i', '--image', required=True, help="Image Path")
# args = vars(ap.parse_args())
# img_path = args['image']
# img = cv2.imread(img_path)


# Initializing image path
def initialize(filepath):
    global pic
    # Reading the image with opencv
    pic = cv2.imread(filepath)
    show_picture()
    main()

# declaring global variables (are used later on)
mclick = False
r = g = b = xpos = ypos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colorhex.csv', names=index, header=None)

# function to calculate minimum distance from all colors and get the most matching color
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# function to get x,y coordinates of mouse double click
def drawFunction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, xpos, ypos, mclick
        mclick = True
        xpos = x
        ypos = y
        b, g, r = pic[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

def show_picture():
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', drawFunction)

def main():
    global mclick
    while (1):
        cv2.imshow("image", pic)
        if (mclick):
            # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
            cv2.rectangle(pic, (20, 20), (750, 60), (b, g, r), -1)
            # Creating text string to display( Color name and RGB values )
            text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
            # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
            cv2.putText(pic, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            # For very light colours we will display text in black colour
            if (r + g + b >= 600):
                cv2.putText(pic, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            mclick = False
            cv2.putText(pic, "press 'esc' key to exit",(50,80),2,0.7,(0,0,0),2,cv2.LINE_AA)
        # Break the loop when user hits 'esc' key    
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
