from tkinter import *
import ttkthemes
from tkinter import ttk
import time
import pymysql
from tkinter import messagebox,filedialog
import pandas


###############Functionality Part
def slider():
    global count, text
    if count >= len(s):
        count = 0
        text = ''
        sliderLabel.config(text=text)

    else:
        text = text + s[count]  # student
        sliderLabel.config(text=text)  # st
        count += 1  # 2
    sliderLabel.after(300, slider)


def clock():
    timee = time.strftime('%H:%M:%S')
    datee = time.strftime('%d/%m/%Y')
    clockLabel.config(text=f' Date: {datee}\nTime: {timee}')
    clockLabel.after(200, clock)


def connectDatabase():
    def connect():
        global con, mycursor
        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details')
            return
        try:
            strr = 'create database studentable'
            mycursor.execute(strr)

            strr = 'use studentable'
            mycursor.execute(strr)

            strr = 'create table student(id int,name varchar(30),mobile varchar(10),email varchar(30),' \
                   'address varchar(100),gender varchar(30),dob varchar(50),date varchar(50),time varchar(50))'

            mycursor.execute(strr)
            strr = 'alter table student modify column id int not null'
            mycursor.execute(strr)

            strr = 'alter table student modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Information', 'You are now connected with the database', parent=root1)
            addButton.config(state=NORMAL)
            searchButton.config(state=NORMAL)
            updateButton.config(state=NORMAL)
            deleteButton.config(state=NORMAL)
            exportButton.config(state=NORMAL)
            showButton.config(state=NORMAL)


        except:
            strr = 'use studentable'
            mycursor.execute(strr)
            messagebox.showinfo('Information', 'You are now connected with the database', parent=root1)
            addButton.config(state=NORMAL)
            searchButton.config(state=NORMAL)
            updateButton.config(state=NORMAL)
            deleteButton.config(state=NORMAL)
            exportButton.config(state=NORMAL)
            showButton.config(state=NORMAL)
        root1.destroy()

    root1 = Toplevel()
    root1.grab_set()
    root1.geometry('470x250+730+230')
    root1.title('Database Connection')
    root1.resizable(0, 0)
    hostNameLabel = Label(root1, text='Host Name:', font=('arial', 20, 'bold'), fg='red4')
    hostNameLabel.place(x=10, y=10)

    userNameLabel = Label(root1, text='User Name:', font=('arial', 20, 'bold'), fg='red4')
    userNameLabel.place(x=10, y=70)

    passLabel = Label(root1, text='Password:', font=('arial', 20, 'bold'), fg='red4')
    passLabel.place(x=10, y=130)

    hostEntry = Entry(root1, font=('roman', 15, 'bold'))
    hostEntry.place(x=250, y=10)

    userEntry = Entry(root1, font=('roman', 15, 'bold'))
    userEntry.place(x=250, y=70)

    passEntry = Entry(root1, font=('roman', 15, 'bold'))
    passEntry.place(x=250, y=130)

    connectButton = ttk.Button(root1, text='Connect', width=15, command=connect)
    connectButton.place(x=150, y=190)

    root1.mainloop()


def add_window():
    def adddata():
        if identry.get() == '' or nameentry.get() == '' or emailentry.get() == '' or phoneentry.get() == '' \
                or addressentry.get() == '' or genderentry.get() == '' or birthentry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=addroot)

        else:
            addeddate = time.strftime('%d/%m/%Y')
            addedtime = time.strftime('%H:%M:%S')
            try:
                strr = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(strr,
                                 (identry.get(), nameentry.get(), phoneentry.get(), emailentry.get(), addressentry.get()
                                  , genderentry.get(), birthentry.get(), addeddate, addedtime))

                con.commit()

                res = messagebox.askyesno('Question',
                                          f'Id {identry.get()} and Name {nameentry.get()} Added Successfully..'
                                          f'Do You want to clean the form?', parent=addroot)

                if res:
                    identry.delete(0, END)
                    nameentry.delete(0, END)
                    emailentry.delete(0, END)
                    phoneentry.delete(0, END)
                    addressentry.delete(0, END)
                    genderentry.delete(0, END)
                    birthentry.delete(0, END)

                else:
                    pass

            except:
                messagebox.showerror('Error', 'Id already exists,Try another id', parent=addroot)

            strr = 'select * from student'
            mycursor.execute(strr)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in fetched_data:
                listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=listdata)

    addroot = Toplevel()
    addroot.grab_set()
    addroot.geometry('470x520+130+130')
    addroot.title('Add Student')
    addroot.resizable(0, 0)

    idLabel = Label(addroot, text='Id', font=('times new roman', 20, 'bold'), fg='red4')
    idLabel.grid(sticky=W, pady=15, padx=10)

    nameLabel = Label(addroot, text='Name', font=('times new roman', 20, 'bold'), fg='red4')
    nameLabel.grid(row=1, sticky=W, pady=15, padx=10)

    phoneLabel = Label(addroot, text='Phone', font=('times new roman', 20, 'bold'), fg='red4')
    phoneLabel.grid(row=2, sticky=W, pady=15, padx=10)

    emailLabel = Label(addroot, text='Email', font=('times new roman', 20, 'bold'), fg='red4')
    emailLabel.grid(row=3, sticky=W, pady=15, padx=10)

    addressLabel = Label(addroot, text='Address', font=('times new roman', 20, 'bold'), fg='red4')
    addressLabel.grid(row=4, sticky=W, pady=15, padx=10)

    genderLabel = Label(addroot, text='Gender', font=('times new roman', 20, 'bold'), fg='red4')
    genderLabel.grid(row=5, sticky=W, pady=15, padx=10)

    birthLabel = Label(addroot, text='D.O.B', font=('times new roman', 20, 'bold'), fg='red4')
    birthLabel.grid(row=6, sticky=W, pady=15, padx=10)

    identry = Entry(addroot, font=('roman', 15, 'bold'), width=24)
    identry.grid(row=0, column=1, pady=15, padx=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), width=24)
    nameentry.grid(row=1, column=1, pady=15, padx=10)

    phoneentry = Entry(addroot, font=('roman', 15, 'bold'), width=24)
    phoneentry.grid(row=2, column=1, pady=15, padx=10)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), width=24)
    emailentry.grid(row=3, column=1, pady=15, padx=10)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), width=24)
    addressentry.grid(row=4, column=1, pady=15, padx=10)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=5, column=1, pady=15, padx=10)

    birthentry = Entry(addroot, font=('roman', 15, 'bold'), width=24)
    birthentry.grid(row=6, column=1, pady=15, padx=10)

    submitButton = ttk.Button(addroot, text='SUBMIT', width=15, command=adddata)
    submitButton.place(x=125, y=470)

    addroot.mainloop()


def search_window():
    def search():
        addedtime = time.strftime('%H:%M:%S')

        try:
            if identry.get() != '':
                strr = 'select * from student where id=%s'
                mycursor.execute(strr, (identry.get()))
                row = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())

                for i in row:
                    listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=listdata)

            elif nameentry.get() != '':
                strr = 'select * from student where name=%s'
                mycursor.execute(strr, (nameentry.get()))
                row = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())

                for i in row:
                    listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=listdata)

            elif emailentry.get() != '':
                strr = 'select * from student where email=%s'
                mycursor.execute(strr, (emailentry.get()))
                row = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())

                for i in row:
                    listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=listdata)

            elif phoneentry.get() != '':
                strr = 'select * from student where mobile=%s'
                mycursor.execute(strr, (phoneentry.get()))
                row = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())

                for i in row:
                    listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=listdata)

            elif addressentry.get() != '':
                strr = 'select * from student where address=%s'
                mycursor.execute(strr, (addressentry.get()))
                row = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())

                for i in row:
                    listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=listdata)

            elif genderentry.get() != '':
                strr = 'select * from student where gender=%s'
                mycursor.execute(strr, (genderentry.get()))
                row = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())

                for i in row:
                    listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=listdata)

            elif birthentry.get() != '':
                strr = 'select * from student where dob=%s'
                mycursor.execute(strr, (birthentry.get()))
                row = mycursor.fetchall()
                studentTable.delete(*studentTable.get_children())

                for i in row:
                    listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    studentTable.insert('', END, values=listdata)

        except:
            messagebox.showerror('Error', 'Something is Wrong')

    searchroot = Toplevel()
    searchroot.grab_set()
    searchroot.geometry('470x530+130+80')
    searchroot.title('Search Student')
    searchroot.resizable(0, 0)

    idLabel = Label(searchroot, text='Id', font=('times new roman', 20, 'bold'), fg='red4')
    idLabel.grid(sticky=W, pady=15, padx=10)

    nameLabel = Label(searchroot, text='Name', font=('times new roman', 20, 'bold'), fg='red4')
    nameLabel.grid(row=1, sticky=W, pady=15, padx=10)

    phoneLabel = Label(searchroot, text='Phone', font=('times new roman', 20, 'bold'), fg='red4')
    phoneLabel.grid(row=2, sticky=W, pady=15, padx=10)

    emailLabel = Label(searchroot, text='Email', font=('times new roman', 20, 'bold'), fg='red4')
    emailLabel.grid(row=3, sticky=W, pady=15, padx=10)

    addressLabel = Label(searchroot, text='Address', font=('times new roman', 20, 'bold'), fg='red4')
    addressLabel.grid(row=4, sticky=W, pady=15, padx=10)

    genderLabel = Label(searchroot, text='Gender', font=('times new roman', 20, 'bold'), fg='red4')
    genderLabel.grid(row=5, sticky=W, pady=15, padx=10)

    birthLabel = Label(searchroot, text='D.O.B', font=('times new roman', 20, 'bold'), fg='red4')
    birthLabel.grid(row=6, sticky=W, pady=15, padx=10)

    identry = Entry(searchroot, font=('roman', 15, 'bold'), width=24)
    identry.grid(row=0, column=1, pady=15, padx=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), width=24)
    nameentry.grid(row=1, column=1, pady=15, padx=10)

    phoneentry = Entry(searchroot, font=('roman', 15, 'bold'), width=24)
    phoneentry.grid(row=2, column=1, pady=15, padx=10)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), width=24)
    emailentry.grid(row=3, column=1, pady=15, padx=10)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), width=24)
    addressentry.grid(row=4, column=1, pady=15, padx=10)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=5, column=1, pady=15, padx=10)

    birthentry = Entry(searchroot, font=('roman', 15, 'bold'), width=24)
    birthentry.grid(row=6, column=1, pady=15, padx=10)

    submitButton = ttk.Button(searchroot, text='SEARCH', width=15, command=search)
    submitButton.place(x=125, y=480)

    searchroot.mainloop()


def update_window():

    def update():
        if identry.get() == '' or nameentry.get() == '' or emailentry.get() == '' or phoneentry.get() == '' \
                or addressentry.get() == '' or genderentry.get() == '' or birthentry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=updateroot)

        else:
            strr='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
            mycursor.execute(strr,(nameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get()
                                   ,birthentry.get(),dateentry.get(),timeentry.get(),identry.get()))
            con.commit()

            messagebox.showinfo('Information',f'id {identry.get()} modified successfully',parent=updateroot)

            updateroot.destroy()

            strr = 'select * from student'
            mycursor.execute(strr)
            rows = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())

            for i in rows:
                listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert('', END, values=listdata)



    updateroot = Toplevel()
    updateroot.grab_set()
    updateroot.geometry('470x590+130+80')
    updateroot.title('Update Student')
    updateroot.resizable(0, 0)

    idLabel = Label(updateroot, text='Id', font=('times new roman', 20, 'bold'), fg='red4')
    idLabel.grid(sticky=W, pady=12, padx=10)

    nameLabel = Label(updateroot, text='Name', font=('times new roman', 20, 'bold'), fg='red4')
    nameLabel.grid(row=1, sticky=W, pady=12, padx=10)

    phoneLabel = Label(updateroot, text='Phone', font=('times new roman', 20, 'bold'), fg='red4')
    phoneLabel.grid(row=2, sticky=W, pady=12, padx=10)

    emailLabel = Label(updateroot, text='Email', font=('times new roman', 20, 'bold'), fg='red4')
    emailLabel.grid(row=3, sticky=W, pady=12, padx=10)

    addressLabel = Label(updateroot, text='Address', font=('times new roman', 20, 'bold'), fg='red4')
    addressLabel.grid(row=4, sticky=W, pady=12, padx=10)

    genderLabel = Label(updateroot, text='Gender', font=('times new roman', 20, 'bold'), fg='red4')
    genderLabel.grid(row=5, sticky=W, pady=12, padx=10)

    birthLabel = Label(updateroot, text='D.O.B', font=('times new roman', 20, 'bold'), fg='red4')
    birthLabel.grid(row=6, sticky=W, pady=12, padx=10)

    dateLabel = Label(updateroot, text='Date', font=('times new roman', 20, 'bold'), fg='red4')
    dateLabel.grid(row=7, sticky=W, pady=12, padx=10)

    timeLabel = Label(updateroot, text='Time', font=('times new roman', 20, 'bold'), fg='red4')
    timeLabel.grid(row=8, sticky=W, pady=12, padx=10)

    identry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    identry.grid(row=0, column=1, pady=12, padx=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    nameentry.grid(row=1, column=1, pady=12, padx=10)

    phoneentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    phoneentry.grid(row=2, column=1, pady=12, padx=10)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    emailentry.grid(row=3, column=1, pady=12, padx=10)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    addressentry.grid(row=4, column=1, pady=12, padx=10)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=5, column=1, pady=12, padx=10)

    birthentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    birthentry.grid(row=6, column=1, pady=12, padx=10)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    dateentry.grid(row=7, column=1, pady=12, padx=10)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), width=24)
    timeentry.grid(row=8, column=1, pady=12, padx=10)

    submitButton = ttk.Button(updateroot, text='UPDATE', width=15,command=update)
    submitButton.place(x=125, y=550)


    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']

    if len(listdata)!=0:
        identry.insert(END,listdata[0])
        nameentry.insert(END,listdata[1])
        phoneentry.insert(END,listdata[2])
        emailentry.insert(END,listdata[3])
        addressentry.insert(END,listdata[4])
        genderentry.insert(END,listdata[5])
        birthentry.insert(END,listdata[6])
        dateentry.insert(END,listdata[7])
        timeentry.insert(END,listdata[8])




    updateroot.mainloop()


def delete():
    indexing=studentTable.focus()

    content=studentTable.item(indexing)
    gotid=content['values'][0]
    strr='delete from student where id=%s'
    mycursor.execute(strr,gotid)
    con.commit()
    messagebox.showinfo('Information',f'Id {gotid} deleted successfully')

    strr='select * from student'
    mycursor.execute(strr)
    data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in data:
        listdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studentTable.insert('', END, values=listdata)


def showdata():
    strr='select * from student'
    mycursor.execute(strr)
    data=mycursor.fetchall()


    studentTable.delete(*studentTable.get_children())

    for i in data:
        listdata=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],[8]]

        studentTable.insert('',END,values=listdata)


def exportdata():
    url=filedialog.asksaveasfilename()
    data=studentTable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in data:
        content=studentTable.item(i)
        listdata=content['values']
        print(listdata)
        id.append(listdata[0])
        name.append(listdata[1])
        mobile.append(listdata[2])
        email.append(listdata[3])
        address.append(listdata[4])

        gender.append(listdata[5])
        dob.append(listdata[6])

        addedtime.append(listdata[7])
        addedtime.append(listdata[8])


    columnHeading=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']

    print(list(zip(id, name, mobile, email, address, gender, dob, addeddate, addedtime)))
    pandadata=pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, addeddate, addedtime)),
                                  columns=columnHeading)
    paths=r'{}.csv'.format(url)
    pandadata.to_csv(paths,index=False)
    messagebox.showinfo('success',f'Student data is saved{paths}')

def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res:
        root.destroy()

    else:
        pass


############################GUI
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x700+100+10')
root.title('Student Management System')
root.resizable(0, 0)
root.iconbitmap('icon.ico')

leftFrame = Frame(root, bg='whitesmoke')
leftFrame.place(x=10, y=80, width=500, height=600)
textlabel = Label(leftFrame, text='.........WELCOME.........', width=30, font=('arial', 22, 'bold'))
textlabel.grid()
addButton = ttk.Button(leftFrame, text='Add Student', width=25, command=add_window, state=DISABLED)
addButton.grid(row=1, pady=20)

searchButton = ttk.Button(leftFrame, text='Search Student', width=25, command=search_window, state=DISABLED)
searchButton.grid(row=2, pady=20)

deleteButton = ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED,command=delete)
deleteButton.grid(row=3, pady=20)

updateButton = ttk.Button(leftFrame, text='Update Student', width=25, command=update_window, state=DISABLED)
updateButton.grid(row=4, pady=20)

showButton = ttk.Button(leftFrame, text='Show Students', width=25, state=DISABLED,command=showdata)
showButton.grid(row=5, pady=20)

exportButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED,command=exportdata)
exportButton.grid(row=6, pady=20)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=iexit)
exitButton.grid(row=7, pady=20)

rightFrame = Frame(root, bg='red', borderwidth=5, relief=GROOVE)
rightFrame.place(x=550, y=80, width=620, height=600)

style = ttk.Style()
style.configure('Treeview.Heading', font=('castellar', 15, 'bold'), foreground='red4')
style.configure('Treeview', font=('times new roman', 15, 'bold'), foreground='red4')

scrollBarx = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBary = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender',
                                                 'D.O.B', 'Added Date', 'Added Time'),
                            yscrollcommand=scrollBary.set, xscrollcommand=scrollBarx.set)

scrollBarx.pack(side=BOTTOM, fill=X)
scrollBary.pack(side=RIGHT, fill=Y)
scrollBarx.config(command=studentTable.xview)
scrollBary.config(command=studentTable.yview)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile No', text='Mobile No')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')
studentTable.config(show='headings')

studentTable.column('Id', width=100)
studentTable.column('Name', width=200)
studentTable.column('Mobile No', width=200)
studentTable.column('Address', width=300)
studentTable.column('Gender', width=100)
studentTable.column('D.O.B', width=150)
studentTable.column('Added Date', width=200)
studentTable.column('Added Time', width=200)
studentTable.column('Email', width=250)
studentTable.pack(fill=BOTH, expand=1)

s = 'Student Management System'  # s[count]
count = 0
text = ''

sliderLabel = Label(root, text=s, font=('arial', 30, 'italic bold'), width=30)
sliderLabel.place(x=200, y=0)
slider()

clockLabel = Label(root, font=('times new roman', 14, 'bold'), fg='red4')
clockLabel.place(x=0, y=0)
clock()

databaseButton = ttk.Button(root, text='Connect To database', width=18, command=connectDatabase)
databaseButton.place(x=975, y=0)

root.mainloop()
