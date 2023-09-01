from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6f4f40dcaf97c0ba8e8551c6038d4ee9").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    ppr_label1.config(text=data["main"]["pressure"])





win = Tk()

win.title("CodSoft")
win.config(bg="brown")
win.geometry("500x500")

name_label = Label(win, text="CodSoft Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name=StringVar()

list_name=("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
com = ttk.Combobox(win, values=list_name ,font=("Times New Roman", 18, "bold"), textvariable=city_name)
com.place(x=50, y=120, height=30, width=400)

done_button = Button(win,text="Done", font=("Arial", 25, "bold"), command=data_get)
done_button.place(x=200, y=170, height=30, width=100)

w_label = Label(win, text="Weather Climate", font=("Times New Roman", 18, "bold"))
w_label.place(x=50, y=220, height=30, width=180)

w_label1 = Label(win, text="", font=("Times New Roman", 18, "bold"))
w_label1.place(x=300, y=220, height=30, width=180)

wb_label = Label(win, text="Weather Description", font=("Times New Roman", 18, "bold"))
wb_label.place(x=50, y=270, height=30, width=220)

wb_label1 = Label(win, text="", font=("Times New Roman", 18, "bold"))
wb_label1.place(x=300, y=270, height=30, width=180)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 18, "bold"))
temp_label.place(x=50, y=320, height=30, width=150)

temp_label1 = Label(win, text="", font=("Times New Roman", 18, "bold"))
temp_label1.place(x=300, y=320, height=30, width=150)

ppr_label = Label(win, text="Pressure", font=("Times New Roman", 18, "bold"))
ppr_label.place(x=50, y=370, height=30, width=100)

ppr_label1 = Label(win, text="", font=("Times New Roman", 18, "bold"))
ppr_label1.place(x=300, y=370, height=30, width=100)

win.mainloop()