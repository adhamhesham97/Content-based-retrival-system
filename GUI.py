from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


window=Tk()
window.title('Content based multimedia retrival')
window.geometry("700x500+150+150")
window.columnconfigure(0,weight=2)
window.configure(bg='#1f666b')
ent1=Entry(window,font=40,width=60,bd=4)
ent1.place(anchor=NW)  
ent1.grid(pady=10)
                                
image_path='image2.jpg'                  #Path of Retieved image
def browseFiles():
    filename = filedialog.askopenfilename(
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("PNG files","*.png*")
                                                       ))
    ent1.insert(0,filename)
def ShowImage():
    photo=ImageTk.PhotoImage(Image.open(ent1.get()))
    l1=Label(window)
    l1.config(image=photo)
    l1.image=photo
    l1.place(x=2,y=200)
    l2=Label(window,text="Input Image",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
    l2.place(x=20,y=160)
    photo1=ImageTk.PhotoImage(Image.open(image_path))
    l3=Label(window)
    l3.config(image=photo1)
    l3.image=photo1
    l3.place(x=470,y=200)
    l4=Label(window,text="Retieved Image",bg='#1f666b',height=1,width=12,bd=6,font='Helvetica 11 bold')
    l4.place(x=520,y=160)
    
    Method=combobox.get()                   #Combobox 
    

    
Font_tuple = ("Comic Sans MS", 9,"bold")
b1= Button(window,text = "Browse Files",
                        command = browseFiles,bd=4,font=Font_tuple) 

b1.grid(row=0,column=5,pady=30)
b2=Button(window,text="Submit",bd=4,command=ShowImage,cursor='hand2',font=Font_tuple)
b2.grid(row=3,column=0,pady=10)

l5=Label(window,text="Choose the retrival method: ",bg='#1f666b',font='Helvetica 11 bold').place(x=5,y=5)


        
combobox=ttk.Combobox(window,font='Helvetica 11')
combobox['values']=('Average RGB','Histogram','Several histograms','CBVR')
combobox.place(x=210,y=5)
combobox.current(0)



b3=Button(window,text="Exit",bd=4,command=window.destroy,font=Font_tuple)
b3.grid(row=3,column=5,pady=10)


window.mainloop()