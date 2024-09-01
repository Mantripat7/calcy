from tkinter import * 
root=Tk()

root.geometry("454x567+360+100")
root.title("CALCULATOR")
root.config(background="black")

def cal(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="C":
        scvalue.set("")
        e1.update()
    elif text == "=":
        try:
            if scvalue.get().isdigit():
                value=int(scvalue.get())
            else:
                value=eval(scvalue.get())
        except:
            scvalue.set("Error")
            e1.update()

        scvalue.set(value)
        e1.update()

    elif text == "DEL":
        scvalue.set(scvalue.get()[:-1])         # x=scvalue.get()  x=x[:-1]  scvalue.set(x)   
        e1.update()
        
    else:
        scvalue.set(scvalue.get() + text)
        e1.update()

scvalue= StringVar()
scvalue.set(" ")

e1=Entry(root,textvar=scvalue,font="bold 35 roman")
e1.pack(fill=X,pady=20,padx=10)

f1=Frame(root,height=250,width=200)
b1=Button(f1,text="C",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="DEL",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="%",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="/",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
f1.pack(side=TOP,anchor=W,padx=20)

f1=Frame(root,height=250,width=200)
b1=Button(f1,text="7",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="8",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="9",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="*",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
f1.pack(side=TOP,anchor=W,padx=20)

f1=Frame(root,height=250,width=200)
b1=Button(f1,text="4",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="5",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="6",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="-", font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
f1.pack(side=TOP,anchor=W,padx=20,pady=3)

f1=Frame(root,height=250,width=200)
b1=Button(f1,text="1",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="2",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="3",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="+",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
f1.pack(side=TOP,anchor=W,padx=20,pady=3)

f1=Frame(root,height=250,width=200)
b1=Button(f1,text="00",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text=".",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="0",font="lucida 20 bold" ,padx=15,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",cal)
b1=Button(f1,text="=",font="lucida 20 bold" ,padx=30,pady=5)
b1.pack(side=LEFT,padx=20,pady=10)
b1.bind("<Button-1>",cal)
f1.pack(side=TOP,anchor=W,padx=20,pady=3)

root.mainloop()