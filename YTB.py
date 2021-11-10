# Import module
from tkinter import *
from tkinter.ttk import Progressbar
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from pathlib import Path
from datetime import timedelta
	
#splash screen window
splash_root = Tk()
splash_root.geometry("500x330")
splash_root.title("Opening YouTube Video Downloader....")

#splash screen image
image=Image.open("yt.png")
resize_img=image.resize((500,330))
img=ImageTk.PhotoImage(resize_img)

limg=Label(splash_root,image=img,bd=0)
limg.image=img
limg.place(x=0,y=0)

#splash screen progress bar
progress = Progressbar(splash_root, orient = HORIZONTAL,
                       length = 500, mode = 'determinate')
progress.start(20)
progress.place(x=0,y=308)
#splash screen window end





# main window function
def main():
    # destory splash screen
    splash_root.destroy()
    
    #Main window
    root = Tk()
    root.title("YouTube Video Downloader")
    root.geometry("550x500")
    root.configure(bg="old lace")


    #Download Function
    def Download(url):
        if (len(n.get())==0):
            messagebox.showinfo("Missing","Select Format then click on download")
        else:
            #print (downdata[n.get()])
            downloads_path = str(Path.home() / "Downloads")
            #print (downloads_path)
            yt = YouTube(url)
            data = yt.streams.get_by_itag(downdata[n.get()])
            #print (data)
            data.download(downloads_path)
            messagebox.showinfo("Successful","Downloaded Successfully")
            print (data)

    #global variable for accessing the itag   
    downdata = dict()
    #global variable for accessing selected item in combobox
    n = StringVar()

    #Onclick Search
    def searchl(url):
        if (len(url)==0):


            messagebox.showinfo("Missing","Enter URL then click on search")
        elif ("youtube.com/watch" not in url):
            messagebox.showinfo("Missing","Enter valid url")
        else:
            info = list()
            #print (url)
            yt = YouTube(url)
            dd1=Label(root,text="Title",font = ("Helvetica",14),bg="old lace").place(x=10,y=220)
            dd2=Label(root,text=": " + yt.title,font = ("Helvetica",14),bg="old lace").place(x=160,y=220)
            dd3=Label(root,text="Views",font = ("Helvetica",14),bg="old lace").place(x=10,y=250)
            dd4=Label(root,text=": " + str(yt.views),font = ("Helvetica",14),bg="old lace").place(x=160,y=250)
            a = timedelta(seconds=yt.length)
            dd3=Label(root,text="Duration",font = ("Helvetica",14),bg="old lace").place(x=10,y=280)
            dd4=Label(root,text=": " + str(a) + "seconds",font = ("Helvetica",14),bg="old lace").place(x=160,y=280)
            dd3=Label(root,text="Rating",font = ("Helvetica",14),bg="old lace").place(x=10,y=310)
            dd4=Label(root,text=": " + str(yt.rating),font = ("Helvetica",14),bg="old lace").place(x=160,y=310)
    
            data = yt.streams.filter(type="video")
            for i in data:  
                info.append(i.mime_type + " " + i.resolution)
                downdata[i.mime_type + " " + i.resolution] = i.itag
            
            data = yt.streams.filter(type="audio")
            for i in data:  
                info.append(i.mime_type + " " + i.abr)
                downdata[i.mime_type + " " + i.abr] = i.itag
                
                        
            #DOWNLOAD FORMAT
            l2=Label(root,text="Choose Format :",font = ("Helvetica",14),bg="old lace").place(x=10,y=340)
            fformat = ttk.Combobox(root, width = 45, textvariable = n)
            fformat['state'] = "readonly"
            fformat['values'] = info
            fformat.place(x=160,y=340)
            download = Button(root, text="Download",width=10,command=lambda: Download(url)).place(x=210,y=385)
        

    #URL Paste
    l1=Label(root,text="Video URL :",font = ("Helvetica",14),bg="old lace").place(x=10,y=185)
    q=StringVar()
    e=Entry(root,textvariable=q,font = ("Helvetica",10),width=35, bd=9).place(x=160,y=185)
    search = Button(root, text="Search",width=10,command=lambda: searchl(q.get())).place(x=430,y=185)
    
    
    #Main page Image
    image=Image.open("yt1.png")
    resize_img=image.resize((545,170))
    img=ImageTk.PhotoImage(resize_img)
    limg=Label(root,image=img,bg="old lace")
    limg.image=img
    limg.place(x=0,y=0)



# Set Interval
splash_root.after(1600,main)

# Execute tkinter
mainloop()