from tkinter import*
import datetime

date=datetime.datetime.now()
print(date)
date=date.strftime('%d-%m-%Y')
print(date)

class Phonebook(object):
    def __init__(self,master): 
        self.master=master
        top=Frame(master,height=150, bg='blue', bg=8, relief=GROOVE)
        top.pack(fill=X)
        bottom=Frame(master, height=500, bg='skyblue', bd=8, relief=GROOVE)
        bottom.pack(fill=X)
        heading=Label(top, text='PhoneBook App', font='arial 40 bold italic', bg='blue', fg='red')
        heading.place(x=70,y=30)
        date1=Label(top, texxt="Today's date :"+date, font='arial 15 bold', bg='blue')
        date1.place(x=370,y=100)
        
def main():
    win = Tk()
    app = Phonebook(win)
    win.title('Phonebookapp') 
    win.geometry('650x570+300+60')
    win.resizable(False,False)
    win.mainloop()
main()    