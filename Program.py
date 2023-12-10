from tkinter import *
import datetime
import sqlite3
from tkinter import messagebox


date=datetime.datetime.now()
date=date.strftime('%d-%m-%Y')



conn=sqlite3.connect('phonebook.db')
curr=conn.cursor()

class Phonebook(object):
    def __init__(self,master):
        self.master = master
        top=Frame(master,height=150,bg='#03fcfc',bd=8,relief=GROOVE)
        top.pack(fill=X)
        self.bottom=Frame(master,height=500,bg='#0335fc',bd=8,relief=GROOVE)
        self.bottom.pack(fill=X)
        heading=Label(top,text="Our PhoneBook App",font='arial 40 bold',bg='#fc0317',fg='#0335fc')
        heading.place(x=120,y=30)
        date2=Label(top,text="Today's Date :"+date,font='arial 25 bold',bg='#fc0317')
        date2.place(x=330,y=100)
        self.login_design()
       
    def login_design(self):
        f1=Frame(self.bottom,height=350,width=390,bg='#f403fc',bd=15,relief=GROOVE)
        f1.place(x=110,y=30)
        f2=Frame(f1,height=300,width=350,bd=8,relief=GROOVE)
        f2.place(x=6,y=6)    
        Label(f2,text='Login Page',font='arial 20 bold',fg='#fc0317').place(x=110,y=10)
       
        Label(f2,text='User Name',font='arial 17 bold').place(x=10,y=90)
        self.name_e=Entry(f2,bd=3)
        self.name_e.place(x=150,y=90,height=35,width=170)
        Label(f2,text='Password',font='arial 17 bold').place(x=10,y=150)
        self.pwd_e=Entry(f2,bd=3)
        self.pwd_e.place(x=150,y=150,height=35,width=170) 
        
        btn1=Button(f2,width=7,text='Login',font='arial 15 bold',bd=4,relief=GROOVE,bg='#f403fc',command=Main_page)
        btn1.place(x=140,y=200)
        
        btn2=Button(f2,height=2,width=13,text='Change Password',font='arial 10 bold',bd=4,relief=GROOVE,bg='#fc0303',command=self.change_design)
        btn2.place(x=5,y=230)
    
    def login(self):
        n=self.name_e.get()
        p=self.pwd_e.get()
        result= curr.execute("select * from login").fetchone()
        
        name=result[0]
        pwd=result[1]
        
        if n!='' and p!='':
            if name==n and pwd==p:
             messagebox.showinfo('Success','Login is Successful')
            else:
             messagebox.showerror('Error','Invalid Credentials')
        else:
            messagebox.showinfo('Information','Enter Your Respective Credentials')     
                
    
    def change_design(self):
        f1=Frame(self.bottom,height=350,width=390,bg='#fc0303',bd=15,relief=GROOVE)
        f1.place(x=110,y=30)
        f2=Frame(f1,height=300,width=350,bd=8,relief=GROOVE)
        f2.place(x=6,y=6)    
        Label(f2,text='Change Password',font='arial 20 bold',fg='#fc0317').place(x=50,y=10)
       
        Label(f2,text='User Name',font='arial 15 bold').place(x=10,y=70)
        self.name_e=Entry(f2,bd=3)
        self.name_e.place(x=170,y=70,height=35,width=150)
        
        Label(f2,text='Old Password',font='arial 15 bold').place(x=10,y=110)
        self.oldpwd_e=Entry(f2,bd=3)
        self.oldpwd_e.place(x=170,y=110,height=35,width=150)
        
        Label(f2,text='New Password',font='arial 15 bold').place(x=10,y=150)
        self.newpwd_e=Entry(f2,bd=3)
        self.newpwd_e.place(x=170,y=150,height=35,width=150)
        
        btn1=Button(f2,width=7,text='Change',font='arial 15 bold',bd=4,relief=GROOVE,bg='#f403fc',command=self.change_password)
        btn1.place(x=140,y=200)
        
        btn2=Button(f2,height=2,width=13,text='Login',font='arial 10 bold',bd=4,relief=GROOVE,bg='#fc03eb',command=self.login_design)
        btn2.place(x=5,y=230)
        
    def change_password(self):
         n=self.name_e.get()
         o_p=self.oldpwd_e.get()
         n_p=self.newpwd_e.get()
         
         result= curr.execute("select * from login").fetchone()
        
         name=result[0]
         pwd=result[1]
        
         if n!='' and o_p!='' and n_p!='':
            if name==n and pwd==o_p:
             curr.execute("update login set password=? where name=? and password=?",(n_p,n,o_p))
             conn.commit()
             messagebox.showinfo('Success','Password is successfully changed')
            else:
             messagebox.showerror('Error','Invalid Credentials')
         else:
            messagebox.showinfo('Information','Enter Your Respective Credentials')  
            
class Main_page(Toplevel):
   
   def __init__(self):
      Toplevel.__init__(self)
      self.title("My Contacts")
      self.geometry('1000x690+170+0')
      self.resizable(False,False)
      
      top=Frame(self,height=150,bg='#03fcfc',bd=8,relief=GROOVE)
      top.pack(fill=X)
      self.bottom=Frame(self,height=500,bg='#0335fc',bd=8,relief=GROOVE)
      self.bottom.pack(fill=X)
      heading=Label(top,text="Our PhoneBook App",font='arial 55 bold',bg='#fc0317',fg='#0335fc')
      heading.place(x=70,y=10)
      date2=Label(top,text="Today's Date :"+date,font='arial 18 bold',bg='#fc0317')
      date2.place(x=670,y=95)

      f1=Frame(self.bottom,height=325,width=220,bg='blue',bd=5,relief=GROOVE)
      f1.place(x=60,y=70)
      f2=Frame(f1,height=295,width=190,bd=5,relief=GROOVE)
      f2.place(x=10,y=10)

      btn1=Button(f2,text='My Contacts',width=10,font='arial 18 bold',bg='skyblue',bd=5,relief=GROOVE)
      btn1.place(x=15,y=30)
      btn2=Button(f2,text='Add Contact',width=10,font='arial 18 bold',bg='white',bd=5,relief=GROOVE,command=self.add_contact)
      btn2.place(x=10,y=110)
      btn3=Button(f2,text='About Us',width=10,font='arial 18 bold',bg='pink',bd=5,relief=GROOVE)
      btn3.place(x=10,y=190)
    
    
   def add_contact(self):
    f3=Frame(self.bottom,height=500,width=600,bd=10,relief=GROOVE,bg='white')
    f3.place(x=370,y=10)
    Label(f3,text='Add Contacts Form',font='arial 25 bold',bg='white',fg='blue').place(x=150,y=10)
    fname=Label(f3,text='First Name',font='arial 15 bold',bg='white')
    fname.place(x=80,y=100)
    self.fname=Entry(f3,bd=3)
    self.fname.place(x=220,y=100,height=30,width=290)

    lname=Label(f3,text='Last Name',font='airal 15 bold',bg='white')
    lname.place(x=80,y=160)
    self.lname=Entry(f3,bd=3)
    self.lname.place(x=220,y=160,height=30,width=290)

    email=Label(f3,text='Email',font='airal 15 bold',bg='white')
    email.place(x=80,y=200)
    self.email=Entry(f3,bd=3)
    self.email.place(x=220,y=220,height=30,width=290)
    
    mobile=Label(f3,text='Mobile No.',font='airal 15 bold',bg='white')
    mobile.place(x=80,y=280)
    self.mobile=Entry(f3,bd=3)
    self.mobile.place(x=220,y=280,height=30,width=290)
    
    address=Label(f3,text='Address',font='airal 15 bold',bg='white')
    address.place(x=80,y=340)
    self.address=Text(f3,bd=5)
    self.address.place(x=220,y=340,height=60,width=290)

    btn=Button(f3,width=7,text='ADD',bd=5,font='airal 13 bold',bg='skyblue')
    btn.place(x=250,y=430)
                  
        
        
        

def main():
    win = Tk()
    app = Phonebook(win)
    win.title("Phone-Book Application")
    win.geometry('650x570+300+60')
    win.resizable(False,False)
    win.mainloop()

main()    