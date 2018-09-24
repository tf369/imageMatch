# _*_ coding=utf-8 _*_
__date__ = '9/24/2018 13:28 '

import cv2
import time
import os
import numpy as np


def getColorVec(img):
    hei, width, channel=img.shape
    colorVec=[0 for e in range(0, 125)]
    i=0
    while(i<hei):
        j=0
        while(j<width):
            pixel=img[i][j]
            grade=getPixelGrade(pixel)
            index=grade[0]*5*5+grade[1]*5+grade[2]
            colorVec[index]+=1
            j+=1
        i+=1
    return colorVec


def getPixelGrade(pixel):
    grade=[]
    base=int(256/5)+1
    for one in np.array(pixel):
        grade.append(int(one/base))
    return grade


#logger = logging.getLogger(__name__)
#logger.setLevel(level=logging.INFO)
#handler = logging.FileHandler('output.log')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)

