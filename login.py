from tkinter import *
from tkvideo import tkvideo
from heather import cityfind

root=Tk()
root.title("LOGIN")
root.state('zoomed')

imglbl=Label(root)
imglbl.place(x=0, y=0, relwidth=1, relheight=1)
player = tkvideo("C:/Users/dr_de/Documents/VS/6.0/backvid.mp4", imglbl,loop = 1, size = (1920,1080))
player.play()

frame=Frame(root,bg='#2896BD', relief=RAISED)
frame.place(x=760,y=390,anchor='center')

name=Label(frame,text="NAME",background="#2896BD",fg='black', font=('Book Antiqua', 11))
name.grid(row=0,column=0,padx=8,pady=(5,0))
city=Label(frame,text="CITY",background="#2896BD",fg='black', font=('Book Antiqua', 11))
city.grid(row=1,column=0)
pincode=Label(frame,text="PINCODE",background="#2896BD",fg='black', font=('Book Antiqua', 11))
pincode.grid(row=2,column=0)

name_box=Entry(frame,width=35,borderwidth=2)
name_box.grid(row=0,column=1,pady=(5,0),padx=10)
city_box=Entry(frame,width=35,borderwidth=2)
city_box.grid(row=1,column=1)
pin_box=Entry(frame,width=35,borderwidth=2)
pin_box.grid(row=2,column=1)

sendbtn=Button(frame,text="SUBMIT",command=lambda: cityfind(city_box.get(),name_box.get()))
sendbtn.grid(row=3,column=1,columnspan=2,padx=10,pady=5,ipadx=50)

root.mainloop()
