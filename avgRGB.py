import cv2
import numpy as np
import DB
import matplotlib.pyplot as plt


def RGB_MEAN(image):
    avg_color_per_row = np.average(image, axis=0)
    #print(avg_color_per_row)
    avg_color = np.average(avg_color_per_row, axis=0) 
    if avg_color[0] > 1 or avg_color[1] > 1  or avg_color[2] > 1 : 
        avg_color /=256
    # print(avg_color)
    return avg_color #BGR Values


def Compare_avg_RGB(avg1, avg2):
    return 1-((abs(avg1[0]-avg2[0])+abs(avg1[1]-avg2[1])+abs(avg1[2]-avg2[2]))/765) ##### 1 is similar


# path= 'images/4.jpeg'
# path2= 'images/5.jpeg' 
# img1= cv2.imread(path)
# img2= cv2.imread(path2)

# avg1 = RGB_MEAN(img1)
# avg2 = RGB_MEAN(img2)


# similarity_rgb = Compare_avg_RGB((0,252,0),(0,0,0))
# print(similarity_rgb)