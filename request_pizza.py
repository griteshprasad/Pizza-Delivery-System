from Tkinter import *
from tkMessageBox import *
import sqlite3

def order():

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


        lab=Label(f1,text="\n\n\n\n\n\n\n\n",bg="white")
        lab.grid(row=0,column=0)
        L1 = Label(f1, text="Pizza Name :",font=('arial',15,'bold'),fg="blue",bg="white")
        L1.grid(row=2,column=0)
        lab=Label(f1,text="\t",bg="white")
        lab.grid(row=2,column=1)
        E1 = Entry(f1, bd =5,width=40,font=('arial',10,'bold'),relief="groove")
        E1.grid(row=2,column=2)
        
          

        

        def ordered():
                conn =sqlite3.connect('pds.db')
                c=conn.cursor()
                fetch1 =c.execute("SELECT * from veg_menu")
                flag=0
                for row in fetch1:
                        for i in range(0,24):
                                if (row[i] ==E1.get()):
                                      flag=1
                                      break

                if(flag ==1):
                        showinfo('Ordered','Pizza ordered Successfully')
                else:
                        showinfo('Unavailable','Pizza Not Available')

                conn.commit()
                conn.close()

        lab=Label(f1,text="\n\n\n\n",bg="white")
        lab.grid(row=3,column=0)
        B=Button(f1,text=" Order ",width=20,bd=5,font=('arial',10,'bold'),fg="white",bg="green",relief="raised",command=ordered)
        B.grid(row=3,column=2)

        root.mainloop()
