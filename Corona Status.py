from tkinter import *
from plyer import notification
import requests
from bs4 import BeautifulSoup
import re

def getData(url):
    r = requests.get(url)
    return r.text

State=[]
StateData= getData("https://api.covid19india.org/csv/latest/state_wise.csv")
sd=re.split(r'\r',StateData)
for i in range(2,len(sd)):
    State.append(sd[i].split(",")[0][1:])
State.sort()
#print(State)

Dist={}

DistData= getData("https://api.covid19india.org/csv/latest/district_wise.csv")
dd=re.split(r'\r',DistData)
for i in State:
    data={}
    for j in dd:
        if j.split(",")[2]==i:
            data[j.split(",")[4]]=[j.split(",")[5],j.split(",")[6],j.split(",")[7],j.split(",")[8]]
    else:
        Dist[i]=data

#for i in Dist.keys():
    #print(i)#District
    #for j in Dist[i].keys():
        #print(j,Dist[i][j][0])#District Data
        

def status():
        c=0
        find=l2.get()
        for i in sd:
            if ((i.split(",")[0][1:]).lower())==find.lower():
                    l4=Label(root,text="Status Showed",font="arial 10 bold",bg="yellow")
                    l4.place(x=163,y=148)
                    tc=Label(root,
                             font="arial 20 bold",
                             text="*****LIVE STATUS*****\nTotalConfirm Cases: "+i.split(",")[1]+"\nRecovered Cases: "+i.split(",")[2])
                    tc.place(x=10,y=250)
                    notifyme(i.split(",")[0][1:]+" (Corona Status)",
                             "Total Confirm Cases: "+i.split(",")[1]+
                             "\nRecovered Cases: "+(i.split(",")[2])+
                             "\nLast Update: "+(i.split(",")[5]))
                    c=1
        if c==0:
            l4=Label(root,text=" Wrong State!! ",font="arial 10 bold",bg="yellow")
            l4.place(x=165,y=148)
            
def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon = "corona.ico",
        timeout=10
        )

root=Tk()
root.geometry("400x450+450+150")
root.config(bg="Black")
root.resizable(False,False)
root.title("Covide Status Finder")
l=Label(root,text="INDIA COVID STATUS FINDER",bg="Black",fg="red",font="arial 17 bold")
l.pack()
l1=Label(root,text="Enter State: ",bg="Black",fg="white",font="arial 15 bold")
l1.place(x=15,y=80)
l2=Entry(root,font="arial 16 bold",bg="pink",width=15)
l2.place(x=150,y=82)
b1=Button(root,text="SHOW STATUS",bg="red",font="arial 10 bold",command=status)
b1.place(x=160,y=180)
l3=Label(root,text="Created By Sumit Saurav",bg="Black",fg="white",font="arial 8 bold")
l3.place(x=260,y=430)


root.mainloop()
