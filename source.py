import cv2
import numpy as np
import matplotlib.pyplot as plt

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
            
    
    '''
    for i in range(numOfFrames):
            ret, curr_frame = cap.read()
            curr_grey_frame = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
            if(i==0):
                prev_grey_frame = curr_grey_frame
                keyFrames.append(curr_frame)
            
            diff = cv2.absdiff(prev_grey_frame, curr_grey_frame)
            non_zero_count = np.count_nonzero(diff)
            if non_zero_count/numOfPixels > threshold:
                keyFrames.append(curr_frame)
                print('diff',np.sum(diff)/numOfPixels)
                print(non_zero_count/numOfPixels)
                print ("Got P-Frame")
                plt.imshow(cv2.cvtColor(curr_frame, cv2.COLOR_BGR2RGB))
                plt.show()
            prev_grey_frame = curr_grey_frame
            
    
    
    for i in range(numOfFrames):
            ret, curr_frame = cap.read()
            
            if(i==0):
                prev_frame = curr_frame
                keyFrames.append(curr_frame)
            
            diff = cv2.absdiff(curr_frame, prev_frame)
            non_zero_count = np.count_nonzero(diff)
            if non_zero_count/numOfPixels > threshold:
                keyFrames.append(curr_frame)
                print(non_zero_count/numOfPixels)
                print ("Got P-Frame")
                plt.imshow(curr_frame)
                plt.show()
            prev_frame = curr_frame
    '''
   
    return keyFrames

video_path = 'videos/Lane Detection.mp4'
threshold = 6
cap = cv2.VideoCapture(video_path)
keyFrames = keyFramesExtracion(cap, threshold)
for keyFrame in keyFrames:
    plt.imshow(cv2.cvtColor(keyFrame, cv2.COLOR_BGR2RGB))
    plt.show()
