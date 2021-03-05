from tkinter import *
import json
import requests	
def getTemperature():
	getReq = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + userEntry.get() + '&appid=5c89bf395effa277f54aaad228fb81e3&units=metric')
	getReq_dict = getReq.json()
	data = "Temperature of "  + str(userEntry.get()) + " is: " + str(getReq_dict['main']['temp']) + "°C"
	label = Label(text = data, bg = 'pink')
	label.grid(row = 2, column = 1)
	


root = Tk()
root.title("Temperature Finder")
root.geometry('500x300')
root.minsize(150, 150)
root.maxsize(1200, 1200)
city = Label(text = "Enter a city name to check Temperature: ")
cityValue = StringVar() #type of data 
userEntry = Entry(root) #entered data 

userEntry.grid(row = 0, column = 1)
city.grid(row = 0)
Button(text = "submit", command = getTemperature).grid(column = 1)


root.mainloop()