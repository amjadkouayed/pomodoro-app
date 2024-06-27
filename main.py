'''
pomodoro app

1- timer in the middle
2- start button that starts the work time
3- pause bottom that starts the pause timer
4- stop botton 
5- records the work time 

'''
from tkinter import *
from time import *


window = Tk()
window.geometry("600x600")
window.title("Pmodoro Timer")
window.config(padx=50, pady=50)

def work_timer():
    pass

def break_timer():
    pass

def stop():
    pass

start_button = Button(text= "Start", command= work_timer, padx= 10, pady= 10)
start_button.place(x= 100, y= 450)

break_button = Button(text= "Break", command= break_timer, padx=10, pady= 10)
break_button.place(x= 225, y= 450)

stop_button = Button(text= "Stop", command= stop, padx=10, pady= 10)
stop_button.place(x= 350, y= 450)

label = Label(text= "timer", font=("Ariel", 40, "bold"))
label.pack(side="top")

timer = Label(text= "00:00", font=("Ariel", 40) , padx= 40, pady=100)
timer.pack()

full_time_label = Label(text= " full time: ", font=("ariel", 20))
full_time_label.place(x= 100, y=350)

mainloop()