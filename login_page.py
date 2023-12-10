from tkinter import *
import datetime
import sqlite3
from tkinter import messagebox

# Adding Date
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
    # Creation Of Login Page   
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
                
    # Creation Of Change Password Page
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
        
# Creation Of Home Page        
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
        
    btn1=Button(f2,text='My Contacts',font='arial 18 bold',bg='#02d9fa',bd=5,relief=GROOVE,command=self.my_contacts)
    btn1.place(x=10,y=30)
    btn2=Button(f2,text='Add Contacts',font='arial 18 bold',bg='#02d9fa',bd=5,relief=GROOVE,command=self.add_people)
    btn2.place(x=10,y=110)
    btn3=Button(f2,text='About Us',font='arial 18 bold',bg='#f059e6',bd=5,relief=GROOVE)
    btn3.place(x=10,y=190)
  
  def add_people(self):
      self.f1=Frame(self.bottom,height=500,width=600,bd=10,relief=GROOVE,bg='#f7f5f6')
      self.f1.place(x=370,y=10)
      heading=Label(self.f1,text='Add Contacts Form',font='arial 25 bold',bg='#f7f5f6',fg='#0068fa').place(x=150,y=10)
      
     
      # Creation of Add Form
      fname=Label(self.f1,text="First Name",font='arial 15 bold',bg='#f7f5f6')
      fname.place(x=85,y=100)
      self.fname_e=Entry(self.f1,bd=3)
      self.fname_e.place(x=220,y=100,height=35,width=270)
      
      lname=Label(self.f1,text="Last Name",font='arial 15 bold',bg='#f7f5f6')
      lname.place(x=85,y=160)
      self.lname_e=Entry(self.f1,bd=3)
      self.lname_e.place(x=220,y=160,height=35,width=270)
      
      email=Label(self.f1,text="Email",font='arial 15 bold',bg='#f7f5f6')
      email.place(x=85,y=220)
      self.email_e=Entry(self.f1,bd=3)
      self.email_e.place(x=220,y=220,height=35,width=270)
      
      phone=Label(self.f1,text="Phone Number",font='arial 15 bold',bg='#f7f5f6')
      phone.place(x=85,y=280)
      self.phone_e=Entry(self.f1,bd=3)
      self.phone_e.place(x=220,y=280,height=35,width=270)
      
      address=Label(self.f1,text="Address",font='arial 15 bold',bg='#f7f5f6')
      address.place(x=85,y=340)
      self.address_t=Entry(self.f1,bd=5)
      self.address_t.place(x=220,y=340,height=65,width=270)
      
      addbtn=Button(self.f1,width=7,text='ADD',bd=5,font='arial 13 bold',bg='#00c0fa',command=self.add_record)
      addbtn.place(x=250,y=430)                  
  
  def add_record (self):
        fname=self.fname_e.get()
        lname=self.lname_e.get()
        email=self.email_e.get()
        phone=self.phone_e.get()
        address=self.address_t.get()
        print(fname,lname,email,phone,address)

        if fname and lname and email and phone and address !='':
    
            curr.execute('CREATE TABLE IF NOT EXISTS addpeople(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,FNAME TEXT,LNAME TEXT,EMAIL TEXT,PHONE INTEGER,ADDRESS TEXT)')
            curr.execute('INSERT INTO addpeople(FNAME,LNAME,EMAIL,PHONE,ADDRESS) VALUES (?,?,?,?,?)',(fname,lname,email,phone,address))
            conn.commit()
            msg1=Label(self.f1,text="Record added successfully.",font="arial 12 bold",bg='#fcfafa',fg='#04c772')
            msg1.place(x=80,y=60)
        else:
            msg2=Label(self.f1,text="Fill details of person.",font="arial 12 bold",bg='#fcfafa',fg='#ff0818')
            msg2.place(x=80,y=60)

  def my_contacts(self):
        f1=Frame(self.bottom,height=500,width=600)
        f1.place(x=370,y=10)

        f2=Frame(f1,height=70,width=600,bg='#ed02c6',bd=10,relief=GROOVE)
        f2.place(x=0,y=0)

        f3=Frame(f1,height=440,width=600,bg='#ed02c6',bd=10,relief=GROOVE)
        f3.place(x=-1,y=60)

        heading=Label(f2,text='My Contacts Page',font='arial 25 bold',bg='#ed02c6')
        heading.place(x=150,y=5)

        scroll=Scrollbar(f3,orient=VERTICAL)
        listbox=Listbox(f3,width=50,height=26)
        listbox.grid(row=0,column=0,padx=(40,0))
        scroll.config(command=listbox.yview)
        listbox.config(yscrollcommand=scroll.set)
        scroll.grid(row=0,column=1,sticky=NS)

        for i in range(60):
            listbox.insert(END,i)

        btnadd=Button(f3,text='Add',width=8,font='Sans 12 bold')
        btnadd.grid(row=0,column=2,padx=10,pady=10,sticky=N)
        btndisplay=Button(f3,text='Display',width=8,font='Sans 12 bold')
        btndisplay.grid(row=0,column=2,padx=10,pady=30,sticky=N)
        btnupdate=Button(f3,text='Update',width=8,font='Sans 12 bold')
        btnupdate.grid(row=0,column=2,padx=10,pady=60,sticky=N)
        btndelete=Button(f3,text='Delete',width=8,font='Sans 12 bold')
        btndelete.grid(row=0,column=2,padx=10,pady=100,sticky=N)
        
  
    
def main():
    win = Tk()
    app = Phonebook(win)
    win.title("Phone-Book Application")
    win.geometry('650x570+300+60')
    win.resizable(False,False)
    win.mainloop()

main()    