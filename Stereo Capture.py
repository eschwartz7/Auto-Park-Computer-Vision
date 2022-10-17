import cv2
import numpy as np
import os
import time

# Code to capture and store stereo images from camera

#Specify number of images to capture
n_images = 30
i = 0

#Create directories for images and specify path
pathL = r'C:\Users\elija\PycharmProjects\Senior Design\StereoL'
pathR = r'C:\Users\elija\PycharmProjects\Senior Design\StereoR'

#Start video capture
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


while(i < n_images):
    ret, frame = vid.read()

    #Get height and width of images
    height = frame.shape[0]
    width = frame.shape[1]

    #Stereo frames need to be split into two separate images
    left_img = frame[0:height, 0:int(width/2)]
    right_img = frame[0:height, int(width/2):width]

    #Save images to directories
    filenameL = 'StereoCalibL%d.jpg' % i
    cv2.imwrite(os.path.join(pathL, filenameL), left_img)

    filenameR = 'StereoCalibR%d.jpg' % i
    cv2.imwrite(os.path.join(pathR, filenameR), right_img)

    #Display images
    cv2.imshow('left', left_img)
    cv2.imshow('right', right_img)

    #Wait a few seconds between images
    time.sleep(3)
    i += 1

    #Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()