import urllib.parse
import requests
from tkinter import *

#Create an instance of tkinter window or frame
win=Tk()

orig,dest = "",""

def get_input():
   global orig
   global dest
   orig = source_txt.get(1.0, "end-1c")
   dest = destination_txt.get(1.0, "end-1c")

#Creating a text box widget for source
source_lbl = Label( win, text="Source City")
source_txt=Text(win, height=5, width=40)
source_lbl.pack()
source_txt.pack()

#Creating a text box widget for destination

destination_lbl = Label( win, text="Destination City")
destination_txt=Text(win, height=5, width=40)
destination_lbl.pack()
destination_txt.pack()
#Create a button for Comment

navigate= Button(win, height=5, width=10, text="Navigate", command=get_input)


#command=get_input() will wait for the key to press and displays the entered text
navigate.pack()

win.mainloop()




main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MhvbvH6lJAKgMu9wisKM5iSoZWOFFPQJ"    # You should use your own key 
while True:
    # orig = input ("Source City :")
    # if orig == "quit" or orig == "q":
    #     break
    # dest = input("Dest City :")
    # if dest == "quit" or dest == "q":
    #     break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ("URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print ("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6)))
        print("Fuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
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
