from tkinter import *
import requests
import json
from PIL import Image
from PIL import ImageTk
import time
from quotes import quotes
import random
from tkvideo import tkvideo
import os
from activities import weather1,weather2,activities1,activities2


#https://api.weatherbit.io/v2.0/current?postal_code=302016&key=+os.environ.get('API')+&include=minutely

def cityfind(citye,namee):

    root1=Toplevel()
    root1.title("HeatherBit")
    root1.geometry("1080x800")

    imglbl=Label(root1)
    imglbl.place(x=0, y=0, relwidth=1, relheight=1)
    player = tkvideo("C:/Users/dr_de/Documents/VS/6.0/topbackvid1.mp4", imglbl,loop = 1, size = (1920,1080))
    player.play()

    frame0=Frame(root1)
    frame0.place(x=550,y=75,anchor='center')

    labeln=Label(frame0,text="Hello "+namee+"!",font=("Cascadia Mono SemiBold", 25),bg="#060840",fg="#8ceaff")
    labeln.pack()

    frame1=Frame(root1,highlightbackground="#655fed", highlightthickness=1.5)
    frame1.place(x=325,y=103)

    myimg2=Image.open("C:/Users/dr_de/Documents/VS/6.0/frameback1.jpg")
    resize2=myimg2.resize((200,307),Image.ANTIALIAS)
    newimg2=ImageTk.PhotoImage(resize2)
    imglbl=Label(frame1,image=newimg2)
    imglbl.grid(row=1,column=0)

    frame2=Frame(root1,highlightbackground="#000000", highlightthickness=1.5)
    frame2.place(x=667,y=150,anchor='center')

    labelt = Label(frame2, font=("Boulder", 25, 'bold'), bg="#1e2114", fg="#fff708", bd=25) 
    labelt.grid(row=0, column=0)

    def digital_clock(): 
            time_live = time.strftime("%I:%M:%S %p")
            labelt.config(text=time_live) 
            labelt.after(200, digital_clock)
    digital_clock()

    frame3=Frame(root1,highlightbackground="#060840", highlightthickness=1.5)
    frame3.place(x=667,y=250,anchor='center')

    i=random.randint(0, len(quotes)-1)
    labelq=Label(frame3,width=22,font=("Malgun Gothic",14,'italic'), bg="#291e75", fg="#fc5e03",wraplengt=200,bd=2)
    labelq.config(text='"'+quotes[i]+'"')
    labelq.grid(row=0,column=0,sticky=W+E)

    frame4=Frame(root1, bg="#b279fc")
    frame4.place(x=667,y=360,anchor='center') 
    steps=IntVar()
    label_s = Label(frame4,text="0/8000",width=10,height=1,font=("Cascadia Mono SemiBold", 25), bg="#b279fc", fg="#3d3842",bd=20) 
    label_s.grid(row=0, column=0,columnspan=2,sticky=W+E,padx=8)
    sentry=Entry(frame4)
    sentry.insert(0,"Enter today's steps:")
    sentry.grid(row=2,column=0,padx=(6,3))

    def temp_text(e):
        sentry.delete(0,"end")
    sentry.bind("<FocusIn>", temp_text)

    def update():
        steps.set(steps.get()+int(sentry.get()))
        label_s.config(text=str(steps.get())+"/8000")
        if steps.get()>=8000:
            label_s.config(text="8000/8000")
            labeln = Label(frame4,text="GREAT JOB!",font=("Cascadia Mono SemiBold", 9), bg="#b279fc", fg="#3d3842")
            labeln.place(x=120,y=73,anchor='center')
        sentry.delete(0,END)

    upd=Button(frame4,text="UPDATE STEPS",command=update)
    upd.grid(row=2,column=1,padx=(0,5),pady=(0,2))

    frame5=Frame(root1,bg="#224f80",highlightbackground="#000000", highlightthickness=1.5,width=470,height=50)
    frame5.grid_propagate(0)
    frame5.place(x=558,y=450,anchor='center')
    labela=Label(frame5,font=("Consolas", 20,),bg="#224f80",fg="#4f96bd",wraplengt=2000)
    labela.grid(row=0,column=0,sticky=W+E,padx=(125,0))

    w1=random.randint(0, len(activities1)-1)
    w2=random.randint(0, len(activities2)-1)

    try:
        apireq=requests.get("https://api.weatherbit.io/v2.0/current?city="+citye+"&key="+os.environ.get('API'))   
        api=json.loads(apireq.content)
        city=api['data'][0]['city_name']
        aqi=api['data'][0]['aqi']
        weather=api['data'][0]['weather']['description']
        temp=api['data'][0]['temp']
        country=api['data'][0]['country_code']

        apilabel=Label(frame1,text=city+"\n"+str(temp)+"°C\n"+weather+"\n Air Quality "+str(aqi),font=("Book Antiqua",15),background="#77C2EC")
        apilabel.grid(row=1,column=0)

        if weather in weather1:
            labela.config(text=activities1[w1])
        elif weather in weather2:
            labela.config(text=activities2[w2])

    except Exception as e:
        api="error..."

    root1.mainloop()

cityfind("Jaipur","Devansh")