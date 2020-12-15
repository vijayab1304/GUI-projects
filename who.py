from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer

mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play(-1)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

questions = ["'.MOV' extension refers usually to what kind of file?",
             "The gas usually filled in the electric bulb is ",
             "The members of the panchayat are ",
             "Which of these formulae is used to calculate the area of a rectangular agriculture field?",
             "Which one of these festivals is celebrated during winter in India?",
             "Who was known as Iron man of India? ",
             "The traditional attire 'pheta' is worn on which part of the body ?",
             "Aurobindo was the author of",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             " Which city is known as 'Electronic City of India'?",
             "The death anniversary of which of the following leaders is observed as Martyrs Day?",
             "Rabindranath Tagore's 'Jana Gana Mana' has been adopted as India's National Anthem. How many stanzas of the said song were adopted?",
             "Which cricketer has most number of international centuries?",
             "The office of the UN General Assembly is in"]

first_option = [" Image file ", " nitrogen ",
                " nominated by the district officer ", "breadth-length",
                "Baisakhi", " Govind Ballabh Pant ",
                "Arm", " Discovery of India ", "11:23PM", "KKR",
                "Chennai", "Smt. Indira Gandhi",
                " Only the first stanza ", "Ricky Ponting", " Vienna "]

second_option = [" Animation/movie file ", " hydrogen ",
                 " the electorates of the respective territorial constituencies ", "length + breadth ",
                 "Makar Sankranti", " Jawaharlal Nehru ",
                 "Head", " Hindu view of life ", "11.11PM", "CSK",
                 " Hyderabad ", "Pt. jawaharlal Nehru",
                 " The whole song ",
                 "Virat Kohli", " New York "]

third_option = [" Audio file ", " carbon dioxide ",
                " nominated by local self-government minister of the state ", "length * breadth",
                "Naag Panchami", " Subhash Chandra Bose ",
                "Waist", " Yogashastra ", "7:23PM", "MI",
                " Guragon ", "Mahatma Gandhi",
                " Third and Fourth stanza ",
                "Rohit Sharma", " Paris "]

fourth_option = [" MS Office document ", " oxygen ",
                 "nominated by the block development organization", "breadth/length",
                 "Ganesh Chaturthi", " Sardar Vallabhbhai Patel ",
                 "Chest", " Savitri ", "9.11PM", "RCB",
                 " Bangalore ",
                 "Bhagat Singh",
                 " First and Second stanza ", "Sachin Tendulkar",
                 " Zurich "]


def select(event):
    mixer.music.set_volume(1)
    b = event.widget
    value = b['text']

    callButton.config(image='')
    progressbarLabel.place_forget()
    progressvolumeLabel.place_forget()

    progressbarLabel1.place_forget()
    progressvolumeLabel1.place_forget()

    progressbarLabel2.place_forget()
    progressvolumeLabel2.place_forget()

    progressbarLabel3.place_forget()
    progressvolumeLabel3.place_forget()

    if value == ' Animation/movie file ':  # 1
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[1])

        textQuestion1Button.config(text=first_option[1])
        textQuestion2Button.config(text=second_option[1])
        textQuestion3Button.config(text=third_option[1])
        textQuestion4Button.config(text=fourth_option[1])
        amountlabel.config(image=image1)

    elif value == ' nitrogen ':  # 2
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[2])

        textQuestion1Button.config(text=first_option[2])
        textQuestion2Button.config(text=second_option[2])
        textQuestion3Button.config(text=third_option[2])
        textQuestion4Button.config(text=fourth_option[2])
        amountlabel.config(image=image2)


    elif value == ' the electorates of the respective territorial constituencies ':  # 3
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[3])

        textQuestion1Button.config(text=first_option[3])
        textQuestion2Button.config(text=second_option[3])
        textQuestion3Button.config(text=third_option[3])
        textQuestion4Button.config(text=fourth_option[3])
        amountlabel.config(image=image3)



    elif value == 'length * breadth':  # 4
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[4])

        textQuestion1Button.config(text=first_option[4])
        textQuestion2Button.config(text=second_option[4])
        textQuestion3Button.config(text=third_option[4])
        textQuestion4Button.config(text=fourth_option[4])
        amountlabel.config(image=image4)


    elif value == 'Makar Sankranti':  # 5
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[5])

        textQuestion1Button.config(text=first_option[5])
        textQuestion2Button.config(text=second_option[5])
        textQuestion3Button.config(text=third_option[5])
        textQuestion4Button.config(text=fourth_option[5])
        amountlabel.config(image=image5)


    elif value == fourth_option[5]:  # 6
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[6])

        textQuestion1Button.config(text=first_option[6])
        textQuestion2Button.config(text=second_option[6])
        textQuestion3Button.config(text=third_option[6])
        textQuestion4Button.config(text=fourth_option[6])
        amountlabel.config(image=image6)


    elif value == second_option[6]:  # 7
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[7])

        textQuestion1Button.config(text=first_option[7])
        textQuestion2Button.config(text=second_option[7])
        textQuestion3Button.config(text=third_option[7])
        textQuestion4Button.config(text=fourth_option[7])
        amountlabel.config(image=image7)



    elif value == fourth_option[7]:  # 8
        # textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[8])

        textQuestion1Button.config(text=first_option[8])
        textQuestion2Button.config(text=second_option[8])
        textQuestion3Button.config(text=third_option[8])
        textQuestion4Button.config(text=fourth_option[8])
        amountlabel.config(image=image8)


    elif value == first_option[8]:  # 9
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[9])

        textQuestion1Button.config(text=first_option[9])
        textQuestion2Button.config(text=second_option[9])
        textQuestion3Button.config(text=third_option[9])
        textQuestion4Button.config(text=fourth_option[9])
        amountlabel.config(image=image9)


    elif value == third_option[9]:  # 10
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[10])

        textQuestion1Button.config(text=first_option[10])
        textQuestion2Button.config(text=second_option[10])
        textQuestion3Button.config(text=third_option[10])
        textQuestion4Button.config(text=fourth_option[10])
        amountlabel.config(image=image10)


    elif value == fourth_option[10]:  # 11
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[11])

        textQuestion1Button.config(text=first_option[11])
        textQuestion2Button.config(text=second_option[11])
        textQuestion3Button.config(text=third_option[11])
        textQuestion4Button.config(text=fourth_option[11])
        amountlabel.config(image=image11)


    elif value == third_option[11]:  # 12
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[12])

        textQuestion1Button.config(text=first_option[12])
        textQuestion2Button.config(text=second_option[12])
        textQuestion3Button.config(text=third_option[12])
        textQuestion4Button.config(text=fourth_option[12])
        amountlabel.config(image=image12)


    elif value == first_option[12]:  # 13
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[13])

        textQuestion1Button.config(text=first_option[13])
        textQuestion2Button.config(text=second_option[13])
        textQuestion3Button.config(text=third_option[13])
        textQuestion4Button.config(text=fourth_option[13])
        amountlabel.config(image=image13)

    elif value == fourth_option[13]:  # 14
        textQuestionArea.delete(1.0, END)
        textQuestionArea.insert(END, questions[14])

        textQuestion1Button.config(text=first_option[14])
        textQuestion2Button.config(text=second_option[14])
        textQuestion3Button.config(text=third_option[14])
        textQuestion4Button.config(text=fourth_option[14])
        amountlabel.config(image=image14)

    elif value == second_option[14]:  # 15
        def playagain():
            phoneButton.config(state=NORMAL, image=phoneImage)
            live50Button.config(state=NORMAL, image=image50)
            audiencePoleButton.config(state=NORMAL, image=audiencePole)
            amountlabel.config(image=amountimage)
            textQuestionArea.delete(1.0, END)
            textQuestionArea.insert(END, questions[0])
            textQuestion1Button.config(text=first_option[0])
            textQuestion2Button.config(text=second_option[0])
            textQuestion3Button.config(text=third_option[0])
            textQuestion4Button.config(text=fourth_option[0])
            root2.destroy()
            mixer.music.load('kbc.mp3')
            mixer.music.play(-1)

        amountlabel.config(image=image15)
        mixer.music.stop()
        mixer.music.load('Kbcwon.mp3')
        mixer.music.play()
        root2 = Toplevel()
        root2.config(bg='black')
        root2.geometry('500x400')
        root2.title('You won 1 million Pounds')
        centerimg = PhotoImage(file='center.png')
        imgLabel = Label(root2, image=centerimg, bd=0, )
        imgLabel.pack(pady=30)

        winlabel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='black', fg='white')
        winlabel.pack()

        happyimage = PhotoImage(file='happy.png')
        happYLabel = Label(root2, image=happyimage, bg='black')
        happYLabel.place(x=400, y=280)

        happYLabel1 = Label(root2, image=happyimage, bg='black')
        happYLabel1.place(x=30, y=280)

        playagainButton = Button(root2, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=playagain)
        playagainButton.pack()

        def on_closing():
            root2.destroy()
            root.destroy()

        root2.protocol('WM_DELETE_WINDOW', on_closing)
        root2.mainloop()

    else:
        def tryagain():
            mixer.music.load('kbc.mp3')
            mixer.music.play(-1)
            phoneButton.config(state=NORMAL, image=phoneImage)
            live50Button.config(state=NORMAL, image=image50)
            audiencePoleButton.config(state=NORMAL, image=audiencePole)

            textQuestionArea.delete(1.0, END)
            textQuestionArea.insert(END, questions[0])
            textQuestion1Button.config(text=first_option[0])
            textQuestion2Button.config(text=second_option[0])
            textQuestion3Button.config(text=third_option[0])
            textQuestion4Button.config(text=fourth_option[0])
            amountlabel.config(image=amountimage)
            root1.destroy()

        mixer.music.stop()
        root1 = Toplevel()
        root1.config(bg='black')
        root1.geometry('500x400')
        root1.title('You won 0 Pound')
        img = PhotoImage(file='center.png')
        imgLabel = Label(root1, image=img, bd=0)
        imgLabel.pack(pady=30)
        loselabel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
        loselabel.pack()
        sadimage = PhotoImage(file='sad.png')
        sadlabel = Label(root1, image=sadimage, bg='black')
        sadlabel.place(x=400, y=280)
        sadlabel1 = Label(root1, image=sadimage, bg='black')
        sadlabel1.place(x=30, y=280)

        tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                , activebackground='black', cursor='hand2', activeforeground='white', command=tryagain)
        tryagainButton.pack()

        def on_closing():
            root1.destroy()
            root.destroy()

        root1.protocol('WM_DELETE_WINDOW', on_closing)

        root1.mainloop()


def change50():
    live50Button.config(image=image50x)
    live50Button.config(state=DISABLED)

    if textQuestionArea.get(1.0, 'end-1c') == questions[0]:
        textQuestion1Button.config(text='')
        textQuestion3Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[1]:
        textQuestion4Button.config(text='')
        textQuestion1Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[2]:
        textQuestion3Button.config(text='')
        textQuestion4Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[3]:
        textQuestion2Button.config(text='')
        textQuestion4Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[4]:
        textQuestion3Button.config(text='')
        textQuestion4Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[5]:
        textQuestion2Button.config(text='')
        textQuestion3Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[6]:
        textQuestion1Button.config(text='')
        textQuestion3Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[7]:
        textQuestion3Button.config(text='')
        textQuestion4Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[8]:
        textQuestion2Button.config(text='')
        textQuestion4Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[9]:
        textQuestion1Button.config(text='')
        textQuestion4Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[10]:
        textQuestion1Button.config(text='')
        textQuestion3Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[11]:
        textQuestion1Button.config(text='')
        textQuestion2Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[12]:
        textQuestion1Button.config(text='')
        textQuestion2Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[13]:
        textQuestion2Button.config(text='')
        textQuestion3Button.config(text='')

    if textQuestionArea.get(1.0, 'end-1c') == questions[14]:
        textQuestion1Button.config(text='')
        textQuestion4Button.config(text='')


def peoplechange():
    audiencePoleButton.config(image=audiencePolex)
    audiencePoleButton.config(state=DISABLED)

    if textQuestionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=30)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=60)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=40)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=90)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=30)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=80)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=40)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=30)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=80)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=60)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=50)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=70)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=30)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=70)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=90)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=50)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=30)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=80)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=40)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=30)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=80)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=10)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=40)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=30)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=30)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=80)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=20)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=40)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=10)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=70)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=50)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=30)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=90)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=80)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=70)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=20)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=30)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=50)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=70)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=60)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=40)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=20)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=50)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=70)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=30)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=80)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=90)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=40)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=20)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=60)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=50)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=80)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=60)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=35)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=40)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=80)
        progressvolumeLabel3.place(x=790, y=330)

    if textQuestionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarLabel.place(x=660, y=200)
        progressvolume.config(value=60)
        progressvolumeLabel.place(x=660, y=330)

        progressbarLabel1.place(x=700, y=200)
        progressvolume1.config(value=65)
        progressvolumeLabel1.place(x=710, y=330)

        progressbarLabel2.place(x=740, y=200)
        progressvolume2.config(value=90)
        progressvolumeLabel2.place(x=750, y=330)

        progressbarLabel3.place(x=780, y=200)
        progressvolume3.config(value=80)
        progressvolumeLabel3.place(x=790, y=330)


def phonechange():
    mixer.music.stop()
    mixer.music.load('calling.mp3')
    mixer.music.play()

    phoneButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)


def phoneclick():
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    if textQuestionArea.get(1.0, 'end-1c') == questions[0]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[1]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[2]:
        engine.say('The Answer is A')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[3]:
        engine.say('The Answer is C')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[4]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[5]:
        engine.say('The Answer is A')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[6]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[7]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[8]:
        engine.say('The Answer is A')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[9]:
        engine.say('The Answer is C')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[10]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[11]:
        engine.say('The Answer is C')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[12]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[13]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionArea.get(1.0, 'end-1c') == questions[14]:
        engine.say('The Answer is C')
        engine.runAndWait()


root = Tk()
root.geometry('1352x652+0+0')
root.resizable(0, 0)
root.title('Who Wants To Be A Millionaire')
root.config(bg='black')

leftFrame = Frame(root, width=900, height=600, bg='black', padx=110)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg='black', width=452, height=600, padx=110, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, width=900, height=200, bg='black', pady=25)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, width=900, height=200, bg='black', pady=25)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, width=900, height=200, bg='black')
bottomFrame.grid(row=2, column=0)

centreImage = PhotoImage(file='center.png')
logoLabel = Label(middleFrame, image=centreImage, bd=0, width=300, height=200, bg='black')
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file='jpge50.png')
image50x = PhotoImage(file='jpge50X.png')

live50Button = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                      height=80, command=change50)
live50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='jpgePeople.png')
audiencePolex = PhotoImage(file='jpgePeopleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                            width=180, height=80, command=peoplechange)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='jpgePhone.png')
phoneImageX = PhotoImage(file='jpgePhoneX.png')
phoneButton = Button(topFrame, image=phoneImage, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                     height=80, command=phonechange)
phoneButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')
callButton = Button(root, bg='black', bd=0, activebackground='black', cursor='hand2', command=phoneclick)
callButton.place(x=70, y=260)

amountimage = PhotoImage(file='Picture01.png')
image1 = PhotoImage(file='Picture1.png')
image2 = PhotoImage(file='Picture2.png')
image3 = PhotoImage(file='Picture3.png')
image4 = PhotoImage(file='Picture4.png')
image5 = PhotoImage(file='Picture5.png')
image6 = PhotoImage(file='Picture6.png')
image7 = PhotoImage(file='Picture7.png')
image8 = PhotoImage(file='Picture8.png')
image9 = PhotoImage(file='Picture9.png')
image10 = PhotoImage(file='Picture10.png')
image11 = PhotoImage(file='Picture11.png')
image12 = PhotoImage(file='Picture12.png')
image13 = PhotoImage(file='Picture13.png')
image14 = PhotoImage(file='Picture14.png')
image15 = PhotoImage(file='Picture15.png')

amountlabel = Label(rightFrame, image=amountimage, bg='black', bd=0)
amountlabel.grid(row=0, column=0)

textQuestionArea = Text(bottomFrame, font=('arial', 18, 'bold'), bg='blue', fg='white', width=44, height=2, bd=5,
                        wrap='word')
textQuestionArea.grid(row=0, column=0, columnspan=4, pady=4)

textQuestionArea.insert(END, questions[0])

labelquestionA = Label(bottomFrame, font=('arial', 14, 'bold'), text='A:', bg='black', fg='white')
labelquestionA.grid(row=1, column=0, pady=4, )

textQuestion1Button = Button(bottomFrame, text=first_option[0], font=('arial', 14, 'bold'), bg='blue', fg='white',
                             width=17, height=2, cursor='hand2')
textQuestion1Button.grid(row=1, column=1, pady=4)

labelquestionB = Label(bottomFrame, font=('arial', 14, 'bold'), text='B:', bg='black', fg='white')
labelquestionB.grid(row=1, column=2, pady=4, )

textQuestion2Button = Button(bottomFrame, text=second_option[0], font=('arial', 14, 'bold'), bg='blue', fg='white',
                             width=17, height=2, cursor='hand2')
textQuestion2Button.grid(row=1, column=3, pady=4)

labelquestionC = Label(bottomFrame, font=('arial', 14, 'bold'), text='C:', bg='black', fg='white')
labelquestionC.grid(row=2, column=0, pady=4, )

textQuestion3Button = Button(bottomFrame, text=third_option[0], font=('arial', 14, 'bold'), bg='blue', fg='white',
                             width=17, height=2, cursor='hand2')
textQuestion3Button.grid(row=2, column=1, pady=4)

labelquestionD = Label(bottomFrame, font=('arial', 14, 'bold'), text='D:', bg='black', fg='white')
labelquestionD.grid(row=2, column=2, pady=4, )

textQuestion4Button = Button(bottomFrame, text=fourth_option[0], font=('arial', 14, 'bold'), bg='blue', fg='white',
                             width=17, height=2, cursor='hand2')
textQuestion4Button.grid(row=2, column=3, pady=4)

progressbarLabel = Label(root, text='', height=8, width=2, bg='black')
progressbarLabel.place(x=660, y=200)
progressbarLabel.place_forget()

progressvolume = Progressbar(progressbarLabel, orient=VERTICAL, mode='determinate', length=120)
progressvolume.grid(row=0, column=0, ipadx=5)

progressvolumeLabel = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')
progressvolumeLabel.place(x=660, y=330)
progressvolumeLabel.place_forget()

progressbarLabel1 = Label(root, text='', height=8, width=2, bg='black')
progressbarLabel1.place(x=700, y=200)
progressbarLabel1.place_forget()

progressvolume1 = Progressbar(progressbarLabel1, orient=VERTICAL, mode='determinate', value=0, length=120)
progressvolume1.grid(row=0, column=0, ipadx=5)

progressvolumeLabel1 = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')
progressvolumeLabel1.place(x=710, y=330)
progressvolumeLabel1.place_forget()

progressbarLabel2 = Label(root, text='', height=8, width=2, bg='black')
progressbarLabel2.place(x=740, y=200)
progressbarLabel2.place_forget()
progressvolume2 = Progressbar(progressbarLabel2, orient=VERTICAL, mode='determinate', value=0, length=120)
progressvolume2.grid(row=0, column=0, ipadx=5)
progressvolumeLabel2 = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')
progressvolumeLabel2.place(x=750, y=330)
progressvolumeLabel2.place_forget()

progressbarLabel3 = Label(root, text='', height=8, width=2, bg='black')
progressbarLabel3.place(x=780, y=200)
progressbarLabel3.place_forget()
progressvolume3 = Progressbar(progressbarLabel3, orient=VERTICAL, mode='determinate', value=0, length=120)
progressvolume3.grid(row=0, column=0, ipadx=5)
progressvolumeLabel3 = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')
progressvolumeLabel3.place(x=790, y=330)
progressvolumeLabel3.place_forget()

textQuestion1Button.bind('<Button-1>', select)
textQuestion2Button.bind('<Button-1>', select)
textQuestion3Button.bind('<Button-1>', select)
textQuestion4Button.bind('<Button-1>', select)

root.mainloop()
