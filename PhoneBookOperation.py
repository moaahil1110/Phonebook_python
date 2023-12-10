#DISPLAY
def display_selectid(self):
    try:
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        self.person = person.split(".")[0]
        print(self.person)
        self.display()
    except:
        pass    


def display(self):
    r = Tk()
    r.title('Display People')
    r.geometry('410x468+550+200')
    r.resizable(False, False)
    try:
        query = "select * from addpeople where ID={}".format(self.person)
        result = cur.execute(query).fetchone()
        fn = result[1]
        ln = result[2]         
        e = result[3]
        m = result[4]
        add = result[5]
    except:
        pass


    top = Frame(r, height=60, bg='skyblue')
    top.pack(fill=X)

    bottom = Frame(r, height=500, bg='lightgray')
    bottom.pack(fill=X)

    Label(top, text='Display People', font="arial 18 bold", bg='skyblue', fg='blue').place(x=100, y=15)
    fname=Label(bottom, text='First name', font='arial 15 bold', bg='lightgray').place(x=40, y=30)
    lname=Label(bottom, text='Last name', font='arial 15 bold', bg='lightgray').place(x=40, y=70)
    email=Label(bottom, text='Email', font='arial 15 bold', bg='lightgray').place(x=40, y=110)
    mob=Label(bottom, text='Mobile no', font='arial 15 bold', bg='lightgray').place(x=40, y=150)
    address=Label(bottom, text="Address", font="arial 15 bold", bg='lightgray').place(x=40, y=190)

    d_fname=Label(bottom, text=fn, font="arial 15 bold", bg='lightgray').place(x=180, y=30)
    d_lname=Label(bottom, text=ln, font="arial 15 bold", bg='lightgray').place(x=180, y=70)
    d_email=Label(bottom, text=e, font='arial 15 bold', bg='lightgray').place(x=180, y=110)
    d_mob=Label(bottom, text=m, font='arial 15 bold', bg='lightgray').place(x=180, y=150)
    d_address=Label(bottom, text=add, font='arial 15 bold', bg='lightgray').place(x=180, y=190)

#UPDATE
    def update_selectid(self):
        try:
            selected_item = self.listbox.curselection()
            person = self.listbox.get(selected_item)
            self.person = person.split(".")[0]
            self.update()
        except:
            pass

def update(self):
    r2 = Tk()
    r2.title('Update people')
    r2.geometry('410x468+550+200')
    r2.resizable(False, False)

    try:
        query = "select * from addpeople where ID={}".format(self.person)
        result = cur.execute(query).fetchone()
        fn = result[1]
        ln = result[2]
        e = result[3]
        m = result[4]
        add = result[5]
    except:
        pass

    top = Frame(r2, height=60, bg='skyblue')
    top.pack(fill=X)

    self.btm = Frame(r2, height=500, bg='lightgray')
    self.btm.pack(fill=X)

    Label(top, text='Update People', font='arial 18 bold', bg='skyblue', fg='blue').place(x=100, y=15)
    fname=Label(self.btm, text='First name', font='arial 15 bold', bg='lightgray').place(x=40, y=30)
    lname=Label(self.btm, text='Last name', font='arial 15 bold', bg='lightgray').place(x=40, y=70)
    email=Label(self.btm, text='Email', font='arial 15 bold', bg='lightgray').place(x=40, y=110)
    mob=Label(self.btm, text='Mobile no', font='arial 15 bold', bg='lightgray').place(x=40, y=150)
    address=Label(self.btm, text='Address', font='arial 15 bold', bg='lightgray').place(x=40, y=190)

    self.e_fn = Entry(self.btm, width=35, bd=3)
    self.e_fn.insert(1, fn)
    self.e_fn.place(x=160, y=30)

    self.e_ln = Entry(self.btm, width=35, bd=3)
    self.e_ln.insert(1, ln)
    self.e_ln.place(x=160, y=70)

    self.e_e = Entry(self.btm, width=35, bd=3)
    self.e_e.insert(1, e)
    self.e_e.place(x=160, y=110)

    self.e_mob = Entry(self.btm, width=35, bd=3)
    self.e_mob.insert(1, m)
    self.e_mob.place(x=160, y=150)

    self.e_add = Entry(self.btm, width=35, bd=3)
    self.e_add.insert(1, add)
    self.e_add.place(x=160, y=190)

    btn = Button(self.btm, width=9, text='UPDATE', bd=5, bg='skyblue', command=self.update_record)
    btn.place(x=180, y=260)

def update_record(self):
    id = self.person
    fname = self.e_fn.get()
    lname = self.e_ln.get()
    email = self.e_e.get()
    mobile = self.e_mob.get()
    address = self.e_add.get()

    query = "update addpeople set FNAME='{}', LNAME='{}', EMAIL='{}', MOBILE='{}', ADDRESS='{}' where id={}".format(
        fname, lname, email, mobile, address, id
    )

    cur.execute(query)
    conn.commit()

    msg = Label(self.btm, text='Update Successfully.', font='arial 12 bold', bg='lightgray', fg='green')
    msg.place(x=40, y=5)

#DELETING RECORD
    def delete_record(self):
        try:
            selected_item = self.listbox.curselection()
            person = self.listbox.get(selected_item)
            self.person = person.split(".")[0]

            query = "delete from addpeople where id={}".format(self.person)
            cur.execute(query)
            conn.commit()

        except:
            pass