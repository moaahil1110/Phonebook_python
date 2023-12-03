from tkinter import *
import datetime

date=datetime.datetime.now()
print(date)
date=date.strftime('%d-%m-%Y')
print(date)

class Phonebook(object):
    def __init__(self,master): 
        self.master=master
        top=Frame(master,height=150, bg='#14635f', bd=8, relief=GROOVE)
        top.pack(fill=X)
        bottom=Frame(master, height=500, bg='skyblue', bd=8, relief=GROOVE)
        bottom.pack(fill=X)
        heading=Label(top, text='PhoneBook App', font='arial 40 bold italic', bg='#14635f', fg='red')
        heading.place(x=70,y=30)
        date1=Label(top, text="Today's date :"+date, font='arial 15 bold', bg='#14635f') 
        date1.place(x=370,y=100)
        self.login_design()
        
        
        def login_design(self):
            f1=Frame(self.bottom,height=340,width=390,bg='red',bd='15',relief=GROOVE)
            f1.place(x=120,y=40)
            f2=Frame(f1,height=300,width=350,bd=8,relief=GROOVE)
            f2.place(x=6,y=6)
            Label(f2,text='Login Page',font='arial 25 bold',fg='blue',).place(x=80,y=10)
            
            Label(f2,text='User Name',font='arial 18 bold').place(x=10,y=90)
            name_e=Entry(f2,bd=3)
            name_e.place(x=150,y=90,height=20,width=170)
            Label(f2,text='Password',font='arial 18 bold').place(x=10,y=150)
            pwd_e=Entry(f2,bd=3)
            pwd_e.place(x=150,y=150,height=28,width=170)
            
            btn1=Button(f2,width=7,text='Login',font='arial 13 bold',bd=4,relief=GROOVE,bg='pink')
            btn1.place(x=140,y=200)
            
            btn2=Button(f2,height=2,width=13,text='Change Password',font='arial 7 bold',bd=4,relief=GROOVE,bg='red',command=self.Change_design)
            btn2.place(x=5,y=250)
        
        
        def Change_design(self):
            f1=Frame(self.bottom,height=340,width=390,bg='red',bd='15',relief=GROOVE)
            f1.place(x=120,y=40)
            f2=Frame(f1,height=300,width=350,bd=8,relief=GROOVE)
            f2.place(x=6,y=6)
            Label(f2,text='Change Password',font='arial 20 bold',fg='blue',).place(x=50,y=10)
            
            Label(f2,text='User Name',font='arial 15 bold').place(x=10,y=70)
            name_e=Entry(f2,bd=3)
            name_e.place(x=170,y=70,height=20,width=150)
            
            Label(f2,text='Old Password',font='arial 15 bold').place(x=10,y=110)
            oldpwd_e=Entry(f2,bd=3)
            oldpwd_e.place(x=170,y=110,height=20,width=150)
            
            Label(f2,text='New Password',font='arial 15 bold').place(x=10,y=150)
            newpwd_e=Entry(f2,bd=3)
            newpwd_e.place(x=170,y=150,height=20,width=150)
            
            btn1=Button(f2,width=7,text='Change',font='arial 13 bold',bd=4,relief=GROOVE,bg='red')
            btn1.place(x=140,y=200)
            
            btn2=Button(f2,height=2,width=13,text='Login',font='arial 7 bold',bd=4,relief=GROOVE,bg='pink',command=self.login_design)
            btn2.place(x=5,y=250)
                
    
     
            
        
def main():
    win = Tk()
    app = Phonebook(win)
    win.title('Phonebookapp') 
    win.geometry('650x570+300+60')
    win.resizable(False,False)
    win.mainloop()
main()    