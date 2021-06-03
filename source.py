import cv2
import numpy as np
import DB
import matplotlib.pyplot as plt

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

'''
divisions= 16
image= cv.imread("image.jpg")
# print(image)
slicing= sliceImage(image,divisions)
# print(slicing)
'''

def CompareHist(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection




    

def RGB_MEAN(image):
    avg_color_per_row = np.average(image, axis=0)
    #print(avg_color_per_row)
    avg_color = np.average(avg_color_per_row, axis=0) 
    if avg_color[0] > 1 or avg_color[1] > 1  or avg_color[2] > 1 : 
        avg_color /=256
    # print(avg_color)
    return avg_color #BGR Values




def Compare_avg_RGB(avg1, avg2):
    
    return 1-np.sqrt(((avg2[0]-avg1[0])**2)+((avg2[1]-avg1[1])**2)+((avg2[2]-avg1[2])**2))

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



def Histogram(image):
    

    histR, bin_edges = np.histogram(image[:, :, 0], bins=256, range=(0, 256))
    histG, bin_edges = np.histogram(image[:, :, 1], bins=256, range=(0, 256))
    histB, bin_edges = np.histogram(image[:, :, 2], bins=256, range=(0, 256))
        
   
    return histR,histG,histB
    
 
    
'''Adding histogram to image slices '''

def SeveralHistograms(image,divisions):
    image_slices= sliceImage(image, divisions)
    histogram= [] 
    for image in image_slices:
        histogram.append(Histogram(image))
    
    return histogram 


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
   


'''    compare 2 images slices with each other '''
def Compare_SeveralHistograms(hist1,hist2):  ####hist = 16 histograms 
    Similar=[]
    for i in range(len(hist1)):
        Similar[i]=CompareHist(hist1[i], hist2[i])
    return np.sum(Similar)/len(hist1)




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







''' comparing histogram, rgb and several histogram '''
path= 'images/4.jpeg'
path2= 'images/4.jpeg' 
img1= cv2.imread(path)
img2= cv2.imread(path2)

hist1= Histogram(img1)
hist2= Histogram(img2)

avg1 = RGB_MEAN(img1)
avg2 = RGB_MEAN(img2)

similarity_rgb = Compare_avg_RGB(avg1,avg2)
similarity_histogram = CompareHist(hist1, hist2 )









