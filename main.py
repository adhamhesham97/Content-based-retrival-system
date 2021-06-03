import cv2
import numpy as np
import DB
import matplotlib.pyplot as plt
from histogram import *
from avgRGB import *
from severalHist import *


def keyFramesExtracion(cap, threshold):
    if (cap.isOpened()== False):
       print("Error opening video file")
       return
    
    keyFrames=[]
    numOfFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
    numOfPixels = width*height
    for i in range(numOfFrames):
            ret, curr_frame = cap.read()
            curr_grey_frame = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
            if(i==0):
                prev_grey_frame = curr_grey_frame
                keyFrames.append(curr_frame)
            
            diff = cv2.absdiff(prev_grey_frame, curr_grey_frame)
            # non_zero_count = np.count_nonzero(diff)
            if np.sum(diff)/numOfPixels > threshold:
                keyFrames.append(curr_frame)
                # print('diff',np.sum(diff)/numOfPixels)
                # print(non_zero_count/numOfPixels)
                # print ("Got P-Frame")
                # plt.imshow(cv2.cvtColor(curr_frame, cv2.COLOR_BGR2RGB))
                # plt.show()
            prev_grey_frame = curr_grey_frame   
    return keyFrames

'''
video_path = 'videos/Lane Detection.mp4'
threshold = 6
cap = cv2.VideoCapture(video_path)
keyFrames = keyFramesExtracion(cap, threshold)
for keyFrame in keyFrames:
    plt.imshow(cv2.cvtColor(keyFrame, cv2.COLOR_BGR2RGB))
    plt.show()
'''

'''extracting features to key frames extracted from videos '''
def keyframesfeatures(keyframes):
    avgRGB=[]
    Histograms=[]
    layoutHistogram=[]
    for frame in keyframes:
        
        avgRGB.append(RGB_MEAN(frame))
   
        Histograms.append(Histogram(frame))
      
        layoutHistogram.append(SeveralHistograms(frame,16))
        # print(len(SeveralHistograms(frame,16)))
    return avgRGB, Histograms ,layoutHistogram

''''
testing 
'''
'''
video_path = 'videos/acrobacia.mp4'
threshold = 6
cap = cv2.VideoCapture(video_path)
keyFrames = keyFramesExtracion(cap, threshold)
# print(len(keyFrames))
avgrgb, histogram, layoutHistogram= keyframesfeatures(keyFrames)

# print("layout histogram", layoutHistogram)
print(layoutHistogram[0][0]) 

'''

def Similarity_Video(Method,VideoFeatures1,VideoFeatures2): #######Video_L[ [avgRGB,histogram,layoutHistorgam],
                                                         #  [avgRGB,histogram,layoutHistorgam],....] 
    #metric=[]
    if(len(VideoFeatures1[0])< len(VideoFeatures2[0])):
        video1=VideoFeatures1
        video2=VideoFeatures2
    else :
        video1=VideoFeatures2
        video2=VideoFeatures1
    
    Bool= [False] * len(video2[0])
    metric = [0] * len(video1[0]) 
    m=[0] * len(video2[0])
    
    for i in range(len(video1[0])):
        
        for j in range(len(video2[0])):
            if(Bool[j])==False:
                if (Method==0):
                    m[j]=Compare_avg_RGB(video1[0][i], video2[0][j])
                elif(Method==1):
                    m[j]=CompareHist(video1[1][i],video2[1][j])
                elif(Method==2):
                    m[j]=Compare_SeveralHistograms(video1[2][i],video2[2][j])
            else:
                continue    
        maxvalue=max(m)
    
        max_index=m.index(maxvalue)
        Bool[max_index]=True
        metric[i]=maxvalue
        m=[0] * len(video2[0])
   
    return np.divide(np.sum(metric),len(metric))
    


'''TTTTTTTTTTTTTTTTTTTTTTTESTINGGGGGGGGGGGGGGGGGGGGGGGGGG'''
# v1=[]
# v2=[]
# video_path = 'videos/acrobacia.mp4'
# threshold = 6
# cap = cv2.VideoCapture(video_path)
# keyFrames = keyFramesExtracion(cap, threshold)  
# avgrgb, histogram, layoutHistogram= keyframesfeatures(keyFrames)
# v1.append(avgrgb)
# v1.append(histogram)
# v1.append(layoutHistogram)

# video_path = 'videos/acrobacia.mp4'
# threshold = 6
# cap = cv2.VideoCapture(video_path)
# keyFrames = keyFramesExtracion(cap, threshold)  
# avgrgb, histogram, layoutHistogram= keyframesfeatures(keyFrames)

# v2.append(avgrgb)
# v2.append(histogram)
# v2.append(layoutHistogram)

# # m= [0]* len(v1)

# similarity =Similarity_Video(0,v1,v2)




















