import os
import sys
import glob
import time
import json
import numpy as np
from scipy import io
import matplotlib.pyplot as plt
import cv2
from StereoCalib import stereoRectification

def disparityMap(imgL, imgR):

    left = cv2.imread(imgL)
    right = cv2.imread(imgR)
    left_gray = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

    stereo = cv2.StereoBM_create(numDisparities=32, blockSize=11)
    disparity = stereo.compute(left_gray, right_gray)
    plt.imshow(disparity)
    plt.show()

disparityMap("000009_11.png", "000009_10.png")

def getDepthImages(imgL, imgR):

    #Code to generate depth map given two stereo images

    f = open('stereocalibdata.json',)
    stereo_data = json.load(f)

    [mtxL, distL, mtxR, distR, Rot, Trns, Emat, rect_l, rect_r, proj_l, proj_r] = stereo_data.values()

    mtxL = np.asarray(mtxL, dtype=np.float32)
    distL = np.asarray(distL, dtype=np.float32)
    mtxR = np.asarray(mtxR, dtype=np.float32)
    distR = np.asarray(distR, dtype=np.float32)
    Rot = np.asarray(Rot, dtype=np.float32)
    Trns = np.asarray(Trns, dtype=np.float32)
    Emat = np.asarray(Emat, dtype=np.float32)
    rect_l = np.asarray(rect_l, dtype=np.float32)
    rect_r = np.asarray(rect_r, dtype=np.float32)
    proj_l = np.asarray(proj_l, dtype=np.float32)
    proj_r = np.asarray(proj_r, dtype=np.float32)

    rect_L, rect_R = stereoRectification(imgL, imgR, mtxL, distL, mtxR, distR, rect_l, rect_r, proj_l, proj_r)

    disparityMap(rect_L, rect_R)


#getDepthImages('TestL/TestL3.jpg', 'TestR/TestR3.jpg')