from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
import psycopg2

#applicaion main window

# def one():
#     top = Tk()
# #entering the event main loop
#     top.mainloop()

# #-------------------------------------------------------Python Geometry------------------------------------------------------------------------------
# #-------------------------Tkinter pack()-------(less orginised way to arrange widgets)
# def two():
#     parent =  Tk()
#     redbutton=Button(parent,text="Red",fg="red")
#     redbutton.pack(side=LEFT)
#     greenbutton=Button(parent,text="Green",fg="green")
#     greenbutton.pack(side=RIGHT)
#     blackButton=Button(parent,text="Black",fg="black")
#     blackButton.pack(side=TOP)
#     orangebutton=Button(parent,text="Orange",fg="orange")
#     orangebutton.pack(side=BOTTOM)
#     parent.mainloop()

#-------------------------Tkinter grid()-------(tabular form, can specifiy rows and column)
# def work():
#     messagebox.showinfo("Info","All good")

#global e1,e2,e3,conn


#def three():
#global e1,e2,e3,conn
      

parent = Tk()
h=Label(parent,text="Host").grid(row=0,column=0)
e1=Entry(parent)
e1.grid(row=0,column=1)
d=Label(parent,text="Database").grid(row=1,column=0)
e2=Entry(parent)
e2.grid(row=1,column=1)
u=Label(parent,text="User").grid(row=2,column=0)
e3=Entry(parent)
e3.grid(row=2,column=1)

#a=e1
#b=e2
#c=e3
global params
params=[e1,e2,e3]

def insert_tab():
    global conn
    a=e1.get()
    b=e2.get()
    c=e3.get()
    conn = None

    #global conn
    try:
        conn = psycopg2.connect(host=a,database=b,user=c)
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
        messagebox.showinfo("Alert","Kindly verify the details")
    finally:
        if conn is not None:
            messagebox.showinfo("Info","Database Connected")


def dbop():
    op=Tk()
    cr=Button(op,text="CREATE",command=tab).grid(row=4,column=0)
    ins=Button(op,text="INSERT").grid(row=4,column=2)
    upd=Button(op,text="UPDATE").grid(row=4,column=4)
    de=Button(op,text="DELETE").grid(row=4,column=6)

def tab():
    vin=Tk()
    tb=Button(vin,text="TABLE",command=tab1).grid(row=4,column=1)
    usr=Button(vin,text="USER").grid(row=4,column=3)
    dat=Button(vin,text="DATABASE").grid(row=4,column=5)

def tab1():
    #global params
    #params [b1,b2,b3,b4,b5,b6]
    
    bun=Tk()
    a=int(input("Enter the number of Columns you want to add"))
    
    #a1=Label(bun,text="Table Name").grid(row=i,column=0)
    #b1=Entry(bun)
    #b1.grid(row=0,column=1)
    for i in range (0,a):
        #params=[b1,bi,bi+1]
        ai=Label(bun,text="column"+str(i)).grid(row=i,column=0)
        bi=Entry(bun)
        bi.grid(row=i,column=1)
        def tab2():
            conn = None
            try:
                #conn = psycopg2.connect(host=a,database=b,user=c)
                cur = conn.cursor()
                cur.execute("create table account  values (:bi,:b+1);" )   
                conn.commit()
                cur.close()
            except(Exception,psycopg2.DatabaseError) as error:
                print(error)
                messagebox.showinfo("Alert","Kindly verify the details")
            finally:
                if conn is not None:
                    messagebox.showinfo("Info","Database Connected")
         


    dbop1=Button(bun,text="Submit",command=tab2).grid(row=5,column=1)    
        
submit=Button(parent,text="Submit",command=insert_tab).grid(row=4,column=1)
dbop=Button(parent,text="Databse Operations",command=dbop).grid(row=5,column=1)
parent.mainloop()
parent.distroy()




#----------------------TKinter place()---------(organize widget into specific places)

# def four():
#     parent = Tk()
#     parent.geometry("400x300")
#     host=Label(parent,text="Host").place(x=30,y=50)
#     database=Label(parent,text="Database").place(x=45,y=50)
#     User=Label(parent,text="User").place(x=60,y=50)
#     e1=Entry(parent).place(x=90,y=50)
#     e2=Entry(parent).place(x=90,y=50)
#     e3=Entry(parent).place(x=100,y=50)
#     parent.mainloop()



# if __name__ == "__main__":
#     #one()
#     #two()
#     three()
#     #four()



