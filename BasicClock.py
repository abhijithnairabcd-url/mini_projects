from tkinter import*
from time import strftime
window=Tk()
window.geometry("300x300")
window.title("clock")
window.resizable(False,False)
window.configure(background="black")
def times():
    timer=strftime('%H:%M:%S')
    label.config(text=timer)
    label.after(1000,times)
label=Label(window,font=('arial',20,'bold'),background="black",foreground="white")
label.pack(expand=True,fill="x")
darkmode=True
def theme():
    global darkmode
    if darkmode:
        darkmode=False
        window.configure(background="white")
        label.config(background="white",fg="black")
        themebutton.config(text="Switch to dark theme")
    else:
        darkmode=True
        window.configure(background="black")
        label.config(bg="black",fg="white")
        themebutton.config(text="Switch to light theme")
themebutton=Button(window,text="switch to light theme",bg="grey",fg="black",command=theme,bd=0)
themebutton.pack(pady=10)
times()
window.mainloop()