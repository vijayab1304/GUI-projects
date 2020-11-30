from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import requests

import time


def receipt():
    global recieptRef, dateofOrder
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or \
            var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or \
            var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or \
            var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:
        if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':

            textReceipt.delete(1.0, END)
            x = random.randint(100, 10000)
            recieptRef = 'BILL ' + str(x)
            dateofOrder = time.strftime('%d:%m:%Y')

            textReceipt.insert(END, 'Receipt Ref:\t\t' + recieptRef + '\t\t' + dateofOrder + '\n')
            textReceipt.insert(END, '*********************************************************************\n')
            textReceipt.insert(END, 'Items:\t\t' + '   Cost of Items(in Rs)\n')
            textReceipt.insert(END, '*********************************************************************\n')
            if e_daal.get() != '0':
                textReceipt.insert(END, f'Daal:\t\t\t{int(e_daal.get()) * 60}\n\n')

            if e_roti.get() != '0':
                textReceipt.insert(END, f'Roti:\t\t\t{int(e_roti.get()) * 10}\n\n')

            if e_chawal.get() != '0':
                textReceipt.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 30}\n\n')

            if e_sabji.get() != '0':
                textReceipt.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n\n')

            if e_fish.get() != '0':
                textReceipt.insert(END, f'Fish:\t\t\t{int(e_fish.get()) * 100}\n\n')

            if e_paneer.get() != '0':
                textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 100}\n\n')

            if e_kebab.get() != '0':
                textReceipt.insert(END, f'Kebab:\t\t\t{int(e_kebab.get()) * 40}\n\n')

            if e_chicken.get() != '0':
                textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n\n')

            if e_mutton.get() != '0':
                textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 120}\n\n')

            if e_lassi.get() != '0':
                textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

            if e_coffe.get() != '0':
                textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffe.get()) * 40}\n\n')

            if e_faluda.get() != '0':
                textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n\n')

            if e_shikanji.get() != '0':
                textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 30}\n\n')

            if e_jaljeera.get() != '0':
                textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 40}\n\n')

            if e_roohafza.get() != '0':
                textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 60}\n\n')

            if e_masalachai.get() != '0':
                textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_masalachai.get()) * 20}\n\n')

            if e_badammilk.get() != '0':
                textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_badammilk.get()) * 50}\n\n')

            if e_coldrinks.get() != '0':
                textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n\n')

            if e_oreo.get() != '0':
                textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 400}\n\n')

            if e_apple.get() != '0':
                textReceipt.insert(END, f'Apple:\t\t\t{int(e_apple.get()) * 300}\n\n')

            if e_kitkat.get() != '0':
                textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 500}\n\n')

            if e_banana.get() != '0':
                textReceipt.insert(END, f'Banana:\t\t\t{int(e_banana.get()) * 450}\n\n')

            if e_brownie.get() != '0':
                textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 800}\n\n')

            if e_pineapple.get() != '0':
                textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_pineapple.get()) * 620}\n\n')

            if e_chocolate.get() != '0':
                textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 700}\n\n')

            if e_blackforest.get() != '0':
                textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

            if e_vanilla.get() != '0':
                textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 550}\n\n')

            textReceipt.insert(END, '*********************************************************************\n')
            if costoffoodvar.get() != '0 Rs':
                textReceipt.insert(END, f'Cost of Food:\t\t\t{priceofFood} Rs\n\n')

            if costofdrinksvar.get() != '0 Rs':
                textReceipt.insert(END, f'Cost of Drinks:\t\t\t{priceofDrinks} Rs\n\n')
            if costofcakesvar.get() != '0 Rs':
                textReceipt.insert(END, f'Cost of Cakes:\t\t\t{priceofCakes} Rs\n\n')

            textReceipt.insert(END, f'Sub Total:\t\t\t{priceofFood + priceofDrinks + priceofCakes} Rs\n\n')
            textReceipt.insert(END, f'Service Charge:\t\t\t{50} Rs\n\n')
            textReceipt.insert(END, f'Total:\t\t\t{priceofFood + priceofDrinks + priceofCakes + 50} Rs\n\n')
            textReceipt.insert(END, '*********************************************************************\n')

    else:
        messagebox.showerror('Error', 'No item is selected ')


def save():
    if textReceipt.get(1.0, END) != '\n':
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('Text File', '.txt'), ('All files', '*.*')))
        if url == None:
            return

        bill_data = textReceipt.get(1.0, END)
        url.write(bill_data)
        url.close()

        messagebox.showinfo('Information', 'Your bill is saved successfully')


def send():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        def send_sms(number, message):
            url = 'https://www.fast2sms.com/dev/bulk'

            params = {
                'authorization': 'woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S',
                'message': message,
                'numbers': number,
                'sender_id': 'FSTSMS',
                'route': 'p',
                'language': 'english'
            }
            response = requests.get(url, params=params)

            dic = response.json()
            return dic.get('return')

        def btn_click():
            num = textNumber.get()
            msg = textarea.get(1.0, END)
            r = send_sms(num, msg)
            if r == True:
                messagebox.showinfo('Send Successful', 'Message successfully sent!')

            else:
                messagebox.showerror('Error', 'Something went wrong!')

        global  root2
        root2 = Toplevel()

        root2.title('Send Bill')
        root2.config(bg='red4')
        root2.geometry('485x590+50+50')

        logopic = PhotoImage(file='sender.png')
        label = Label(root2, image=logopic, bg='red4')
        label.pack(pady=5)

        numberLabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        numberLabel.place(x=5, y=150)

        textNumber = Entry(root2, font=('helvetica', 22, 'bold'), bd=5, width=32)
        textNumber.place(x=0, y=185)

        messageLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        messageLabel.place(x=5, y=250)

        sendButton = Button(root2, text='SEND', bd=7, relief=GROOVE, bg='white', fg='black',
                            font=('arial', 19, 'bold'), command=btn_click)
        sendButton.place(x=180, y=520)

        textarea = Text(root2, font=('times new roman', 14, 'bold'), bd=8, relief=GROOVE, width=46, height=9)
        textarea.place(x=4, y=285)

        textarea.insert(END, 'Receipt Ref:\t\t' + recieptRef + '\t\t' + dateofOrder + '\n')
        textarea.insert(END, 'Items:\t\t' + '   Cost of Items(in Rs)\n\n')

        if e_daal.get() != '0':
            textarea.insert(END, f'Daal:\t\t\t{int(e_daal.get()) * 60}\n')

        if e_roti.get() != '0':
            textarea.insert(END, f'Roti:\t\t\t{int(e_roti.get()) * 10}\n')

        if e_chawal.get() != '0':
            textarea.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 30}\n')

        if e_sabji.get() != '0':
            textarea.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n')

        if e_fish.get() != '0':
            textarea.insert(END, f'Fish:\t\t\t{int(e_fish.get()) * 100}\n')

        if e_paneer.get() != '0':
            textarea.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 100}\n')

        if e_kebab.get() != '0':
            textarea.insert(END, f'Kebab:\t\t\t{int(e_kebab.get()) * 40}\n')

        if e_chicken.get() != '0':
            textarea.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n')

        if e_mutton.get() != '0':
            textarea.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 120}\n')

        if e_lassi.get() != '0':
            textarea.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n')

        if e_coffe.get() != '0':
            textarea.insert(END, f'Coffee:\t\t\t{int(e_coffe.get()) * 40}\n')

        if e_faluda.get() != '0':
            textarea.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n')

        if e_shikanji.get() != '0':
            textarea.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 30}\n')

        if e_jaljeera.get() != '0':
            textarea.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 40}\n')

        if e_roohafza.get() != '0':
            textarea.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 60}\n')

        if e_masalachai.get() != '0':
            textarea.insert(END, f'Masala Chai:\t\t\t{int(e_masalachai.get()) * 20}\n')

        if e_badammilk.get() != '0':
            textarea.insert(END, f'Badam Milk:\t\t\t{int(e_badammilk.get()) * 50}\n')

        if e_coldrinks.get() != '0':
            textarea.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n')

        if e_oreo.get() != '0':
            textarea.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 400}\n')

        if e_apple.get() != '0':
            textarea.insert(END, f'Apple:\t\t\t{int(e_apple.get()) * 300}\n')

        if e_kitkat.get() != '0':
            textarea.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 500}\n')

        if e_banana.get() != '0':
            textarea.insert(END, f'Banana:\t\t\t{int(e_banana.get()) * 450}\n')

        if e_brownie.get() != '0':
            textarea.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 800}\n')

        if e_pineapple.get() != '0':
            textarea.insert(END, f'Pineapple:\t\t\t{int(e_pineapple.get()) * 620}\n')

        if e_chocolate.get() != '0':
            textarea.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 700}\n')

        if e_blackforest.get() != '0':
            textarea.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n')

        if e_vanilla.get() != '0':
            textarea.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 550}\n')

        if costoffoodvar.get() != '0 Rs':
            textarea.insert(END, f'\nCost of Food:\t\t\t{priceofFood} Rs\n')

        if costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Drinks:\t\t\t{priceofDrinks} Rs\n')
        if costofcakesvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Cakes:\t\t\t{priceofCakes} Rs\n')

        textarea.insert(END, f'\nSub Total:\t\t\t{priceofFood + priceofDrinks + priceofCakes} Rs\n')
        textarea.insert(END, f'Service Charge:\t\t\t{50} Rs\n')
        textarea.insert(END, f'Total:\t\t\t{priceofFood + priceofDrinks + priceofCakes + 50} Rs\n')
        root2.mainloop()


def reset():
    e_daal.set('0')
    e_roti.set('0')
    e_sabji.set('0')
    e_fish.set('0')
    e_kebab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffe.set('0')
    e_faluda.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalachai.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_kitkat.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    textdaal.config(state=DISABLED)
    textroti.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textchawal.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textmasalachai.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)

    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotal.set('')
    servicecharge.set('')
    totalcost.set('')

    textReceipt.delete(1.0, END)
    root2.destroy()


def CostofItem():
    global priceofDrinks, priceofFood, priceofCakes

    if e_daal.get() == '' or e_roti.get() == '' or e_fish.get() == '' or e_sabji.get() == '' or e_kebab.get() == '' or e_chawal.get() == '' or e_mutton.get() == '' or e_paneer.get() == '' or \
            e_chicken.get() == '' or e_lassi.get() == '' or e_coffe.get() == '' or e_faluda.get() == '' or e_shikanji.get() == '' or e_jaljeera.get() == '' or e_roohafza.get() == '' or e_masalachai.get() == '' or \
            e_badammilk.get() == '' or e_coldrinks.get() == '' or e_oreo.get() == '' or e_apple.get() == '' or e_kitkat.get() == '' or e_vanilla.get() == '' or \
            e_banana.get() == '' or e_brownie.get() == '' or e_pineapple.get() == '' or e_chocolate.get() == '' or e_blackforest.get() == '':
        messagebox.showerror('Error', 'No Quantity is selected')

    else:
        if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or \
                var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or \
                var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or \
                var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
                var26.get() != 0 or var27.get() != 0:

            item1 = int(e_roti.get())
            item2 = int(e_daal.get())
            item3 = int(e_fish.get())
            item4 = int(e_sabji.get())
            item5 = int(e_kebab.get())
            item6 = int(e_chawal.get())
            item7 = int(e_mutton.get())
            item8 = int(e_paneer.get())
            item9 = int(e_chicken.get())

            item10 = int(e_lassi.get())
            item11 = int(e_coffe.get())
            item12 = int(e_faluda.get())
            item13 = int(e_shikanji.get())
            item14 = int(e_jaljeera.get())
            item15 = int(e_roohafza.get())
            item16 = int(e_masalachai.get())
            item17 = int(e_badammilk.get())
            item18 = int(e_coldrinks.get())

            item19 = int(e_oreo.get())
            item20 = int(e_apple.get())
            item21 = int(e_kitkat.get())
            item22 = int(e_vanilla.get())
            item23 = int(e_banana.get())
            item24 = int(e_brownie.get())
            item25 = int(e_pineapple.get())
            item26 = int(e_chocolate.get())
            item27 = int(e_blackforest.get())

            priceofFood = (item1 * 10) + (item2 * 60) + (item3 * 100) + (item4 * 50) + (item5 * 40) + (item6 * 30) + (
                        item7 * 120) + (item8 * 100) + (item9 * 120)
            priceofDrinks = (item10 * 50) + (item11 * 40) + (item12 * 80) + (item13 * 30) + (item14 * 40) + (
                        item15 * 60) + (item16 * 20) + (item17 * 50) + (item18 * 80)
            priceofCakes = (item19 * 400) + (item20 * 300) + (item21 * 500) + (item22 * 550) + (item23 * 450) + (
                        item24 * 800) + (item25 * 620) + (item26 * 700) + (item27 * 550)

            costoffoodvar.set(str(priceofFood) + ' Rs')
            costofdrinksvar.set(str(priceofDrinks) + ' Rs')
            costofcakesvar.set(str(priceofCakes) + ' Rs')

            subtototalofItems = priceofFood + priceofDrinks + priceofCakes
            subtotal.set(str(subtototalofItems) + ' Rs')

            servicecharge.set('50' + ' Rs')

            tc = subtototalofItems + 50

            totalcost.set(str(tc) + ' Rs')

        else:
            messagebox.showerror('Error', 'No item is selected')


def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.focus()
        textroti.delete(0, END)
    elif var1.get() == 0:
        textroti.config(state=DISABLED)
        e_roti.set('0')


def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.focus()
        textdaal.delete(0, END)
    elif var2.get() == 0:
        textdaal.config(state=DISABLED)
        e_daal.set('0')


def fish():
    if var3.get() == 1:
        textfish.config(state=NORMAL)
        textfish.focus()
        textfish.delete(0, END)
    elif var3.get() == 0:
        textfish.config(state=DISABLED)
        e_fish.set('0')


def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kebab():
    if var5.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    elif var5.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.focus()
        textmutton.delete(0, END)
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffe.set('0')


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')


def shikanji():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.focus()
        textshikanji.delete(0, END)
    elif var13.get() == 0:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')


def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.focus()
        textjaljeera.delete(0, END)
    elif var14.get() == 0:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')


def roohafza():
    if var15.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.focus()
        textroohafza.delete(0, END)
    elif var15.get() == 0:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')


def masalachai():
    if var16.get() == 1:
        textmasalachai.config(state=NORMAL)
        textmasalachai.focus()
        textmasalachai.delete(0, END)
    elif var16.get() == 0:
        textmasalachai.config(state=DISABLED)
        e_masalachai.set('0')


def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    elif var17.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)  # e_apple.set('')
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def vanilla():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def banana():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        e_banana.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def pineapple():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')


root = Tk()
root.geometry('1350x710+0+0')
root.resizable(0, 0)
root.title('Restaurant Management System')
root.config(bg='firebrick4')

topFrame = Frame(root, bd=10, relief=RIDGE, pady=5, bg='firebrick4')
topFrame.pack(side=TOP)

labeltitle = Label(topFrame, text='Restaurant Management  System', bd=9, font=('arial', 30, 'bold'), width=54,
                   fg='yellow', bg='red4')
labeltitle.grid(row=0, column=0)
###################################################Frame






menuFrame = Frame(root, bg='firebrick4', bd=10, relief=RIDGE)
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bg='firebrick4', bd=4)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), fg='red4', bg='white', bd=10, relief=RIDGE)
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'), fg='red4', bg='white', bd=10,
                         relief=RIDGE)
drinksFrame.pack(side=LEFT)

cakeFrame = LabelFrame(menuFrame, text='Cakes', font=('arial', 19, 'bold'), fg='red4', bg='white', bd=10, relief=RIDGE)
cakeFrame.pack(side=RIGHT)

receiptcal_frame = Frame(root, bd=15, relief=RIDGE, bg='red4')
receiptcal_frame.pack(side=RIGHT)

calculatorFrame = Frame(receiptcal_frame, bg='red4', bd=1, relief=RIDGE)
calculatorFrame.pack()

recieptFrame = Frame(receiptcal_frame, bg='red4', bd=4, relief=RIDGE)
recieptFrame.pack()

buttonFrame = Frame(receiptcal_frame, bg='red4', bd=3, relief=RIDGE)
buttonFrame.pack()
#####################################Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_daal = StringVar()
e_roti = StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi = StringVar()
e_coffe = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalachai = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()
e_oreo = StringVar()

costoffoodvar = StringVar()
subtotal = StringVar()
totalcost = StringVar()
costofcakesvar = StringVar()
costofdrinksvar = StringVar()
servicecharge = StringVar()

e_daal.set('0')
e_roti.set('0')
e_sabji.set('0')
e_fish.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffe.set('0')
e_faluda.set('0')
e_roohafza.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_masalachai.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_kitkat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

##########################FOOD

roti = Checkbutton(foodFrame, text='Roti', onvalue=1, variable=var1, offvalue=0, font=('arial', 18, 'bold'),
                   bg='white', command=roti).grid(row=0,
                                                  column=0,
                                                  sticky=W)

daal = Checkbutton(foodFrame, text='Daal', variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                   bg='white', command=daal).grid(row=1,
                                                  column=0,
                                                  sticky=W)

fish = Checkbutton(foodFrame, text='Fish', onvalue=1, variable=var3, offvalue=0, font=('arial', 18, 'bold'),
                   bg='white', command=fish).grid(row=2,
                                                  column=0,
                                                  sticky=W)

sabji = Checkbutton(foodFrame, text='Sabji', onvalue=1, variable=var4, offvalue=0, font=('arial', 18, 'bold'),
                    bg='white', command=sabji).grid(row=3,
                                                    column=0,
                                                    sticky=W)

kebab = Checkbutton(foodFrame, text='Kebab', onvalue=1, variable=var5, offvalue=0, font=('arial', 18, 'bold'),
                    bg='white', command=kebab).grid(row=4,
                                                    column=0,
                                                    sticky=W)

chawal = Checkbutton(foodFrame, text='Chawal', onvalue=1, variable=var6, offvalue=0, font=('arial', 18, 'bold'),
                     bg='white', command=chawal).grid(
    row=5, column=0, sticky=W)

mutton = Checkbutton(foodFrame, text='Mutton', onvalue=1, variable=var7, offvalue=0, font=('arial', 18, 'bold'),
                     bg='white', command=mutton).grid(
    row=6, column=0, sticky=W)

paneer = Checkbutton(foodFrame, text='Paneer', onvalue=1, variable=var8, offvalue=0, font=('arial', 18, 'bold'),
                     bg='white', command=paneer).grid(
    row=7, column=0, sticky=W)

chicken = Checkbutton(foodFrame, text='Chicken', onvalue=1, variable=var9, offvalue=0, font=('arial', 18, 'bold'),
                      bg='white', command=chicken).grid(
    row=8, column=0, sticky=W)

########################Food entry

textroti = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, textvariable=e_roti,
                 state=DISABLED)  # textroti.get()
textroti.grid(row=0, column=1)

textdaal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_daal)
textdaal.grid(row=1, column=1)

textfish = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_fish)
textfish.grid(row=2, column=1)

textsabji = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textkebab = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=4, column=1)

textchawal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textmutton = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=8, column=1)

###############DRinks

lassi = Checkbutton(drinksFrame, text='Lassi', onvalue=1, offvalue=0, variable=var10, font=('arial', 18, 'bold'),
                    bg='white', command=lassi).grid(
    row=0, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text='Coffee', onvalue=1, offvalue=0, variable=var11, font=('arial', 18, 'bold'),
                     bg='white', command=coffee).grid(
    row=1, column=0, sticky=W)

faluda = Checkbutton(drinksFrame, text='Faluda', onvalue=1, offvalue=0, variable=var12, font=('arial', 18, 'bold'),
                     bg='white', command=faluda).grid(
    row=2, column=0, sticky=W)

shikanji = Checkbutton(drinksFrame, text='Shikanji', onvalue=1, offvalue=0, variable=var13, font=('arial', 18, 'bold'),
                       bg='white', command=shikanji).grid(row=3, column=0, sticky=W)

jaljeera = Checkbutton(drinksFrame, text='jal-jeera', onvalue=1, offvalue=0, variable=var14, font=('arial', 18, 'bold'),
                       bg='white', command=jaljeera).grid(row=4, column=0, sticky=W)

roohafza = Checkbutton(drinksFrame, text='Roohafza', onvalue=1, offvalue=0, variable=var15, font=('arial', 18, 'bold'),
                       bg='white', command=roohafza).grid(row=5, column=0, sticky=W)

masalachai = Checkbutton(drinksFrame, text='Masala Tea', onvalue=1, offvalue=0, variable=var16,
                         font=('arial', 18, 'bold'),
                         bg='white', command=masalachai).grid(row=6, column=0, sticky=W)

badammilk = Checkbutton(drinksFrame, text='Badam Milk', onvalue=1, offvalue=0, variable=var17,
                        font=('arial', 18, 'bold'),
                        bg='white', command=badammilk).grid(row=7, column=0, sticky=W)

colddrinks = Checkbutton(drinksFrame, text='Cold Drinks', onvalue=1, offvalue=0, variable=var18,
                         font=('arial', 18, 'bold'),
                         bg='white', command=colddrinks).grid(row=8, column=0, sticky=W)

######Entry fields for drinks

textlassi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_coffe)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textshikanji = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_shikanji)
textshikanji.grid(row=3, column=1)

textjaljeera = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_jaljeera)
textjaljeera.grid(row=4, column=1)

textroohafza = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_roohafza)
textroohafza.grid(row=5, column=1)

textmasalachai = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED,
                       textvariable=e_masalachai)
textmasalachai.grid(row=6, column=1)

textbadammilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

###################Cakes
oreocake = Checkbutton(cakeFrame, text='Oreo', onvalue=1, offvalue=0, variable=var19, font=('arial', 18, 'bold'),
                       bg='white', command=oreo).grid(
    row=0, column=0, sticky=W)
applecake = Checkbutton(cakeFrame, text='Apple', onvalue=1, offvalue=0, variable=var20, font=('arial', 18, 'bold'),
                        bg='white', command=apple).grid(
    row=1, column=0, sticky=W)

kitkatecake = Checkbutton(cakeFrame, text='Kitkat', onvalue=1, offvalue=0, variable=var21, font=('arial', 18, 'bold'),
                          bg='white', command=kitkat).grid(
    row=2, column=0, sticky=W)

vanillacake = Checkbutton(cakeFrame, text='Vanilla', onvalue=1, offvalue=0, variable=var22, font=('arial', 18, 'bold'),
                          bg='white', command=vanilla).grid(row=3, column=0, sticky=W)

bananacake = Checkbutton(cakeFrame, text='Banana', onvalue=1, offvalue=0, variable=var23, font=('arial', 18, 'bold'),
                         bg='white', command=banana).grid(
    row=4, column=0, sticky=W)

browniecake = Checkbutton(cakeFrame, text='Brownie', onvalue=1, offvalue=0, variable=var24, font=('arial', 18, 'bold'),
                          bg='white', command=brownie).grid(row=5, column=0, sticky=W)

pineapplecake = Checkbutton(cakeFrame, text='Pineapple', onvalue=1, offvalue=0, variable=var25,
                            font=('arial', 18, 'bold'),
                            bg='white', command=pineapple).grid(row=6, column=0, sticky=W)

chocolatecake = Checkbutton(cakeFrame, text='Chocolate', onvalue=1, offvalue=0, variable=var26,
                            font=('arial', 18, 'bold'),
                            bg='white', command=chocolate).grid(row=7, column=0, sticky=W)
blackforestcake = Checkbutton(cakeFrame, text='Black Forest', onvalue=1, offvalue=0, variable=var27,
                              font=('arial', 18, 'bold'),
                              bg='white', command=blackforest).grid(row=8, column=0, sticky=W)

###################Entry field for cakes

textoreo = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textbanana = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrownie = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=8, width=6, state=DISABLED,
                        textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

######################cost labels

labelCostofdrinks = Label(costFrame, font=('arial', 16, 'bold'), text='Cost of Drinks\t', bg='firebrick4',
                          fg='cornsilk', justify=CENTER)
labelCostofdrinks.grid(row=0, column=0, sticky=W)

textcostofdrinks = Entry(costFrame, font=('arial', 16, 'bold'), textvariable=costofdrinksvar, bd=7, bg='white',
                         width=14, justify=RIGHT,
                         state='readonly')
textcostofdrinks.grid(row=0, column=1)

labelCostofcakes = Label(costFrame, font=('arial', 16, 'bold'), text='Cost of Cakes\t', bg='firebrick4', fg='cornsilk',
                         justify=CENTER)
labelCostofcakes.grid(row=1, column=0, sticky=W)

textcostofcakes = Entry(costFrame, font=('arial', 16, 'bold'), textvariable=costofcakesvar, bd=7, bg='white', width=14,
                        justify=RIGHT,
                        state='readonly')
textcostofcakes.grid(row=1, column=1)

labelCostoffood = Label(costFrame, font=('arial', 16, 'bold'), text='Cost of Food\t', bg='firebrick4', fg='cornsilk',
                        justify=CENTER)
labelCostoffood.grid(row=2, column=0, sticky=W)

textcostoffood = Entry(costFrame, font=('arial', 16, 'bold'), bd=7, bg='white', textvariable=costoffoodvar, width=14,
                       justify=RIGHT,
                       state='readonly')
textcostoffood.grid(row=2, column=1)

labelSubtotal = Label(costFrame, font=('arial', 16, 'bold'), text='   Sub Total\t', bg='firebrick4', fg='cornsilk', )
labelSubtotal.grid(row=0, column=2, sticky=W)

textSubtotal = Entry(costFrame, font=('arial', 16, 'bold'), textvariable=subtotal, bd=7, bg='white', width=14,
                     justify=RIGHT, state='readonly')
textSubtotal.grid(row=0, column=3)

labelServiceCharge = Label(costFrame, font=('arial', 16, 'bold'), text='   Service Charge\t', bg='firebrick4',
                           fg='cornsilk', )
labelServiceCharge.grid(row=1, column=2, sticky=W)

textServiceCharge = Entry(costFrame, font=('arial', 16, 'bold'), textvariable=servicecharge, bd=7, bg='white', width=14,
                          justify=RIGHT,
                          state='readonly')
textServiceCharge.grid(row=1, column=3)

labelTotalCost = Label(costFrame, font=('arial', 16, 'bold'), text='   Total Cost\t', bg='firebrick4', fg='cornsilk', )
labelTotalCost.grid(row=2, column=2, sticky=W)

textTotalCost = Entry(costFrame, font=('arial', 16, 'bold'), textvariable=totalcost, bd=7, bg='white', width=14,
                      justify=RIGHT,
                      state='readonly')
textTotalCost.grid(row=2, column=3)

buttonTotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='red4', padx=16, pady=1,
                     bd=4, width=4, command=CostofItem)
buttonTotal.grid(row=0, column=0)

buttonReciept = Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='red4', padx=16, pady=1,
                       bd=4, width=4, command=receipt)
buttonReciept.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='red4', padx=16, pady=1, bd=4,
                    width=4, command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='red4', padx=16, pady=1, bd=4,
                    width=4, command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', padx=16, pady=1,
                     bd=4, width=4, command=reset)
buttonReset.grid(row=0, column=4)

########################Text Area for receipt

textReceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=4, width=46, height=14)
textReceipt.grid(row=0, column=0)

######################### GUI for Calculator
operator = ''


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)  # 7+58
    textDisplay.delete(0, END)
    textDisplay.insert(END, operator)  # 7+58


def btnClear():
    global operator
    operator = ''
    textDisplay.delete(0, END)


def btnAnswer():
    global operator
    if operator == '':
        pass
    else:
        sumup = str(eval(operator))
        textDisplay.delete(0, END)
        textDisplay.insert(0, sumup)
        operator = ''


textDisplay = Entry(calculatorFrame, width=35, bg='white', bd=4, font=('arial', 16, 'bold'), justify=RIGHT, )
textDisplay.grid(row=0, column=0, columnspan=4, pady=1)
textDisplay.insert(0, '0')

button7 = Button(calculatorFrame, text='7', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                 width=4,
                 command=lambda: btnClick(7))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text='8', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                 width=4
                 , command=lambda: btnClick(8))
button8.grid(row=1, column=1)

butto9 = Button(calculatorFrame, text='9', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4
                , command=lambda: btnClick(9))
butto9.grid(row=1, column=2)

buttonAdd = Button(calculatorFrame, text='+', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                   width=4,
                   command=lambda: btnClick('+'))
buttonAdd.grid(row=1, column=3)

butto4 = Button(calculatorFrame, text='4', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4
                , command=lambda: btnClick(4))
butto4.grid(row=2, column=0)

butto5 = Button(calculatorFrame, text='5', fg='red4', bg='white', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4
                , command=lambda: btnClick(5))
butto5.grid(row=2, column=1)

butto6 = Button(calculatorFrame, text='6', fg='red4', bg='white', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4,
                command=lambda: btnClick(6))
butto6.grid(row=2, column=2)

buttoSub = Button(calculatorFrame, text='-', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                  width=4
                  , command=lambda: btnClick('-'))
buttoSub.grid(row=2, column=3)

butto1 = Button(calculatorFrame, text='1', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4
                , command=lambda: btnClick(1))
butto1.grid(row=3, column=0)

butto2 = Button(calculatorFrame, text='2', fg='red4', bg='white', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4,
                command=lambda: btnClick(2))
butto2.grid(row=3, column=1)

butto3 = Button(calculatorFrame, text='3', fg='red4', bg='white', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4,
                command=lambda: btnClick(3))
butto3.grid(row=3, column=2)

buttomult = Button(calculatorFrame, text='*', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                   width=4,
                   command=lambda: btnClick('*'))
buttomult.grid(row=3, column=3)

buttoAns = Button(calculatorFrame, text='Ans', fg='yellow', bg='red4', bd=7, padx=16, pady=1,
                  font=('arial', 16, 'bold'), width=4
                  , command=btnAnswer)
buttoAns.grid(row=4, column=0)

buttoClear = Button(calculatorFrame, text='Clear', fg='yellow', bg='red4', bd=7, padx=16, pady=1,
                    font=('arial', 16, 'bold'), width=4
                    , command=btnClear)
buttoClear.grid(row=4, column=1)

butto0 = Button(calculatorFrame, text='0', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                width=4
                , command=lambda: btnClick(0))
butto0.grid(row=4, column=2)

buttodiv = Button(calculatorFrame, text='/', fg='yellow', bg='red4', bd=7, padx=16, pady=1, font=('arial', 16, 'bold'),
                  width=4
                  , command=lambda: btnClick('/'))
buttodiv.grid(row=4, column=3)

root.mainloop()
