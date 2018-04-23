from Tkinter import *
from login_page import *
from register import *
from contact import*
from menu import *
from request_pizza import *



def ask_quit():
    if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
        root.destroy()


import sqlite3
conn = sqlite3.connect('pds.db')
c=conn.cursor()
#c.execute("CREATE TABLE USER_DETAIL (NAME text,GENDER real ,ADDRESS text,PHONE real,EMAIL text,PASSWORD text)")
conn.commit()
conn.close()

root=Tk()
root.geometry("1600x800+0+0")
root.title("Pizza Delivery system")
root.configure(bg="white")


Tops=Frame(root, width=1600, height=50, bg="white")
Tops.pack(side=TOP)

f1=Frame(root, width=800, height=700, bg="white")
f1.pack(side=TOP)


lblinfo = Label(Tops, font=('arial', 50 , 'bold' ), text="PIZZA DELIVERY SYSTEM" , fg="blue",bg="yellow", bd=10,anchor='w')
lblinfo.grid(row=0,column=0)



lab=Label(f1,text="\n\n\n\n\n\n\n\n\n\n",bg="white")
lab.grid(row=0,column=0)



lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=1,column=2)


B2=Button(f1,text="Menu",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="blue",relief="raised",command=pizza_menu)
B2.grid(row=1,column=3)

lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=1,column=4)


B3=Button(f1,text="Login / SignUp",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="blue",relief="raised",command=login)
B3.grid(row=1,column=1)

B1=Button(f1,text="Order",width=10,height=4,bd=5,font=('arial',20,'bold'),fg="white",bg="green",relief="raised",command=order)
B1.grid(row=1,column=5)

lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=1,column=6)


B4=Button(f1,text="Track Order",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="blue",relief="raised",command=login)
B4.grid(row=1,column=7)

lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=1,column=8)

B5=Button(f1,text="Contact Us",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="blue",relief="raised",command=contact_details)
B5.grid(row=1,column=9)

lab=Label(f1,text="\t\t\t",bg="white")
lab.grid(row=3,column=10)

B6=Button(f1,text="Quit",width=20,height=4,bd=5,font=('arial',10,'bold'),fg="white",bg="red",relief="raised",command=ask_quit)
B6.grid(row=4,column=5)

lab=Label(f1,text="\t",bg="white")
lab.grid(row=3,column=6)


root.mainloop()
