import cv2
import numpy as np
import DB
import matplotlib.pyplot as plt

def sliceImage(img,divisions):
    # img = cv.imread(Image_path)

    dimensions= img.shape
    print(dimensions)
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

'''
divisions= 16
image= cv.imread("image.jpg")
# print(image)
slicing= sliceImage(image,divisions)
# print(slicing)
'''

# def CompareHist(image1, image2, methodtype="Correlation"):
#     image1_r = cv2.resize(image1, (1024, 540),
#                interpolation = cv2.INTER_NEAREST)
#     image2_r = cv2.resize(image2, (1024, 540),
#                interpolation = cv2.INTER_NEAREST)
# ################# Method1: Using the OpenCV cv2.compareHist function ###################
# # cv2.compareHist(H1, H2, method)

# # The cv2.compareHist function takes three arguments: 
# #     H1, which is the first histogram to be compared, 
# #     H2, the second histogram to be compared, 
# #     and method, which is a flag indicating which comparison method should be performed.

# # initialize OpenCV methods for histogram comparison
#     OPENCV_METHODS = (
#     	("Correlation", cv2.HISTCMP_CORREL),
#     	("Chi-Squared", cv2.HISTCMP_CHISQR),
#     	("Intersection", cv2.HISTCMP_INTERSECT),
#     	("Hellinger", cv2.HISTCMP_BHATTACHARYYA))
    
    
#     # We start by initializing a reverse variable to False.
#     #  This variable handles how sorting the results dictionary will be performed. 
#     #  For some similarity functions a LARGER value indicates higher similarity 
#     #          (Correlation and Intersection).
#     #  And for others, a SMALLER value indicates higher similarity 
#     #          (Chi-Squared and Hellinger).
    
#     # loop over the comparison methods
#     for (methodName, method) in OPENCV_METHODS:
#     	# initialize the results dictionary and the sort
#     	# direction
#     	results = {}
#     	reverse = False
        
#         # if we are using the correlation or intersection
#     	# method, then sort the results in reverse order
#     	if methodName in ("Correlation", "Intersection"):
#     		reverse = True
            
#     if methodtype == "Correlation":
#         d = cv2.compareHist(image1_r, image2_r, OPENCV_METHODS[0][1])
#         #print(d)
#     elif methodtype == "Chi-Squared":
#         d = cv2.compareHist(image1_r, image2_r, OPENCV_METHODS[1][1])
#         #print(d)
#     elif methodtype == "Intersection":        
#         d = cv2.compareHist(image1_r, image2_r, OPENCV_METHODS[2][1])
#         #print(d)
#     elif methodtype == "Hellinger":
#         d = cv2.compareHist(image1_r, image2_r, OPENCV_METHODS[3][1])
#         #print(d)

#     if (methodtype == "Correlation") or (methodtype == "Intersection"):
#         if d > 1000000:
#             print("Similar")
#         else:
#             print("Not Similar")
#     elif (methodtype ==  "Chi-Squared") or (methodtype == "Hellinger"):
#         if d < 100000:
#             print("Similar")
#         else:
#             print("Not Similar")

'''
CompareHist(image1,image2,"Intersection")
'''
def CompareHist (image1,image2):
    histo1=Histogram(image1)
    histo2=Histogram(image2)
    
    #mini=0

    mminima=np.sum(np.minimum(histo1,histo2))
    distance=np.divide(mminima,np.sum(histo2))
    
    #print(distance)
    if distance<0.1:
        return 1
    else:
        return 0
    

def RGB_MEAN(image):
    avg_color_per_row = np.average(image, axis=0)
    #print(avg_color_per_row)
    avg_color = np.average(avg_color_per_row, axis=0) 
    if avg_color[0] > 1 and avg_color[1] > 1  and avg_color[2] > 1 : ##JPEG Format
        avg_color /=256
    #print(avg_color)
    return avg_color #BGR Values


def Compare_avg_RGB(image1, image2):
    avg1=RGB_MEAN(image1)
    #print(avg1)
    avg2=RGB_MEAN(image2)
    #print(avg2)
    if abs(avg2[0]-avg1[0]) < 0.1 and abs(avg2[1]-avg1[1]) < 0.1 and abs(avg2[2]-avg1[2]) < 0.1:
        #print("Similar")
        return 1
    else:
        #print("NOT Similar")
        return 0

#Compare_avg_RGB(image1,image2)

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

'''
video_path = 'videos/Lane Detection.mp4'
threshold = 6
cap = cv2.VideoCapture(video_path)
keyFrames = keyFramesExtracion(cap, threshold)
for keyFrame in keyFrames:
    plt.imshow(cv2.cvtColor(keyFrame, cv2.COLOR_BGR2RGB))
    plt.show()
'''

''''''

def Histogram(image):
    

    histR, bin_edges = np.histogram(image[:, :, 0], bins=256, range=(0, 256))
    histG, bin_edges = np.histogram(image[:, :, 1], bins=256, range=(0, 256))
    histB, bin_edges = np.histogram(image[:, :, 2], bins=256, range=(0, 256))
        
   
    return histR,histG,histB
    

'''extracting features to key frames extracted from videos '''
def keyframesfeatures(cap,threshold):
    keyframes=keyFramesExtracion(cap,threshold)
    avgRGB=[]
    histogram=[]
    layoutHistogram=[]
    for frame in range(keyframes):
        avgRGB[frame]= RGB_MEAN(frame)
        histogram[frame] = Histogram(frame)
        layoutHistogram[frame]= layoutHistogram(frame)
    
    
    
    return[avgRGB,histogram ,layoutHistogram]


'''Adding histogram to image slices '''

def SeveralHistograms(image,divisions):
    image_slices= sliceImage(image, divisions)
    histogram= [] 
    for image in range(image_slices):
        histogram[image]=Histogram(image)
    
    return histogram 


def Similarity_Video(Video_I,Method):           #########Method : 0 for RGB, 1 for Histogram, 2 for Several histograms
    Keyframes_I=keyFramesExtracion(Video_I)
    Similar=[]
    for video in DB.getVideos():    #loop on videos in DB
        Keyframes_M=keyFramesExtracion(video)
        for keyframeM in Keyframes_M:   #loop on keyframes of video inDB
            for keyframeI in Keyframes_I:   #loop on keyframes of input video
                if (Method==0):
                    if(Compare_avg_RGB(keyframeI, keyframeM)):
                        Similar[video]+=1
                elif (Method==1):
                    if(CompareHist(keyframeI, keyframeM)):
                        Similar[video]+=1
                elif (Method==1):
                    if(SeveralHistograms(keyframeI, keyframeM)):
                        Similar[video]+=1
        Similar[video]/=keyframeM 
        
    maxvalue=max(Similar)
    max_index=Similar.index(maxvalue)
    
    
    
    return max_index


