import cv2
import numpy as np
import DB
import matplotlib.pyplot as plt

def Histogram(image):
    histR, bin_edges = np.histogram(image[:, :, 0], bins=256, range=(0, 256))
    histG, bin_edges = np.histogram(image[:, :, 1], bins=256, range=(0, 256))
    histB, bin_edges = np.histogram(image[:, :, 2], bins=256, range=(0, 256))
    return histB.tolist(),histG.tolist(),histR.tolist()


def CompareHist(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection


# path= 'images/1_1.png'
# path2= 'images/2_1.png' 
# img1= cv2.imread(path)
# img2= cv2.imread(path2)

# hist1= Histogram(img1)
# hist2= Histogram(img2)

# similarity_histogram = CompareHist(hist1, hist2 )
