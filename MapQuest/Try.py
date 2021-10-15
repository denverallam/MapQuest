import urllib.parse
import requests
from tkinter import *

#Create an instance of tkinter window or frame
win=Tk()

scrollbar = Scrollbar(win)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(win, yscrollcommand = scrollbar.set )


orig,dest,gas = "","",""
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MhvbvH6lJAKgMu9wisKM5iSoZWOFFPQJ"    # You should use your own key 

def get_direction():
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
        print ("URL ", (url))
        Label( win, text="Destination City").pack()
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
                # Label( win, text="API Status: " + str(json_status) + " = A successful route call.\n").pack()
                Label( win, text="Directions from " + (orig) + " to " + (dest)).pack()
                Label( win, text="Trip Duration: " + (json_data["route"]["formattedTime"])).pack()
                Label( win, text="Kilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))).pack()
                Label( win, text="Fuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))).pack()
                Label( win, text="Money to be Spent on Fuel: " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78 * gas))).pack()
                scrollbar.pack(side=RIGHT, fill = Y)
                myList = Listbox(win,  yscrollcommand=scrollbar.set, width=70)
                for each in json_data["route"]["legs"][0]["maneuvers"]:
                        # Label( win, textvariable=narrative).pack()
                        narrative = each["narrative"] + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")
                        myList.insert(END, narrative)
                myList.pack(side=LEFT, fill=BOTH)
                scrollbar.config(command=myList.yview)

        elif json_status == 402:
                print("**********************************************")
                print("Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations.")
                print("**********************************************\n")
        elif json_status == 611:
                print("**********************************************")
                print("Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations.")
                print("**********************************************\n")
        else:
                print("************************************************************************")
                print("For Staus Code: " + str(json_status) + "; Refer to:")
                print("https://developer.mapquest.com/documentation/directions-api/status-codes")
                print("************************************************************************\n")

def get_input():
   global orig
   global dest
   global gas
   orig = source_txt.get(1.0, "end-1c")
   dest = destination_txt.get(1.0, "end-1c")
   gas = gas_txt.get(1.0, "end-1c")
   get_direction()
   Button(win, height=1, width=10, text="Close ", command=destroy)

def destroy():
        win.destroy()
#Creating a text box widget for source
source_lbl = Label( win, text="Source City")
source_txt=Text(win, height=2, width=40)
source_lbl.pack()
source_txt.pack()

scrollbar = Scrollbar(win)

destination_lbl = Label( win, text="Destination City")
destination_txt=Text(win, height=2, width=40)
destination_lbl.pack()
destination_txt.pack()

#Creating a text box widget for destination

gas_lbl = Label( win, text="Gas Price")
gas_txt=Text(win, height=2, width=40)
gas_lbl.pack()
gas_txt.pack()
#Create a button for Comment

navigate= Button(win, height=1, width=10, text="Navigate", command=get_input)


#command=get_input() will wait for the key to press and displays the entered text
navigate.pack()
win.mainloop() 






