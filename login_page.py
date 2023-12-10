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
        
        btn2=Button(f2,height=2,width=13,text='Change Password',font='arial 10 bold',bd=4,relief=GROOVE,bg='#fc0303',command=self.Change_design)
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
                
    
    def Change_design(self):
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
    self.title("My contacts")
    self.geometry('1000x690+170+0')
    self.resizable(False,False) 
        
    top=Frame(self, height=150,bg='#03fcfc',bd=8,relief=GROOVE)
    top.pack(fill=X)
    self.bottom=Frame(self,height=500,bg='#0335fc',bd=8,relief=GROOVE)
    self.bottom.pack(fill=X)
    heading=Label(top,text="Our PhoneBook App",font='arial 55 bold',bg='#fc0317',fg='#0335fc')
    heading.place(x=135,y=10)
    date2=Label(top,text="Today's Date :"+date,font='arial 18 bold',bg='#fc0317')
    date2.place(x=670,y=95) 
        
    f1=Frame(self.bottom,height=325,width=220,bg="#027afa",bd=5,relief=GROOVE)
    f1.place(x=7,y=70)
    f2=Frame(f1,height=295,width=190,bd=5,relief=GROOVE)
    f2.place(x=10,y=10)
        
    btn1=Button(f2,text='My Contacts',font='arial 18 bold',bg='#02d9fa',bd=5,relief=GROOVE)
    btn1.place(x=10,y=30)
    btn2=Button(f2,text='Add Contacts',font='arial 18 bold',bg='#02d9fa',bd=5,relief=GROOVE,command=self.add_people)
    btn2.place(x=10,y=110)
    btn3=Button(f2,text='About Us',font='arial 18 bold',bg='#f059e6',bd=5,relief=GROOVE)
    btn3.place(x=10,y=190)
  
  def add_people(self):
      f1=Frame(self.bottom,height=500,width=600,bd=10,relief=GROOVE,bg='#f7f5f6')
      f1.place(x=370,y=10)
      Label(f1,text='Add Contacts Form',font='arial 25 bold',bg='#f7f5f6',fg='#0068fa').place(x=150,y=10) 
      
      fname=Label(f1,text="First Name",font='arial 15 bold',bg='#f7f5f6')
      fname.place(x=85,y=100)
      self.fname_e=Entry(f1,bd=3)
      self.fname_e.place(x=220,y=100,height=35,width=270)
      
      lname=Label(f1,text="Last Name",font='arial 15 bold',bg='#f7f5f6')
      lname.place(x=85,y=160)
      self.lname_e=Entry(f1,bd=3)
      self.lname_e.place(x=220,y=160,height=35,width=270)
      
      email=Label(f1,text="Email",font='arial 15 bold',bg='#f7f5f6')
      email.place(x=85,y=220)
      self.email_e=Entry(f1,bd=3)
      self.email_e.place(x=220,y=220,height=35,width=270)
      
      phone=Label(f1,text="Phone Number",font='arial 15 bold',bg='#f7f5f6')
      phone.place(x=85,y=280)
      self.phone_e=Entry(f1,bd=3)
      self.phone_e.place(x=220,y=280,height=35,width=270)
      
      add=Label(f1,text="Address",font='arial 15 bold',bg='#f7f5f6')
      add.place(x=85,y=340)
      self.add_t=Text(f1,bd=5)
      self.add_t.place(x=220,y=340,height=65,width=270)
      
      addbtn=Button(f1,width=7,text='ADD',bd=5,font='arial 13 bold',bg='#00c0fa')
      addbtn.place(x=250,y=430)                  
  
  
    
def main():
    win = Tk()
    app = Phonebook(win)
    win.title("Phone-Book Application")
    win.geometry('650x570+300+60')
    win.resizable(False,False)
    win.mainloop()

main()    