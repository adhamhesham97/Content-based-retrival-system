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
    return abs(1-np.sqrt(((avg2[0]-avg1[0])**2)+((avg2[1]-avg1[1])**2)+((avg2[2]-avg1[2])**2)))


# path= 'images/1_1.png'
# path2= 'images/2_1.png' 
# img1= cv2.imread(path)
# img2= cv2.imread(path2)

# avg1 = RGB_MEAN(img1)
# avg2 = RGB_MEAN(img2)

# similarity_rgb = Compare_avg_RGB(avg1,avg2)