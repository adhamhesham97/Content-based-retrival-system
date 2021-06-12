from tkinter import *
from tkinter import ttk,Label,Button,Entry,NW,Tk
from tkinter import filedialog
from tkvideo import tkvideo
from PIL import ImageTk, Image
from DB import *
#from source import *
from main import *
import os
import numpy as np
import cv2 as cv
# from histogram import *
# from avgRGB import *
# from SeveralHist import *


# buildDB()

def Build_DB (videos_path,images_path):
    #con = sl.connect('myDB.db')
    #buildDB()
    #deleteDB()
    clearDB()
    for filename in os.listdir(images_path):
        img=cv.imread(os.path.join(images_path,filename))
        insertImage(filename,RGB_MEAN(img),Histogram(img),SeveralHistograms(img,16))
    for filename in os.listdir(videos_path):
        video=cv.VideoCapture(os.path.join(videos_path,filename))
        KF=keyFramesExtracion(video,6)
        RGB,Hist,LayoutHist=keyframesfeatures(KF)
        insertvideo(filename,RGB,Hist,LayoutHist)
       
    # lst=getImages()
    # print(lst)
    return



def BuildButton ():
    Build_DB('videos','images')
    
    return












window=Tk()
window.title('Content based multimedia retrival')
window.geometry("1000x500+150+150")
window.columnconfigure(0,weight=2)
window.configure(bg='#1f666b')
ent1=Entry(window,font=40,width=60,bd=4)
ent1.place(anchor=NW)  
ent1.grid(pady=10)
                      
def browseFiles():
    filename = filedialog.askopenfilename(
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("PNG files","*.png*")
                                                       ))
    ent1.insert(0,filename)
def ShowImage():
    Method=combobox.get()                    
    Type=combobox1.get()
    # if (Method=="CBVR"):
    #     ############################Function of CBVR to return video path##########
    #     video_path="acrobacia.mp4" 
    #     IP_img=Label(window)
    #     IP_img.place(x=2,y=200)
    #     player=tkvideo(ent1.get(),IP_img,loop=1,size=(768,432))
    #     player.play()
        

    #     IPimg_L=Label(window,text="Input Video",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
    #     IPimg_L.place(x=20,y=160)
    
    #     R_img=Label(window)
    #     R_img.place(x=470,y=200)
    #     player=tkvideo(video_path,R_img,loop=1,size=(768,432))
    #     player.play()

    #     R_img_L=Label(window,text="Retieved Video",bg='#1f666b',height=1,width=12,bd=6,font='Helvetica 11 bold')
    #     R_img_L.place(x=520,y=160)
    
    # else:
    if(Type=="Image"):
        w=400
        h=350
        photo=ImageTk.PhotoImage(Image.open(ent1.get()).resize((w, h), Image. ANTIALIAS))
        IP_img=Label(window)
        IP_img.config(image=photo)
        IP_img.image=photo
        IP_img.place(x=2,y=200)
        
        IPimg_L=Label(window,text="Input Image",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
        IPimg_L.place(x=20,y=160)
        img = cv.imread(ent1.get())
        images = getImages()
        max_similarity = 0
        if(Method=="Average RGB"):
            ############################Function of Average RGB to return image path##########
            avgRGB = RGB_MEAN(img) ####
            for image in images:
                similarity = Compare_avg_RGB(avgRGB, image[2])
                if(similarity > max_similarity):
                    max_similarity = similarity
                    image_index = image[0]
                    image_path = image[1]
                
            # image_path='image2.jpg'
        elif(Method=="Histogram"):
            ############################Function of Histogram to return image path##########
            #image_path='image3.jpg'
            
            Histogram1 = Histogram(img) ####
            for image in images:
                similarity = CompareHist(Histogram1, image[3])
                if(similarity > max_similarity):
                    max_similarity = similarity
                    image_index = image[0]
                    image_path = image[1]
        elif(Method=="Several Histograms"):
            ############################Function of Histogram to return image path##########
            #image_path='image4.jpg'
           
              L_H= SeveralHistograms(img,16) ####
              for image in images:
                similarity = Compare_SeveralHistograms(L_H, image[4])
                if(similarity > max_similarity):
                    max_similarity = similarity
                    image_index = image[0]
                    image_path = image[1]
                #print(image_path)

        if(image_path == '0'): #video not image
            video_Path = getKeyFrameVideo(image_index)
            print(video_Path)
            IPimg_L=Label(window,text="Input Image",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
            IPimg_L.place(x=20,y=160)
        
            R_img=Label(window)
            R_img.place(x=470,y=200)
            player=tkvideo('videos/'+video_Path, R_img, loop=1, size=(768,432))
            player.play()
    
            R_img_L=Label(window,text="Retieved Video",bg='#1f666b',height=1,width=12,bd=6,font='Helvetica 11 bold')
            R_img_L.place(x=520,y=160)
        else:
            #print(image_path)
            # w=450
            # h=350
            photo1=ImageTk.PhotoImage(Image.open('images/'+image_path).resize((w, h), Image. ANTIALIAS))    
            R_img=Label(window)
            R_img.config(image=photo1)
            R_img.image=photo1
            R_img.place(x=400,y=200)
            
            R_img_L=Label(window,text="Retieved Image",bg='#1f666b',height=1,width=12,bd=6,font='Helvetica 11 bold')
            R_img_L.place(x=450,y=160)
    
    
    elif(Type=="Video"):
        ###########################Function of CBVR to return video path##########
        video_path=ent1.get()
        IP_img=Label(window)
        IP_img.place(x=2,y=200)
        w=400
        h=350
        player=tkvideo(ent1.get(),IP_img,loop=1,size=(w,h))
        player.play()
        cap = cv.VideoCapture(video_path)
        keyframes = keyFramesExtracion(cap, 6)
        inputVideoFeatures = keyframesfeatures(keyframes)
        videos = getVideos()
        max_similarity = 0
        if(Method=="Average RGB"):
            ############################Function of Average RGB to return video path##########
            #image_path='image2.jpg'
            # video_path='videos/video1.mp4'
            method=0
            
        elif(Method=="Histogram"):
            ############################Function of Histogram to return video path##########
            #image_path='image3.jpg'
            # video_path='videos/video1.mp4'
            method=1
            
        elif(Method=="Several Histograms"):
            ############################Function of Histogram to return video path##########
            #image_path='image4.jpg'
            # video_path='videos/video1.mp4'
            method=2
        
        for video in videos:
            # DBvideoFeatures=[]
            rgb=[]
            hist=[]
            hist16=[]
            for keyFrame in video[2]:
                rgb.append(keyFrame[2])
                hist.append(keyFrame[3])
                hist16.append(keyFrame[4])
            
            DBvideoFeatures=(rgb, hist, hist16)
            similarity = Similarity_Video(method, DBvideoFeatures, inputVideoFeatures)
            
            if(similarity > max_similarity):
                max_similarity = similarity
                video_index = video[0]
                output_video_path = video[1]
                
                
        IPimg_L=Label(window,text="Input Video",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
        IPimg_L.place(x=20,y=160)
    
        R_img=Label(window)
        R_img.place(x=470,y=200)
        player=tkvideo('videos/'+output_video_path, R_img, loop=1, size=(w,h))
        player.play()

        R_img_L=Label(window,text="Retieved Video",bg='#1f666b',height=1,width=12,bd=6,font='Helvetica 11 bold')
        R_img_L.place(x=520,y=160)

    



    

Font_tuple = ("Comic Sans MS", 9,"bold")

Build_B=Button(window,text="Build DB",bd=4,cursor='hand2',font=Font_tuple,command=BuildButton)
Build_B.grid(row=3,column=0,pady=30)


Browse_B= Button(window,text = "Browse Files",
                        command = browseFiles,bd=4,cursor='hand2',font=Font_tuple) 
Browse_B.grid(row=0,column=5,pady=30)


Submit_B=Button(window,text="Submit",bd=4,command=ShowImage,cursor='hand2',font=Font_tuple)
Submit_B.grid(row=3,column=2,pady=10)

Exit_B=Button(window,text="Exit",bd=4,command=window.destroy,cursor='hand2',font=Font_tuple)
Exit_B.grid(row=3,column=5,pady=10)

Choose_L=Label(window,text="Choose the multimedia type: ",bg='#1f666b',font='Helvetica 11 bold').place(x=5,y=5)

Choose_L=Label(window,text="Choose the retrival method: ",bg='#1f666b',font='Helvetica 11 bold').place(x=600,y=5)

        
combobox=ttk.Combobox(window,font='Helvetica 11')
combobox['values']=('Average RGB','Histogram','Several Histograms')
combobox.place(x=805,y=5)
combobox.current(0)

combobox1=ttk.Combobox(window,font='Helvetica 11',width=10)
combobox1['values']=('Image','Video')
combobox1.place(x=210,y=5)
combobox1.current(0)



window.mainloop()
