import cv2
import numpy as np
import DB
import matplotlib.pyplot as plt
from histogram import *

def sliceImage(img,divisions):
    # img = cv.imread(Image_path)
    # dimensions= img.shape
    # print(dimensions)

    height = img.shape[0]
    width = img.shape[1]
    x=0
    y=0
    new_height = height/np.sqrt(divisions)
    # print(new_height)
    new_width = width/np.sqrt(divisions)
    # print(new_width)
    new_images=[]
    
    #image cropping 
    i=0
    for i in range(int(np.sqrt(divisions))):
        y=0
        for j in range(int(np.sqrt(divisions))):   
            image= img[ int(y): int(new_height+y), int(x) :int(new_width+x) , : ]
            y= y + new_height 
            # print(image)            
            new_images.append(image)
            # new_image_path = Image_path[0 : 4]  + str(i) + str(j) + '.jpg'
            # cv.imwrite(new_image_path, image)    
        x= x+ new_width
    # image_parts= image_slicer.slice(Image_path, divisions)
    return new_images

'''Adding histogram to image slices '''

def SeveralHistograms(image,divisions):
    image_slices= sliceImage(image, divisions)
    histogram= [] 
    for image in image_slices:
        histogram.append(Histogram(image))
    return histogram 

'''    compare 2 images slices with each other '''
def Compare_SeveralHistograms(hist1,hist2):  ####hist = 16 histograms 
    Similar=0
    for i in range(len(hist1)):
        Similar+=CompareHist(hist1[i], hist2[i])
    return Similar/len(hist1)

# path= 'images/1_1.png'
# path2= 'images/2_1.png' 
# img1= cv2.imread(path)
# img2= cv2.imread(path2)

# SH1=SeveralHistograms(img1,16)
# SH2=SeveralHistograms(img2,16)

# similarity_severalHist=Compare_SeveralHistograms(SH1, SH2)