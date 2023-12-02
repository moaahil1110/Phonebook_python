from tkinter import*
import datetime

date=datetime.datetime.now()
print(date)
date=date.strftime('%d-%m-%Y')
print(date)

class Phonebook(object):
    def __init__(self,master): 
        self.master=master
        top=Frame(master,height=150, bg='blue',bg=8, relief=GROOVE)
        top.pack(fill=X)
        bottom=Frame(master, height=500, bg='skyblue', bd=8, relief=GROOVE)
        bottom.pack(fill=X)
        heading=Label(top, text='PhoneBook App', font='arial 40 bold italic', bg='blue', fg='red')
        heading.place(x=70,y=30)
        date1=Label(top, texxt="Today's date :"+date, font='arial 15 bold', bg='blue')
        date1.place(x=370,y=100)
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
            
            btn1=Button(f2,width=7,text='Login',font='arial 15 bold',bd=4,relief=GROOVE,bg='pink')
            btn1.place(x=140,y=200)
        
def main():
    win = Tk()
    app = Phonebook(win)
    win.title('Phonebookapp') 
    win.geometry('650x570+300+60')
    win.resizable(False,False)
    win.mainloop()
main()    