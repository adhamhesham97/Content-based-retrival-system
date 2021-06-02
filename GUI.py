from tkinter import *
from tkinter import ttk,Label,Button,Entry,NW,Tk
from tkinter import filedialog
from tkvideo import tkvideo
from PIL import ImageTk, Image


window=Tk()
window.title('Content based multimedia retrival')
window.geometry("700x500+150+150")
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
    
    if (Method=="CBVR"):
        ############################Function of CBVR to return video path##########
        video_path="acrobacia.mp4" 
        IP_img=Label(window)
        IP_img.place(x=2,y=200)
        player=tkvideo(ent1.get(),IP_img,loop=1,size=(768,432))
        player.play()
        

        IPimg_L=Label(window,text="Input Video",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
        IPimg_L.place(x=20,y=160)
    
        R_img=Label(window)
        R_img.place(x=470,y=200)
        player=tkvideo(video_path,R_img,loop=1,size=(768,432))
        player.play()

        R_img_L=Label(window,text="Retieved Video",bg='#1f666b',height=1,width=12,bd=6,font='Helvetica 11 bold')
        R_img_L.place(x=520,y=160)
    
    else:
        photo=ImageTk.PhotoImage(Image.open(ent1.get()))
        IP_img=Label(window)
        IP_img.config(image=photo)
        IP_img.image=photo
        IP_img.place(x=2,y=200)
        
        IPimg_L=Label(window,text="Input Image",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
        IPimg_L.place(x=20,y=160)
        if(Method=="Average RGB"):
            ############################Function of Average RGB to return image path##########
            image_path='image2.jpg'
        elif(Method=="Histogram"):
            ############################Function of Histogram to return image path##########
            image_path='image3.jpg'
        elif(Method=="Several Histograms"):
            ############################Function of Histogram to return image path##########
            image_path='image4.jpg'
        
    
        photo1=ImageTk.PhotoImage(Image.open(image_path))    
        R_img=Label(window)
        R_img.config(image=photo1)
        R_img.image=photo1
        R_img.place(x=400,y=200)
        
        R_img_L=Label(window,text="Retieved Image",bg='#1f666b',height=1,width=12,bd=6,font='Helvetica 11 bold')
        R_img_L.place(x=450,y=160)
    

    

    
Font_tuple = ("Comic Sans MS", 9,"bold")

Browse_B= Button(window,text = "Browse Files",
                        command = browseFiles,bd=4,cursor='hand2',font=Font_tuple) 
Browse_B.grid(row=0,column=5,pady=30)


Submit_B=Button(window,text="Submit",bd=4,command=ShowImage,cursor='hand2',font=Font_tuple)
Submit_B.grid(row=3,column=0,pady=10)

Exit_B=Button(window,text="Exit",bd=4,command=window.destroy,cursor='hand2',font=Font_tuple)
Exit_B.grid(row=3,column=5,pady=10)

Choose_L=Label(window,text="Choose the retrival method: ",bg='#1f666b',font='Helvetica 11 bold').place(x=5,y=5)


        
combobox=ttk.Combobox(window,font='Helvetica 11')
combobox['values']=('Average RGB','Histogram','Several Histograms','CBVR')
combobox.place(x=210,y=5)
combobox.current(0)

window.mainloop()
