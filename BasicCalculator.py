from tkinter import *
window = Tk()
window.title("ABHI'S CALCULATOR")
window.geometry("360x500")
window.configure(bg="black")
window.resizable(False,False)
def click(value):
    display.configure(state="normal")
    display.insert(END,value)
    display.configure(state="readonly")
def clear():
    display.configure(state="normal")
    display.delete(len(display.get())-1)
    display.configure(state="readonly")
def fclear():
    display.configure(state="normal")
    display.delete(0, END)
    display.configure(state="readonly")
def equal():
    display.configure(state="normal")
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0,END)
        display.insert(END,"ERROR")
    display.configure(state="readonly")
display=Entry(window,font=('arial',20,'bold'),justify='right',bd=20,relief="flat")
display.grid(row=0,column=1,columnspan=4,padx=10,pady=10)
display.configure(state="readonly")
buttons=[
    ['1','2','3','+'],
    ['4','5','6','-'],
    ['7','8','9','*'],
    ['.','0','BCK','/'],
    ['=','CLR']

]
for r,row in enumerate(buttons,start=1):
    for c,bt in enumerate(row,start=1):
        if bt =='BCK':
            cmd=lambda:clear()
        elif bt =='CLR':
            c=3
            cmd=lambda:fclear()
        elif bt =='=':
            c=2
            cmd=lambda:equal()
        else:
            cmd=lambda ch=bt: click(ch)
        Button(window,text=bt,command=cmd,bd=20,relief='sunken').grid(row=r,column=c,padx=10,pady=10)

window.title("ABHI'S CALCULATOR")
window.mainloop()