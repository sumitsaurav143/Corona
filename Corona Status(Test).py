from tkinter import *
import requests
import re
from tkinter import ttk
from tkinter import messagebox

msgurl = "https://www.fast2sms.com/dev/bulk"

def mainn():
    global msgurl
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


    def status():
            find=statechoose.get()
            if statechoose.get() in Dist.keys():
                Dis=[]
                for j in Dist[statechoose.get()].keys():
                    Dis.append([j+" : "+"Total Cases="+str(Dist[statechoose.get()][j][0])])#District Data
            
             
      
            listbox = Listbox(root,width=66,height=20,font="arial 13 bold")  
            for i in range(len(Dis)):
                listbox.insert(i,Dis[i])    
       
            listbox.place(x=640,y=200)  
            
            
            for i in sd:
                if ((i.split(",")[0][1:]).lower())==find.lower():
                        tc=Label(root,
                                 font="arial 15 bold",
                                 text="Total Confirm Cases: "+i.split(",")[1]+
                                 "\nRecovered Cases: "+i.split(",")[2]+
                                 "\nTotal Deaths: "+(i.split(",")[3])+
                                 "\nActive Cases: "+(i.split(",")[4])+"\n"+
                                 "\nDate_Time: "+(i.split(",")[5]))
                        tc.place(x=85,y=540)
                        l4=Label(root,text="----------Last Updated On----------",font="arial 10 bold",bg="red")
                        l4.place(x=132,y=640)
                        global msg
                        msg="----------"+i.split(",")[0]+"\n----------\nTotal Confirm Cases: "+i.split(",")[1]+"\nRecovered Cases: "+i.split(",")[2]+"\nTotal Deaths: "+(i.split(",")[3])+"\nActive Cases: "+(i.split(",")[4])+"\n"+"\nUpdated At: "+(i.split(",")[5])
                    
            def mssg():
                querystring = {"authorization":"LfFOWD0vGeBgyNtb42RquXEkrUYSKpZQzHTij6dVaw571coJ8hhjT5M8SFaWqPkOgnDl3syrINeAYdz0","sender_id":"FASTWP","message": msg,"language":"english","route":"p","numbers":numb.get()}

                headers = {'cache-control': "no-cache"}

                response = requests.request("GET", msgurl, headers=headers, params=querystring)

                if "true" in response.text:
                    messagebox.showinfo("Notification","Message Sent")
                else:
                    messagebox.showinfo("Notification","Message Not Sent!!")
            
            n=Label(root,text="Mobile Number:",font="Arial 15 bold",bg="white")
            n.place(x=650,y=672)
            n1=Label(root,text="Enter Your Number Below To Get Status On Your Mobile",font="Arial 10 bold",bg="yellow")
            n1.place(x=650,y=645)
            numb=Entry(root,width=12,font="arial 16")
            numb.place(x=815,y=675)
            print(msg)
            send=Button(root,text="SEND STATUS",bg="Blue",font="arial 12 bold",command=mssg)
            send.place(x=1100,y=675)

    root=Tk()
    #root.attributes('-fullscreen', True)
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.config(bg="Black")
    root.resizable(True,True)
    logo = PhotoImage(file="bgg.gif")
    w1 = Label(root, image=logo).pack()
    root.title("Covide Status Finder")
    l=Label(root,text="INDIA COVID STATUS FINDER",bg="Black",fg="red",font="arial 17 bold")
    l.pack()
    l1=Label(root,text="Select State: ",bg="white",font="arial 15 bold")
    l1.place(x=55,y=130)


    # Combobox creation
    n = StringVar()
    statechoose = ttk.Combobox(root, width = 27, textvariable = n)
    statechoose['values'] = State
    statechoose.place(x=180,y=135)
    statechoose.current()


    b1=Button(root,text="SHOW STATUS",bg="red",font="arial 12 bold",command=status)
    b1.place(x=172,y=190)
    l3=Label(root,text="Created By Sumit Saurav",bg="Black",fg="white",font="arial 8 bold")
    l3.place(x=260,y=710)
    root.mainloop()

#Check Internet Connection
try:
    request=requests.get(msgurl,timeout=None)
    mainn()
except(requests.ConnectionError, requests.Timeout) as exception:
    messagebox.showwarning("Notification","Please Connect to Internet First!!")
