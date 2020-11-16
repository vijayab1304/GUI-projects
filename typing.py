from tkinter import *
from tkinter import ttk
import ttkthemes
import random
from time import sleep
import threading


timelimit=60
remainingtime=timelimit
elapsedtime=0
elapsedtimeInMinutes=0

totalwords=0
wrongwords=0

wpm=0
accuracy=0

def start_timer():
    global elapsedtime

    entry.focus()
    entry.config(state=NORMAL)
    startButton.config(state=DISABLED)

    for time in range(1,timelimit+1):
        elapsedtime=time
        elapsed_timer_label.config(text=elapsedtime)

        updateRemainingTime=remainingtime-elapsedtime
        remaining_timer_label.config(text=updateRemainingTime)

        sleep(1)
        root.update()

    entry.config(state=DISABLED)
    resetButton.config(state=NORMAL)

def count():
    global wrongwords,elapsedtime,elapsedtimeInMinutes
    para_words=label_paragraph['text'].split()

    while elapsedtime!=timelimit:
        entered_paragraph=entry.get(1.0,END).split()
        totalwords=len(entered_paragraph)

    for pair in list(zip(para_words,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1

    elapsedtimeInMinutes=elapsedtime/60

    wpm=(totalwords-wrongwords)/elapsedtimeInMinutes
    wpm_timer_label.config(text=wpm)

    gross_wpm=totalwords/elapsedtimeInMinutes
    accuracy=wpm/gross_wpm*100
    accuracy=round(accuracy)
    accuracy_countlabel.config(text=str(accuracy)+'%')


    total_words_count_label.config(text=totalwords)

    wrong_words_count_label.config(text=wrongwords)

def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2=threading.Thread(target=count)
    t2.start()


def reset():
    global remainingtime,elapsedtime
    resetButton.config(state=DISABLED)
    startButton.config(state=NORMAL)

    entry.config(state=NORMAL)
    entry.delete(1.0,END)
    entry.config(state=DISABLED)

    remainingtime=timelimit
    elapsedtime=0
    elapsedtimeInMinutes=0

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_timer_label.config(text='0')
    accuracy_countlabel.config(text='0')
    total_words_count_label.config(text='0')
    wrong_words_count_label.config(text='0')

root=ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')

root.geometry('940x735+350+0')
root.title('Master Typing')
root.resizable(0,0)

mainframe=Frame(root,bg='snow',bd=4)
mainframe.grid(row=0,column=0)

titleframe=Frame(mainframe,bg='orange',relief=FLAT)
titleframe.grid(row=0,column=0)
titleLabel=Label(titleframe,text="Master Typing",font=('algerian',28,'bold'),bg='goldenrod3',fg='white',
                 bd=10,width=38,relief=FLAT)
titleLabel.grid(row=0,column=0,pady=5)

frame_test=Frame(mainframe,bg='snow',relief='flat')
frame_test.grid(row=1,column=0)
selected_paragraph=[' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

                    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

                    'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

                    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

                    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
                    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
                    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

                    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'

                    ]

random.shuffle(selected_paragraph)

label_paragraph=Label(frame_test,text=selected_paragraph[0],wraplength=930,justify=LEFT,bg='snow',font=('arial',14,'bold'))
label_paragraph.grid(row=0,column=0,pady=5)

text_frame=Frame(mainframe,bg='snow',relief='flat')
text_frame.grid(row=2,column=0)
entry=Text(text_frame,height=7,width=100,bd=4,font=('arial',12,'bold'),wrap='word',relief=GROOVE)
entry.grid(row=0,column=0,pady=5,padx=5)

entry.config(state=DISABLED)

frame_output=Frame(mainframe,bg='snow',relief=FLAT)
frame_output.grid(row=3,column=0)
frame_label=Frame(frame_output,bg='snow')
frame_label.grid(row=0)

elapsed_time_label=Label(frame_label,text='Elapsed Time',font=('Tahoma',12,'bold'),bg='snow',fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5,pady=5)
elapsed_timer_label=Label(frame_label,text='0',font=('Tahoma',12,'bold'),bg='snow',fg='black')
elapsed_timer_label.grid(row=0,column=1,padx=5,pady=5)

remaining_time_label=Label(frame_label,text='Remaining Time',font=('Tahoma',12,'bold'),bg='snow',fg='red')
remaining_time_label.grid(row=0,column=2,padx=5,pady=5)
remaining_timer_label=Label(frame_label,text='60',font=('Tahoma',12,'bold'),bg='snow',fg='black')
remaining_timer_label.grid(row=0,column=3,padx=5,pady=5)

wpm_time_label=Label(frame_label,text='WPM',font=('Tahoma',12,'bold'),bg='snow',fg='red')
wpm_time_label.grid(row=0,column=4,padx=5,pady=5)
wpm_timer_label=Label(frame_label,text='0',font=('Tahoma',12,'bold'),bg='snow',fg='black')
wpm_timer_label.grid(row=0,column=5,padx=5,pady=5)

accuracylabel=Label(frame_label,text='Accuracy',font=('Tahoma',12,'bold'),bg='snow',fg='red')
accuracylabel.grid(row=0,column=6,padx=5,pady=5)
accuracy_countlabel=Label(frame_label,text='0',font=('Tahoma',12,'bold'),bg='snow',fg='black')
accuracy_countlabel.grid(row=0,column=7,padx=5,pady=5)

total_words_label=Label(frame_label,text='Total Words',font=('Tahoma',12,'bold'),bg='snow',fg='red')
total_words_label.grid(row=0,column=8,padx=5,pady=5)
total_words_count_label=Label(frame_label,text='0',font=('Tahoma',12,'bold'),bg='snow',fg='black')
total_words_count_label.grid(row=0,column=9,padx=5,pady=5)

wrong_words_label=Label(frame_label,text='Wrong Words',font=('Tahoma',12,'bold'),bg='snow',fg='red')
wrong_words_label.grid(row=0,column=10,padx=5,pady=5)
wrong_words_count_label=Label(frame_label,text='0',font=('Tahoma',12,'bold'),bg='snow',fg='black')
wrong_words_count_label.grid(row=0,column=11,padx=5,pady=5)

frame_control=Frame(frame_output,bg='snow')
frame_control.grid(row=1)

startButton=ttk.Button(frame_control,text='Start',command=start)
startButton.grid(row=0,column=0,padx=10)

resetButton=ttk.Button(frame_control,text='Reset',command=reset)
resetButton.grid(row=0,column=1,padx=10)
resetButton.config(state=DISABLED)

exitButton=ttk.Button(frame_control,text='Exit',command=root.destroy)
exitButton.grid(row=0,column=2,padx=10)

keyboardFrame=Frame(mainframe,bg='snow')
keyboardFrame.grid(row=4,pady=10)

frame_1to0=Frame(keyboardFrame,bg='snow')
frame_1to0.grid(row=0,column=0)
label1=Label(frame_1to0,text='1',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label2=Label(frame_1to0,text='2',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label3=Label(frame_1to0,text='3',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label4=Label(frame_1to0,text='4',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label5=Label(frame_1to0,text='5',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label6=Label(frame_1to0,text='6',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label7=Label(frame_1to0,text='7',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label8=Label(frame_1to0,text='8',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label9=Label(frame_1to0,text='9',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label0=Label(frame_1to0,text='0',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))

label1.grid(row=0,column=0,padx=5,pady=3)
label2.grid(row=0,column=1,padx=5,pady=3)
label3.grid(row=0,column=2,padx=5,pady=3)
label4.grid(row=0,column=3,padx=5,pady=3)
label5.grid(row=0,column=4,padx=5,pady=3)
label6.grid(row=0,column=5,padx=5,pady=3)
label7.grid(row=0,column=6,padx=5,pady=3)
label8.grid(row=0,column=7,padx=5,pady=3)
label9.grid(row=0,column=8,padx=5,pady=3)
label0.grid(row=0,column=9,padx=5,pady=3)

frame_q_p=Frame(keyboardFrame,bg='snow')
frame_q_p.grid(row=1)

labelQ=Label(frame_q_p,text='Q',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelW=Label(frame_q_p,text='W',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelE=Label(frame_q_p,text='E',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelR=Label(frame_q_p,text='R',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelT=Label(frame_q_p,text='T',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelY=Label(frame_q_p,text='Y',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelU=Label(frame_q_p,text='U',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelI=Label(frame_q_p,text='I',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelO=Label(frame_q_p,text='O',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelP=Label(frame_q_p,text='P',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelQ.grid(row=0,column=0,padx=5,pady=3)
labelW.grid(row=0,column=1,padx=5,pady=3)
labelE.grid(row=0,column=2,padx=5,pady=3)
labelR.grid(row=0,column=3,padx=5,pady=3)
labelT.grid(row=0,column=4,padx=5,pady=3)
labelY.grid(row=0,column=5,padx=5,pady=3)
labelU.grid(row=0,column=6,padx=5,pady=3)
labelI.grid(row=0,column=7,padx=5,pady=3)
labelO.grid(row=0,column=8,padx=5,pady=3)
labelP.grid(row=0,column=9,padx=5,pady=3)


frame_a_l=Frame(keyboardFrame,bg='snow')
frame_a_l.grid(row=2)

labelA=Label(frame_a_l,text='A',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelS=Label(frame_a_l,text='S',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelD=Label(frame_a_l,text='D',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelF=Label(frame_a_l,text='F',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelG=Label(frame_a_l,text='G',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelH=Label(frame_a_l,text='H',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelJ=Label(frame_a_l,text='J',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelK=Label(frame_a_l,text='K',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelL=Label(frame_a_l,text='L',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))

labelA.grid(row=0,column=0,padx=5,pady=3)
labelS.grid(row=0,column=1,padx=5,pady=3)
labelD.grid(row=0,column=2,padx=5,pady=3)
labelF.grid(row=0,column=3,padx=5,pady=3)
labelG.grid(row=0,column=4,padx=5,pady=3)
labelH.grid(row=0,column=5,padx=5,pady=3)
labelJ.grid(row=0,column=6,padx=5,pady=3)
labelK.grid(row=0,column=7,padx=5,pady=3)
labelL.grid(row=0,column=8,padx=5,pady=3)

frame_z_m=Frame(keyboardFrame,bg='snow')
frame_z_m.grid(row=3)

labelZ=Label(frame_z_m,text='Z',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelX=Label(frame_z_m,text='X',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelC=Label(frame_z_m,text='C',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelV=Label(frame_z_m,text='V',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelB=Label(frame_z_m,text='B',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelN=Label(frame_z_m,text='N',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
labelM=Label(frame_z_m,text='M',fg='white',bg='black',width=5,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))


labelZ.grid(row=0,column=0,padx=5,pady=3)
labelX.grid(row=0,column=1,padx=5,pady=3)
labelC.grid(row=0,column=2,padx=5,pady=3)
labelV.grid(row=0,column=3,padx=5,pady=3)
labelB.grid(row=0,column=4,padx=5,pady=3)
labelN.grid(row=0,column=5,padx=5,pady=3)
labelM.grid(row=0,column=6,padx=5,pady=3)

spaceFrame=Frame(keyboardFrame,bg='snow')
spaceFrame.grid(row=4)

label_space=Label(spaceFrame,bg='black',fg='white',width=40,height=2,relief=GROOVE,bd=10,font=('arial',10,'bold'))
label_space.grid(row=0,column=0,padx=10,pady=3)


def changeBG(widget):
    bg='black'
    widget.configure(background='blue')
    widget.after(100,lambda color=bg: widget.configure(background=color))


label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]
label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,
                 labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]
space_label=[label_space]



binding_numbers=['1','2','3','4','5','6','7','8','9','0']

binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
                           'U','V','W','X','Y','Z']
binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                         'u','v','w','x','y','z']

for number in range(len(binding_numbers)):
    root.bind(f'{binding_numbers[number]}',lambda event,label=label_numbers[number]:changeBG(label))

for capital_alphabet in range(len(binding_capital_alphabets)):
    root.bind(f'{binding_capital_alphabets[capital_alphabet]}',lambda event,label=label_alphabets[capital_alphabet]:changeBG(label))

for small_alphabet in range(len(binding_small_alphabets)):
    root.bind(f'{binding_small_alphabets[small_alphabet]}',lambda event,label=label_alphabets[small_alphabet]:changeBG(label))


root.bind('<space>',lambda event,label=space_label[0]:changeBG(label))












root.mainloop()
