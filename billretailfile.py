import ttkthemes
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import time
import random
import pyqrcode
import smtplib

rupees = [10000, 5000, 15000, 12000, 14000, 20000, 25000, 11000,
          13000, 16000, 17000, 18000, 19000, 8000, 9000, 21000,
          22000, 23000, 24000, 26000, 27000, 4000, 28000, 29000,
          37000, 36000, 30000, 31000, 32000, 33000, 34000, 35000]
random.shuffle(rupees)

num = random.randint(10, 10000)
billnumber = str(num)

##################Functionality

quantitylist = []


def addtocart():
    global quantitylist
    if productCombobox.get() == 'Select':
        messagebox.showerror('Error', 'No Product Is Selected')
    elif quantityEntry.get() == '':
        messagebox.showerror('Error', 'Select Quantity')
    else:
        billTextarea.grid_remove()
        listboxArea.grid()
        listboxArea.insert(END, productCombobox.get())
        quantitylist.append(quantityEntry.get())


def remove():
    delete = listboxArea.curselection()
    if delete == ():
        messagebox.showerror('Error', 'Nothing To Remove')

    else:
        listboxArea.delete(delete)
        for item in delete:
            quantitylist.pop(item)


def clearAll():
    listboxArea.delete(0, END)
    quantityEntry.delete(0, END)
    selectCategoryCombobox.set('Select')
    selectSubCategoryCombobox.set('Select')
    productCombobox.set('Select')
    selectSubCategoryCombobox.config(state=DISABLED)
    productCombobox.config(state=DISABLED)


def generate():
    global sumup,qrimage,l,s
    if customernameEntry.get() == '' or contactEntry.get() == '' or emailEntry.get() == '':
        messagebox.showerror('Error', 'Please enter customer details')

    else:
        listboxArea.grid_remove()
        l = listboxArea.get(0, END)
        print(l)
        billTextarea.grid()

        billTextarea.delete(1.0, END)
        billTextarea.insert(END, '\t\t** Welcome To General Bazaar **\n\n')
        billTextarea.insert(END, f'Customer Name:\t{customernameEntry.get()}\t\t\t\tPhone No:\t{contactEntry.get()}\n\n'
                                 f'Email Id:\t{emailEntry.get()}\t\t\t\tDate:\t{time.strftime("%d/%m/%Y")}\n')

        billTextarea.insert(END, f'===========================================================\n')
        billTextarea.insert(END, f'Products\t\t\tQuantity\t\t\tPrice (in Rs)\n')
        billTextarea.insert(END, f'===========================================================\n')
        sumup = 0
        for item in range(len(l)):
            billTextarea.insert(END, f'{l[item]}\t\t\t{quantitylist[item]}\t\t\t{rupees[0]}\n')
            sumup = sumup + rupees[0]
            random.shuffle(rupees)

        billTextarea.insert(END,
                            f'----------------------------------------------------------------------------------------------------------\n\n')
        billTextarea.insert(END, f'Total Products:\t\t{len(l)}\n')
        s = 0
        for plus in quantitylist:  # [1,4,6]
            s = s + int(plus)  # 11

        billTextarea.insert(END, f'Total Quantity:\t\t{s}\n')
        billTextarea.insert(END, f'Total Price:\t\t{sumup} Rs\n')
        billTextarea.insert(END,
                            f'----------------------------------------------------------------------------------------------------------\n\n')

        qrcode()
        qrimage=PhotoImage(file='vijaya.png')
        qrcodeFrame.place(x=365, y=175)
        qrLabel.config(image=qrimage)





def qrcode():
    billnumber=random.randint(100,10000)
    message = f'GENERAL BAZAAR (FUTURE RETAIL LTD)\nOWNER- VIJAYA\nCONTACT- +917569771559\n\nCustomer:-Bill No:{billnumber}\n' \
              f'Name:{customernameEntry.get()}\nEmail id:{emailEntry.get()}\nContact:{contactEntry.get()}\nBill Amount:{sumup} Rs'

    qr=pyqrcode.create(message)
    qr.png('vijaya.png',scale=3)


def save():
    if billTextarea.get(1.0, END) == '\n':
        pass

    else:

        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('Text File', '.txt'), ('All Files', '*.*')))

        if url == None:
            return
        bill_data = billTextarea.get(1.0, END)
        url.write(bill_data)
        url.close()


def email():
    if billTextarea.get(1.0, END) == '\n':
        pass
    else:

        def send_email():
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(gmailidEntry.get(), passwordEntry.get())
            subject = subjectEntry.get()
            body = messageText.get(1.0, END)
            message = f'{subject}\n\n{body}'

            listofAddress = [customeridEntry.get()]
            ob.sendmail(gmailidEntry.get(), listofAddress, message)
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root2)
            res = messagebox.askyesno('information', 'Do you want to clear the fields?', parent=root2)
            if res:
                messageText.delete(1.0, END)
                subjectEntry.delete(0, END)
                customeridEntry.delete(0, END)
                gmailidEntry.delete(0, END)
                passwordEntry.delete(0, END)

            else:
                pass

            ob.close()

        root2 = Toplevel()
        root2.geometry('600x720+100+0')
        root2.title('Send Gmail')
        root2.config(bg='sienna3')
        root2.resizable(0, 0)

        gmailFrame = Frame(root2, width=570, height=690)
        gmailFrame.place(x=15, y=15)

        fromLabel = Label(gmailFrame, text='From,', font=('arial', 22, 'bold'), fg='sienna3')
        fromLabel.place(x=5, y=5)

        gmailidLabel = Label(gmailFrame, text='Gmail Id', font=('arial', 20, 'bold'), fg='sienna3')
        gmailidLabel.place(x=80, y=45)

        passwordLabel = Label(gmailFrame, text='Password', font=('arial', 20, 'bold'), fg='sienna3')
        passwordLabel.place(x=80, y=105)

        gmailidEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), bd=5, relief=RIDGE, width=23)
        passwordEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), bd=5, relief=RIDGE, width=23)

        gmailidEntry.place(x=240, y=40)
        passwordEntry.place(x=240, y=100,show='*')

        tolabel = Label(gmailFrame, text='To,', font=('arial', 22, 'bold'), fg='sienna3')
        tolabel.place(x=5, y=170)

        customerIdLabel = Label(gmailFrame, text='Gmail Id', font=('arial', 20, 'bold'), fg='sienna3')
        customerIdLabel.place(x=80, y=210)

        subjectLabel = Label(gmailFrame, text='Subject', font=('arial', 20, 'bold'), fg='sienna3')
        subjectLabel.place(x=80, y=270)

        customeridEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), bd=5, relief=RIDGE, width=23)
        subjectEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), bd=5, relief=RIDGE, width=23)

        customeridEntry.place(x=240, y=205)
        subjectEntry.place(x=240, y=265)

        customeridEntry.insert(END, emailEntry.get())
        subjectEntry.insert(END, 'GENERAL BAZAAR BILL')

        messageLabel = Label(gmailFrame, text='Bill', font=('arial', 20, 'bold'), fg='sienna3')
        messageLabel.place(x=5, y=310)

        messageText = Text(gmailFrame, font=('arial', 15, 'bold'), bd=5, relief=SUNKEN, width=49, height=11)
        messageText.place(x=10, y=350)

        sendButton = Button(gmailFrame, text='SEND', font=('arial', 15, 'bold'), bg='sienna3', fg='white', command=send_email)
        sendButton.place(x=485, y=640)

        messageText.insert(END, '\t*** Welcome To General Bazaar ***\n\n')
        messageText.insert(END, f'\tCustomer Name:\t{customernameEntry.get()}\n\tPhone No:\t{contactEntry.get()}\n\t'
                                f'Email Id:\t{emailEntry.get()}\n\tDate:\t{time.strftime("%d/%m/%Y")}\n\n')

        messageText.insert(END, f'Total Products:\t{len(l)}\n')
        messageText.insert(END, f'Total Quantity:\t{s}\n')
        messageText.insert(END, f'Total Price:\t{sumup}\n')


def clear():
    billTextarea.delete(1.0, END)
    customernameEntry.delete(0, END)
    contactEntry.delete(0, END)
    emailEntry.delete(0, END)

    qrcodeFrame.place_forget()


def search_bill():
    url = filedialog.askopenfilename(defaultextension='.txt', filetypes=(('Text File', '.txt'), ('All Files', '*.*')))
    if url == None:
        return
    f1 = open(url, 'r')
    billTextarea.delete(1.0, END)
    for d in f1:
        billTextarea.insert(END, d)

    f1.close()


def product_selection(event):
    def func1(event):
        if selectSubCategoryCombobox.get() == 'Laptops':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Hp', 'Dell', 'Lenovo')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

        elif selectSubCategoryCombobox.get() == 'Headphones & Speakers':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('JBL', 'Skullcandy', 'Sony')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

        elif selectSubCategoryCombobox.get() == 'Mobiles':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Samsung', 'Oppo', 'Vivo')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

    def func2(event):
        if selectSubCategoryCombobox.get() == 'Footwear':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Sports Shoes', 'Casual Shoes', 'Formal Shoes')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

        elif selectSubCategoryCombobox.get() == 'Clothing':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Tshirts', 'Shirts', 'Innerwear')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

        elif selectSubCategoryCombobox.get() == 'Watches':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Casio', 'Fossil', 'Titan')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

    def func3(event):
        if selectSubCategoryCombobox.get() == 'Bedroom Furniture':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Bed', 'Mattress', 'Wardrobe')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

        elif selectSubCategoryCombobox.get() == 'Living & Dining Room Furniture':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Sofas', 'Recliners', 'Dining Table Set')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

        elif selectSubCategoryCombobox.get() == 'Kids Furniture':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Bean Bag', 'Stool', 'Study Table')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

    def func4(event):
        if selectSubCategoryCombobox.get() == 'Televisions':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Realme Smart TV', 'Nokia 4K UHD TV', 'LG Smart TV')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')


        elif selectSubCategoryCombobox.get() == 'Washing Machines':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Onida 6.2kg', 'Whirlpool 7kg', 'LG 8kg')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')


        elif selectSubCategoryCombobox.get() == 'Refrigerators':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Whirlpool 3Star', 'Samsung 2Star', 'LG 3Star')
            quantityEntry.config(state=NORMAL)
            productCombobox.set('Select')

    if selectCategoryCombobox.get() == 'Electronics':
        selectSubCategoryCombobox.config(state=NORMAL)
        selectSubCategoryCombobox.config(state='readonly')
        selectSubCategoryCombobox['values'] = ('Laptops', 'Headphones & Speakers', 'Mobiles',)
        selectSubCategoryCombobox.bind('<<ComboboxSelected>>', func1)
        selectSubCategoryCombobox.set('Select')
        productCombobox.set('Select')

    elif selectCategoryCombobox.get() == 'Fashion':
        selectSubCategoryCombobox.config(state=NORMAL)
        selectSubCategoryCombobox.config(state='readonly')
        selectSubCategoryCombobox['values'] = ('Footwear', 'Clothing', 'Watches',)
        selectSubCategoryCombobox.bind('<<ComboboxSelected>>', func2)
        selectSubCategoryCombobox.set('Select')
        productCombobox.set('Select')

    elif selectCategoryCombobox.get() == 'Home & Furniture':
        selectSubCategoryCombobox.config(state=NORMAL)
        selectSubCategoryCombobox.config(state='readonly')
        selectSubCategoryCombobox['values'] = ('Bedroom Furniture', 'Living & Dining Room Furniture', 'Kids Furniture',)
        selectSubCategoryCombobox.bind('<<ComboboxSelected>>', func3)
        selectSubCategoryCombobox.set('Select')
        productCombobox.set('Select')



    elif selectCategoryCombobox.get() == 'Tvs & Appliances':
        selectSubCategoryCombobox.config(state=NORMAL)
        selectSubCategoryCombobox.config(state='readonly')
        selectSubCategoryCombobox['values'] = ('Televisions', 'Washing Machines', 'Refrigerators',)
        selectSubCategoryCombobox.bind('<<ComboboxSelected>>', func4)
        selectSubCategoryCombobox.set('Select')
        productCombobox.set('Select')


operator = ''


def calculator():
    def btnClick(number):
        global operator
        operator = operator + str(number)
        text_input.set(operator)

    def clear():
        global operator
        operator = ''
        text_input.set('')

    def answer():
        global operator
        sumup = eval(operator)
        text_input.set(sumup)
        operator = ''

    text_input = StringVar()
    textDisplay = Entry(calculatorFrame, width=21, bg='white', bd=3, textvariable=text_input,
                        font=('arial', 14, 'bold'), justify=CENTER)
    textDisplay.grid(row=0, column=0, columnspan=4, pady=10)
    textDisplay.insert(0, '0')

    button7 = ttk.Button(calculatorFrame, width='4', text='7', command=lambda: btnClick(7))
    button7.grid(row=1, column=0)

    button8 = ttk.Button(calculatorFrame, width='4', text='8', command=lambda: btnClick(8))
    button8.grid(row=1, column=1)

    button9 = ttk.Button(calculatorFrame, width='4', text='9', command=lambda: btnClick(9))
    button9.grid(row=1, column=2)

    buttonAdd = ttk.Button(calculatorFrame, width='4', text='+', command=lambda: btnClick('+'))
    buttonAdd.grid(row=1, column=3)

    button4 = ttk.Button(calculatorFrame, width='4', text='4', command=lambda: btnClick(4))
    button4.grid(row=2, column=0)

    button5 = ttk.Button(calculatorFrame, width='4', text='5', command=lambda: btnClick(5))
    button5.grid(row=2, column=1)

    button6 = ttk.Button(calculatorFrame, width='4', text='6', command=lambda: btnClick(6))
    button6.grid(row=2, column=2)

    buttonSub = ttk.Button(calculatorFrame, width='4', text='-', command=lambda: btnClick('-'))
    buttonSub.grid(row=2, column=3)

    button1 = ttk.Button(calculatorFrame, width='4', text='1', command=lambda: btnClick(1))
    button1.grid(row=3, column=0)

    button2 = ttk.Button(calculatorFrame, width='4', text='2', command=lambda: btnClick(2))
    button2.grid(row=3, column=1)

    button3 = ttk.Button(calculatorFrame, width='4', text='3', command=lambda: btnClick(3))
    button3.grid(row=3, column=2)

    buttonMult = ttk.Button(calculatorFrame, width='4', text='*', command=lambda: btnClick('*'))
    buttonMult.grid(row=3, column=3)

    buttonEqual = ttk.Button(calculatorFrame, width='4', text='=', command=answer)
    buttonEqual.grid(row=4, column=0)

    buttonDel = ttk.Button(calculatorFrame, width='4', text='Del', command=clear)
    buttonDel.grid(row=4, column=1)

    button0 = ttk.Button(calculatorFrame, width='4', text='0', command=lambda: btnClick(0))
    button0.grid(row=4, column=2)

    buttonDiv = ttk.Button(calculatorFrame, width='4', text='/', command=lambda: btnClick('/'))
    buttonDiv.grid(row=4, column=3)


def timer():
    current_time = time.strftime('%H:%M:%S')
    timeLabel.config(text=current_time)
    timeLabel.after(20, timer)


def logout():
    root.destroy()
    import signin


###################GUI
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('itft1')

root.geometry('1350x720+0+0')
root.config(bg='sienna3')
root.title('Retail System')

mainframe = Frame(root, width=1320, height=690)
mainframe.place(x=15, y=15)

titleLabel = Label(mainframe, text='Retail System', font=('arial', 40, 'bold'), fg='sienna3')
titleLabel.place(x=510, y=10)

timeLabel = Label(mainframe, font=('chillar', 18, 'bold'), )
timeLabel.place(x=1200, y=25)
timer()

logoutButton = ttk.Button(mainframe, text='Logout', command=logout)
logoutButton.place(x=15, y=5)

searchbutton = ttk.Button(mainframe, text='Search Bill', command=search_bill)
searchbutton.place(x=5, y=45)

customerFrame = LabelFrame(mainframe, text='Customer Details', font=('times new roman', 20, 'bold'), bd=10)
customerFrame.place(x=5, y=80)

customernameLabel = Label(customerFrame, text='Customer Name\t', font=('times new roman', 16, 'bold'))
customernameLabel.grid(row=0, column=0)

customernameEntry = Entry(customerFrame, font=('times new roman', 14, 'bold'), width=25, bd=5, relief=GROOVE)
customernameEntry.grid(row=0, column=1, padx=20)

emailLabel = Label(customerFrame, text='Email Id', font=('times new roman', 16, 'bold'))
emailLabel.grid(row=0, column=2)

emailEntry = Entry(customerFrame, font=('times new roman', 14, 'bold'), width=25, bd=5, relief=GROOVE)
emailEntry.grid(row=0, column=3, padx=20)

contactLabel = Label(customerFrame, text='Contact Number', font=('times new roman', 16, 'bold'))
contactLabel.grid(row=0, column=4)

contactEntry = Entry(customerFrame, font=('times new roman', 14, 'bold'), width=23, bd=5, relief=GROOVE)
contactEntry.grid(row=0, column=5, padx=18)

leftFrame = LabelFrame(mainframe, text='Products', font=('times new roman', 20, 'bold'), fg='sienna3', bd=10)
leftFrame.place(x=5, y=160)

selectcategoryLabel = Label(leftFrame, text='Select Category', font=('times new roman', 16, 'bold'))
selectcategoryLabel.grid(row=0, column=0, sticky=W, pady=5)

selectCategoryCombobox = ttk.Combobox(leftFrame, font=('times new roman', 14, 'bold'), state='readonly', width=30)
selectCategoryCombobox['values'] = (
    'Electronics', 'Fashion', 'Home & Furniture', 'Tvs & Appliances')
selectCategoryCombobox.grid(row=1, column=0)
selectCategoryCombobox.set('Select')

selectsubcategoryLabel = Label(leftFrame, text='Sub Category', font=('times new roman', 16, 'bold'))
selectsubcategoryLabel.grid(row=2, column=0, sticky=W, pady=5)

selectSubCategoryCombobox = ttk.Combobox(leftFrame, font=('times new roman', 14, 'bold'), state=DISABLED, width=30)
selectSubCategoryCombobox.grid(row=3, column=0)

productLabel = Label(leftFrame, text='Product', font=('times new roman', 16, 'bold'))
productLabel.grid(row=4, column=0, sticky=W, pady=5)

productCombobox = ttk.Combobox(leftFrame, font=('times new roman', 14, 'bold'), state=DISABLED, width=30)
productCombobox.grid(row=5, column=0)

quantityLabel = Label(leftFrame, text='Quantity', font=('times new roman', 16, 'bold'))
quantityLabel.grid(row=6, column=0, sticky=W, pady=5)
quantityEntry = Entry(leftFrame, font=('times new roman', 14, 'bold'), state=DISABLED, bd=5, relief=GROOVE, width=30)
quantityEntry.grid(row=7, column=0, padx=10)

addtocartButton = ttk.Button(leftFrame, text='Add To Cart', command=addtocart)
addtocartButton.grid(row=8, column=0, pady=20, sticky=W, padx=30)

removeButton = ttk.Button(leftFrame, text='Remove', command=remove)
removeButton.place(x=140, y=298)

clearAllButton = ttk.Button(leftFrame, text='Clear All', command=clearAll)
clearAllButton.place(x=230, y=298)

bottomFrame = LabelFrame(mainframe, text='Bill Options', font=('times new roman', 20, 'bold'), fg='sienna3', bd=10)
bottomFrame.place(x=5, y=555, width=350)

generateButton = ttk.Button(bottomFrame, text='Generate', command=generate)
generateButton.grid(row=0, column=0, padx=15, pady=26)

saveButton = ttk.Button(bottomFrame, text='Save', command=save)
saveButton.place(x=115, y=26)

emailButton = ttk.Button(bottomFrame, text='Email', command=email)
emailButton.place(x=190, y=26)

clearButton = ttk.Button(bottomFrame, text='Clear', command=clear)
clearButton.place(x=270, y=26)

calculatorFrame = LabelFrame(mainframe, text='Calculator', font=('times new roman', 20, 'bold'), fg='sienna3', bd=10)
calculatorFrame.place(x=365, y=460)
calculator()

billareaFrame = LabelFrame(mainframe, text='Bill Details', font=('times new roman', 20, 'bold'), fg='sienna3', bd=10)
billareaFrame.place(x=630, y=160)

shopnameLabel = Label(billareaFrame,
                      text='GENERAL BAZAAR (FUTURE RETAIL LTD)\nHYDERABAD -500060\nEMAIL: vijaya@gmail.com\n'
                           'MOBILE NO: 7569771559\nTEL NO: 055-76876489\nHELPLINE:'
                           '1800-102-1800\n', font=('arial', 10, 'bold'))
shopnameLabel.grid(row=0, column=0)

scroll_y = Scrollbar(billareaFrame, orient=VERTICAL)
billTextarea = Text(billareaFrame, font=('times new roman', 14, 'bold'), width=65, height=17)
scroll_y.grid(row=1, column=1)
scroll_y.config(command=billTextarea.yview)
billTextarea.grid(row=1, column=0)

listboxArea = Listbox(billareaFrame, font=('times new roman', 14, 'bold'), width=65, height=17, justify=CENTER)
listboxArea.grid(row=1, column=0)
listboxArea.grid_remove()

qrcodeFrame = LabelFrame(mainframe,text='QR Code',font=('times new roman', 20, 'bold'), fg='sienna3', bd=10)
qrcodeFrame.place(x=365, y=175)
qrcodeFrame.place_forget()


qrLabel = Label(qrcodeFrame)
qrLabel.grid(row=0, column=0)

selectCategoryCombobox.bind('<<ComboboxSelected>>', product_selection)

root.mainloop()
