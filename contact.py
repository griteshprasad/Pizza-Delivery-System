from register import *
import tkMessageBox
import sqlite3
from login_page import *
from request_pizza import *
from welcome_in import *


def contact_details():

        root=Tk()
        root.geometry("1600x800+0+0")
        root.title("Pizza Delivery system")
        root.configure(bg="white")


        Tops=Frame(root, width=1600, height=50, bg="white")
        Tops.pack(side=TOP)

        f1=Frame(root, width=800, height=700, bg="white")
        f1.pack(side=TOP)
    

        lblinfo = Label(Tops, font=('arial',50,'bold'), text="PIZZA DELIVERY SYSTEM" , fg="blue",bg="yellow", bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)
        

        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)

        L1 = Label(f1, text="Contact Details",font=('arial',25,'bold'),fg="blue",bg="white")
        L1.grid(row=0,column=1)

        L2 = Label(f1, text="Phone : ",font=('arial',15,'bold'),fg="dark green",bg="white")
        L2.grid(row=1,column=1) 
        
       
        L5 = Label(f1, text="6888 6888",font=('arial',15),fg="black",bg="white")
        L5.grid(row=1,column=2)

        L2 = Label(f1, text="Email : ",font=('arial',15,'bold'),fg="red",bg="white")
        L2.grid(row=3,column=1)

        L5 = Label(f1, text="pizzas@india.co.in",font=('arial',15),fg="black",bg="white")
        L5.grid(row=3,column=2)

        L2 = Label(f1, text="Website : ",font=('arial',15,'bold'),fg="blue",bg="white")
        L2.grid(row=5,column=1)

        L5 = Label(f1, text="PizzasIndia.co.in\nIndianPizza.com",font=('arial',15),fg="black",bg="white")
        L5.grid(row=5,column=2)

        root.mainloop()

if __name__=="__main__":
        login()
