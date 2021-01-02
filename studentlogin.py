from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


def login():
    if userEntry.get()=='' or passEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif userEntry.get()=='vijaya' and passEntry.get()=='1304':
        messagebox.showinfo('success','welcome to login page')
    else:
        messagebox.showerror('Error','Invalid details')





root = Tk()

root.title('Login page of Student Management System')
root.geometry('1280x700+10+10')
root.resizable(0,0)

bgimage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(root,image=bgimage)
bgLabel.pack()

login_frame = Frame(root,bg='white')
login_frame.place(x=400,y=150)

logoimage=PhotoImage(file='student.png')
logolabel=Label(login_frame,image=logoimage,bg='white')
logolabel.grid(row=0,column=0,columnspan=2,pady=20)

userimage=PhotoImage(file='usericon.png')
userlabel=Label(login_frame,text='Username',image=userimage,font=('times new roman',20,'bold'),fg='navy',bg='white',compound=LEFT)
userlabel.grid(row=1,column=0,padx=20,pady=10)

userEntry=Entry(login_frame,font=('arial',15,'bold'),bd=5,relief=GROOVE)
userEntry.grid(row=1,column=1)

passimage=PhotoImage(file='password1.png')
passlabel=Label(login_frame,text='Password',image=passimage,font=('times new roman',20,'bold'),fg='navy',bg='white',compound=LEFT)
passlabel.grid(row=2,column=0,padx=20,pady=10)

passEntry=Entry(login_frame,font=('arial',15,'bold'),bd=5,relief=GROOVE)
passEntry.grid(row=2,column=1,padx=20,pady=10)

loginButton=Button(login_frame,text='Login',width=15,font=('times new roman',15,'bold'),bg='cornflowerblue',
                   fg='white',cursor='hand2',activebackground='cornflowerblue',activeforeground='white',command=login)
loginButton.grid(row=3,column=1,pady=20)







root.mainloop()