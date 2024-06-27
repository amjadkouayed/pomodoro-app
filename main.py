'''
pomodoro app

1- timer in the middle
2- start button that starts the work time
3- pause bottom that starts the pause timer
4- break button 
4- stop botton 
5- records the work time 

'''
from tkinter import *
from plyer import notification


timer_running = False
current_timer = None
total_work_time = 0  
paused = False
remaining_time = 0

def work_timer():
    global timer_running, current_timer, paused, remaining_time
    if timer_running and not paused:
        return
    if paused:
        resume_timer()
    else:
        timer_running = True
        label.config(text="Work")
        countdown(30 * 60) 

def break_timer():
    global timer_running, current_timer, paused, remaining_time
    if timer_running and not paused:
        return
    if paused:
        resume_timer()
    else:
        timer_running = True
        label.config(text="Break")
        countdown(5 * 60)  
        
def pause_timer():
    global current_timer, paused, remaining_time
    if current_timer is not None:
        window.after_cancel(current_timer)
    paused = True
    remaining_time = int(timer.cget("text").split(":")[0]) * 60 + int(timer.cget("text").split(":")[1])

def resume_timer():
    global paused
    paused = False
    countdown(remaining_time)

def stop():
    global timer_running, current_timer, paused
    if current_timer is not None:
        window.after_cancel(current_timer)
        current_timer = None
    timer_running = False
    paused = False
    timer.config(text="00:00")
    label.config(text="Timer")

def countdown(seconds):
    global current_timer, total_work_time
    minutes, secs = divmod(seconds, 60)
    timer.config(text=f"{minutes:02}:{secs:02}")
    if seconds > 0 and not paused:
        current_timer = window.after(1000, countdown, seconds - 1)
    elif seconds == 0:
        if label.cget("text") == "Work":
            total_work_time += 30 * 60  
            update_total_work_time()
            show_notification("work session is over", "Take a break")
        elif label.cget("text") == "Break":
            show_notification("Break is over", "Get back to work")
        stop()

def update_total_work_time():
    global total_work_time
    minutes, secs = divmod(total_work_time, 60)
    hours, minutes = divmod(minutes, 60)
    full_time_label.config(text=f"Full time: {hours:02}:{minutes:02}:{secs:02}")

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

window = Tk()
window.geometry("600x600")
window.title("Pomodoro Timer")
window.config(padx=50, pady=50)

start_button = Button(window, text="Start", command=work_timer, padx=10, pady=10)
start_button.place(x=50, y=450)

break_button = Button(window, text="Break", command=break_timer, padx=10, pady=10)
break_button.place(x=150, y=450)

pause_button = Button(window, text="Pause", command=pause_timer, padx=10, pady=10)
pause_button.place(x=275, y=450)

stop_button = Button(window, text="Stop", command=stop, padx=10, pady=10)
stop_button.place(x=375, y=450)

label = Label(window, text="Timer", font=("Arial", 40, "bold"))
label.pack(side="top")

timer = Label(window, text="00:00", font=("Arial", 40), padx=40, pady=100)
timer.pack()

full_time_label = Label(window, text="Full time: 00:00:00", font=("Arial", 20))
full_time_label.place(x=100, y=350)

mainloop()

