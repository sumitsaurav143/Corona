from plyer import notification
import requests
from bs4 import BeautifulSoup
from tkinter import *


def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon = "corona.ico",
        timeout=10
        )

def getData(url):
    r = requests.get(url)
    return r.text

data=[]
state=[]

if __name__ == "__main__":
    root=Tk()
    root.geometry("500x400")
    myHtmlData= getData("https://covidindia.org/")
    soup=BeautifulSoup(myHtmlData,'html.parser')
    #print(soup.prettify())
    for tr in soup.find_all('tbody')[0].find_all('td'):
        data.append(tr.get_text())
    for i in range(0,len(data),4):
        state.append(data[i:i+4])
    indiacase=0
    for i in range(len(state)):
        indiacase=indiacase+(int(state[i][1]))
    print("Total India Cases: ",indiacase)
    #print("----------------------------------")
    #print("     INDIA CORONA CASES FINDER    ")
    #print("----------------------------------\n")
    while 1:
        c=0
        find=input("Enter State Name: ")
        for i in state:
            if i[0].lower()==find.lower():
                    print("**********************************")
                    print("Total Confirmed Cases: ",i[1],"\nTotal Recoveries: ",i[2],"\nTotal Deaths: ",i[3])
                    print("**********************************\n")
                    notifyme(i[0]+" (Corona Status)","Total Confirm Cases: "+i[1]+"\nActive Cases: "+str(int(i[1])-(int(i[2])+int(i[3])))+"\nRecoveries: "+i[2]+"\nDeaths: "+i[3])
                    c=1
        if c==0:
            print("\n!!!WRONG STATE INPUT!!!\n")
root.mainloop()
