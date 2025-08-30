from tkinter import *
window=Tk()
window.title("draw")
window.geometry("500x500")
window.configure(background="black")
window.resizable(False,False)
canvas=Canvas(window,width=480,height=440,background="white")
canvas.pack(padx=10,pady=10)
def draw(event):
    x,y=event.x,event.y
    canvas.create_oval(x-2,y-2,x+2,y+2,fill="black")
canvas.bind("<B1-Motion>",draw)
button=Button(window,text="CLEAR",command=lambda: canvas.delete("all"),bg="white",fg="black")
button.pack(padx=5)
window.mainloop()