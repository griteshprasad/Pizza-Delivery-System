from register import *
import tkMessageBox
import sqlite3
from login_page import *
from request_pizza import *
from welcome_in import *


def pizza_menu():

        root=Tk()
        root.geometry("1600x800+0+0")
        root.title("Pizza Delivery system")
        root.configure(bg="white")


        Tops=Frame(root, width=1600, height=50, bg="white")
        Tops.pack(side=TOP)

        f1=Frame(root, width=800, height=700, bg="white")
        f1.pack(side=TOP)


        pizza=['Margherita','Cheese And Tomato Pizza','Spicy Delight','Double Cheese Margherita','Fresh Veggie','Country Special','Farmhouse','5 Papper','Peppy Paneer','Mexican Green Wave','Deluxe Veggie','Gourmet','Cheese And Barbeque Chicken','Chicken Flesta','Barbeque Chicken','Spicy Chicken','Zesty Chicken','Chicken Mexicana','Keema Do Pyaaza','Chicken Golden Delight','Veg Extra Vaganza','Meatzaa','Non Veg Supreme','Cheese And Pepperoni']

        
        conn = sqlite3.connect('pds.db')
        c=conn.cursor()
        #c.execute('create table veg_menu(p1 text,p2 text,p3 text,p4 text,p5 text,p6 text,p7 text,p8 text,p9 text,p10 text,p11 text,p12 text,p13 text,p14 text,p15 text,p16 text,p17 text,p18 text,p19 text,p20 text,p21 text,p22 text,p23 text,p24 text)')
        c.execute("insert into veg_menu values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",pizza)
        conn.commit()
        conn.close()
    

        lblinfo = Label(Tops, font=('arial',50,'bold'), text="PIZZA DELIVERY SYSTEM" , fg="blue",bg="yellow", bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)
        

        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)

        L1 = Label(f1, text="PIZZA LIST",font=('arial',15,'bold'),fg="blue",bg="white")
        L1.grid(row=0,column=1)
        L4 = Label(f1, text="PRICE(in Rs)",font=('arial',15,'bold'),fg="blue",bg="white")
        L4.grid(row=0,column=2)

        L2 = Label(f1, text="VEG [o]",font=('arial',12,'bold'),fg="dark green",bg="white")
        L2.grid(row=1,column=1)
        
        L3 = Label(f1, text="Margherita\nCheese And Tomato Pizza\nSpicy Delight\nDouble Cheese Margherita\nFresh Veggie\nCountry Special\nFarmhouse\n5 Papper\nPeppy Paneer\nMexican Green Wave\nDeluxe Veggie\nGourmet",font=('arial',10),fg="dark green",bg="white")
        L3.grid(row=2,column=1)
        L5 = Label(f1, text="80\n190\n135\n275\n340\n435\n160\n335\n500\n145\n265\n330",font=('arial',10),fg="black",bg="white")
        L5.grid(row=2,column=2)

        L2 = Label(f1, text="NON VEG [o]",font=('arial',12,'bold'),fg="red",bg="white")
        L2.grid(row=3,column=1)

        L3 = Label(f1, text="Cheese And Barbeque Chicken\nChicken Flesta\nBarbeque Chicken\nSpicy Chicken\nZesty Chicken\nChicken Mexicana\nKeema Do Pyaaza\nChicken Golden Delight\nVeg Extra Vaganza\nMeatzaa\nNon Veg Supreme\nCheese And Pepperoni",font=('arial',10),fg="red",bg="white")
        L3.grid(row=4,column=1)
        L5 = Label(f1, text="135\n275\n435\n180\n335\n500\n215\n380\n535\n265\n625\n340",font=('arial',10),fg="black",bg="white")
        L5.grid(row=4,column=2)

        root.mainloop()

if __name__=="__main__":
        login()
