from tkinter import  *
import tkinter as ttk
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)



mixer.init()
mixer.music.load('kbc_awesome.mp3')
mixer.music.play(-1)
import Image
import ImageTk

'----------------------------------------------------Select Function------------------------------------------------------------------------'

def select(event):
    callbutton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarlblA.place_forget()
    progressbarlblB.place_forget()
    progressbarlblC.place_forget()
    progressbarlblD.place_forget()



    b=event.widget
    value=b['text']
    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def Exit():

                    root2.destroy()
                    root.destroy()

                def Playagain():
                    ll50.config(state=NORMAL, image=image50)
                    llaudiencepol.config(state=NORMAL, image=audiencepol)
                    llphonofrnd.config(state=NORMAL, image=phonofriend)
                    root2.destroy()
                    question_area.delete(1.0, END)
                    question_area.insert(END, questions[0])

                    optionbutton1.config(text=first_option[0])
                    optionbutton2.config(text=second_option[0])
                    optionbutton3.config(text=third_option[0])
                    optionbutton4.config(text=fourth_option[0])

                    chrtimagelable.config(image=chart0)

                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()


                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.title('Final Result')
                root2.config(bg="black")
                root2.geometry('500x400+560+260')
                madelimage=ImageTk.PhotoImage(Image.open("medel_edited1.jpg"))
                imglable = Label(root2,image=madelimage,bd=0)
                imglable.pack(padx=50)

                Wonlabel = Label(root2, text='CONGRATULATIONS\n YOU BECOME\n MILLIONAIRE', font=("Copperplate Gothic Bold", 25, "bold",), bg='black', bd=0, fg="#8B2323")
                # Wonlabel = Label(root2, text='YOU BECOME MILLIONAIRE', font=("Cambria", 25, "bold"), bg='black', bd=0, fg="white")
                # Wonlabel.pack()
                Wonlabel.pack()
                playimage=ImageTk.PhotoImage(Image.open("playbutton20_edited.jpg"))


                playagainbutton = Button(root2, image=playimage, font=("Copperplate Gothic Bold", 19, "bold"), bd=0, fg="white", bg="black",
                                   activebackground="black", activeforeground="white", cursor="hand2", command=Playagain)
                playagainbutton.pack()

                exitbutton1=ImageTk.PhotoImage(Image.open('exitbutton.jpg'))

                closebutton = Button(root2, image=exitbutton1, font=("Copperplate Gothic Bold", 19, "bold"), bd=0, fg="white", bg="black",width=80,height=72,
                                     activebackground="black", activeforeground="white", cursor="hand2", command=Exit)
                closebutton.pack()

                emojimg = Image.open("happy1.png")
                emojiimage = ImageTk.PhotoImage(emojimg)
                emojilbl = Label(root2, image=emojiimage, width=180, height=180, bg="black")
                emojilbl.place(x=12, y=250)

                emojimg1 = Image.open("happy1.png")
                emojiimage2 = ImageTk.PhotoImage(emojimg1)
                emojilbl2 = Label(root2, image=emojiimage2, width=180, height=180, bg="black")
                emojilbl2.place(x=350, y=250)

                root2.mainloop()
                break

            question_area.delete(1.0,END)
            question_area.insert(END,questions[i+1])

            optionbutton1.config(text=first_option[i+1])
            optionbutton2.config(text=second_option[i+1])
            optionbutton3.config(text=third_option[i+1])
            optionbutton4.config(text=fourth_option[i+1])
            chrtimagelable.config(image=chart[i+1])
        if value not in correct_answers:
            def Exit():
                root1.destroy()
                root.destroy()

            def Tryagain():
                ll50.config(state=NORMAL,image=image50)
                llaudiencepol.config(state=NORMAL,image=audiencepol)
                llphonofrnd.config(state=NORMAL,image=phonofriend)
                root1.destroy()
                question_area.delete(1.0,END)
                question_area.insert(END,questions[0])

                optionbutton1.config(text=first_option[0])
                optionbutton2.config(text=second_option[0])
                optionbutton3.config(text=third_option[0])
                optionbutton4.config(text=fourth_option[0])

                chrtimagelable.config(image=chart0)

            root1=Toplevel()
            root1.overrideredirect(True)
            root1.title('Losing Result')
            root1.config(bg="black")
            root1.geometry('500x400+560+260')
            imglable=Label(root1,fg="#1874CD",bd=0)
            imglable.pack(pady=30)
            root1.grab_set()

            loselabel=Label(root1,text='YOU JUST LOST',font=("Copperplate Gothic Bold",25,"bold"),bg='black',bd=0,fg="#8B2323")
            loselabel.pack()

            tryimage = ImageTk.PhotoImage(Image.open("tryagain_edited.jpg"))

            trybutton=Button(root1,image=tryimage,font=("Copperplate Gothic Bold",19,"bold"),bd=0,fg="#1874CD",bg="black",
                             activebackground="black",activeforeground="white",cursor="hand2",command=Tryagain)
            trybutton.pack()

            exitbutton=ImageTk.PhotoImage(Image.open("exitbutton.jpg"))


            closebutton=Button(root1,image=exitbutton,font=("Copperplate Gothic Bold",19,"bold"),bd=0,fg="white",bg="black",width=80,height=72,
                               activebackground="black",activeforeground="white",cursor="hand2",command=Exit)
            closebutton.pack()

            emojimg=Image.open("smilyemoji.jpg")
            emojiimage=ImageTk.PhotoImage(emojimg)

            emojilbl=Label(root1,image=emojiimage,width=80,height=80,bg="black")
            emojilbl.place(x=25,y=250)

            emojimg1 = Image.open("smilyemoji.jpg")
            emojiimage2 = ImageTk.PhotoImage(emojimg1)
            emojilbl2 = Label(root1, image=emojiimage2, width=80, height=80, bg="black")
            emojilbl2.place(x=380, y=250)

            root1.mainloop()

            break

'=================================================================lifeline50 function================================================================='

def Lyfeline50():
    ll50.config(image=image50x,state=DISABLED)
    if question_area.get(1.0,'end-1c')==questions[0]:
        optionbutton1.config(text="")
        optionbutton2.config(text="")

    if question_area.get(1.0,'end-1c')==questions[1]:
        optionbutton1.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[2]:
        optionbutton3.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[3]:
        optionbutton2.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[4]:
        optionbutton1.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[5]:
        optionbutton3.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[6]:
        optionbutton3.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[7]:
        optionbutton1.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[8]:
        optionbutton2.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[9]:
        optionbutton1.config(text="")
        optionbutton4.config(text="")

    if question_area.get(1.0,'end-1c')==questions[10]:
        optionbutton1.config(text="")
        optionbutton3.config(text="")

    if question_area.get(1.0,'end-1c')==questions[11]:
        optionbutton1.config(text="")
        optionbutton2.config(text="")

    if question_area.get(1.0,'end-1c')==questions[12]:
        optionbutton2.config(text="")
        optionbutton3.config(text="")

    if question_area.get(1.0,'end-1c')==questions[13]:
        optionbutton1.config(text="")
        optionbutton3.config(text="")

    if question_area.get(1.0,'end-1c')==questions[14]:
        optionbutton1.config(text="")
        optionbutton4.config(text="")

'================================================================audiencepole function=================================================================='

def audiencepolelifeline():
        llaudiencepol.config(image=audiencepolx,state=DISABLED)
        progressbarA.place(x=750,y=320)
        progressbarB.place(x=810,y=320)
        progressbarC.place(x=870,y=320)
        progressbarD.place(x=930,y=320)

        progressbarlblA.place(x=750,y=450)
        progressbarlblB.place(x=810,y=450)
        progressbarlblC.place(x=870,y=450)
        progressbarlblD.place(x=930,y=450)

        if question_area.get(1.0,'end-1c')==questions[0]:
            progressbarA.config(value=20)
            progressbarB.config(value=50)
            progressbarC.config(value=70)
            progressbarD.config(value=90)

        if question_area.get(1.0,'end-1c')==questions[1]:
            progressbarA.config(value=20)
            progressbarB.config(value=80)
            progressbarC.config(value=60)
            progressbarD.config(value=40)

        if question_area.get(1.0,'end-1c')==questions[2]:
            progressbarA.config(value=80)
            progressbarB.config(value=40)
            progressbarC.config(value=20)
            progressbarD.config(value=55)

        if question_area.get(1.0,'end-1c')==questions[3]:
            progressbarA.config(value=35)
            progressbarB.config(value=25)
            progressbarC.config(value=88)
            progressbarD.config(value=15)

        if question_area.get(1.0,'end-1c')==questions[4]:
            progressbarA.config(value=20)
            progressbarB.config(value=85)
            progressbarC.config(value=45)
            progressbarD.config(value=62)

        if question_area.get(1.0,'end-1c')==questions[5]:
            progressbarA.config(value=91)
            progressbarB.config(value=10)
            progressbarC.config(value=60)
            progressbarD.config(value=25)

        if question_area.get(1.0,'end-1c')==questions[6]:
            progressbarA.config(value=20)
            progressbarB.config(value=75)
            progressbarC.config(value=25)
            progressbarD.config(value=55)

        if question_area.get(1.0,'end-1c')==questions[7]:
            progressbarA.config(value=20)
            progressbarB.config(value=88)
            progressbarC.config(value=65)
            progressbarD.config(value=56)

        if question_area.get(1.0,'end-1c')==questions[8]:
            progressbarA.config(value=75)
            progressbarB.config(value=45)
            progressbarC.config(value=84)
            progressbarD.config(value=56)

        if question_area.get(1.0,'end-1c')==questions[9]:
            progressbarA.config(value=45)
            progressbarB.config(value=81)
            progressbarC.config(value=95)
            progressbarD.config(value=25)

        if question_area.get(1.0,'end-1c')==questions[10]:
            progressbarA.config(value=25)
            progressbarB.config(value=68)
            progressbarC.config(value=55)
            progressbarD.config(value=85)

        if question_area.get(1.0,'end-1c')==questions[11]:
            progressbarA.config(value=35)
            progressbarB.config(value=75)
            progressbarC.config(value=88)
            progressbarD.config(value=65)

        if question_area.get(1.0,'end-1c')==questions[12]:
            progressbarA.config(value=75)
            progressbarB.config(value=55)
            progressbarC.config(value=35)
            progressbarD.config(value=90)

        if question_area.get(1.0,'end-1c')==questions[13]:
            progressbarA.config(value=35)
            progressbarB.config(value=55)
            progressbarC.config(value=70)
            progressbarD.config(value=90)

        if question_area.get(1.0,'end-1c')==questions[14]:
            progressbarA.config(value=20)
            progressbarB.config(value=70)
            progressbarC.config(value=90)
            progressbarD.config(value=50)

'==================================================phonelifeline function========================================================================'

def phonelifeline():
    mixer.music.load('kbc_idea_phone_a_frd.mp3')
    mixer.music.play()
    callbutton.place(x=900,y=100)
    llphonofrnd.config(image=phonofriendx,state=DISABLED)

'============================================================phoneclick function=================================================================='

def phoneclick():
    for i in range(15):
        if question_area.get(1.0,'end-1c')==questions[i]:
            engine.say(f'The Answer is{correct_answers[i]}')
            engine.runAndWait()

'=====================================================Questions & Answer========================================================================'

questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Find the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "11:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]


'==========================================================Main window==============================================================================='


root=Tk()
root.geometry("1610x850+0+0")
root.title("Who want to become a Millionaire created by Vimal Yadav")
root.config(bg="#030303")

canvas=Canvas(root,width=1900,height=950)
image=ImageTk.PhotoImage(Image.open('bg2.jpg'))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.place(x=0,y=0)

# mainwindowimage=ImageTk.PhotoImage(Image.open('bgwindowimg.jpg'))
# mainlabel=LabelFrame(root,Image=mainwindowimage,bd=0)
# mainlabel.place(x=0,y=0,width=450,height=200)



# leftframe=Frame(root,bg="black")



# leftframe.grid(row=0,column=0)



topframe=Frame(root,bg="black",padx=100,pady=20,width=40,height=10)
topframe.place(x=100,y=50)

centerframe=Frame(root,pady=50,width=30,height=50,bg='black')
centerframe.place(x=210,y=200)


bottomframe=Frame(root,bg="black",bd=0,padx=150,pady=40)
bottomframe.place(x=30,y=520)

rightframe=Frame(root,padx=30,pady=20,bg="black",width=50,height=15)
rightframe.place(x=980,y=50)


image50=PhotoImage(file="50-50.png")
image50x=PhotoImage(file="50-50-X.png")

ll50=Button(topframe,image=image50,bg="black",bd=0,activebackground="black",width=250,height=150,cursor='hand2',command=Lyfeline50)
ll50.grid(row=0,column=1)

audiencepol=PhotoImage(file="audiencePole.png")
audiencepolx=PhotoImage(file="audiencePoleX.png")

llaudiencepol=Button(topframe,image=audiencepol,bg="black",bd=0,activebackground="black",width=200,height=90,cursor='hand2',command=audiencepolelifeline)
llaudiencepol.grid(row=0,column=2)

phonofriend=PhotoImage(file="phoneAFriend.png")
phonofriendx=PhotoImage(file="phoneAFriendX.png")

llphonofrnd=Button(topframe,image=phonofriend,bg="black",bd=0,activebackground="black",width=200,height=90,cursor='hand2',command=phonelifeline)
llphonofrnd.grid(row=0,column=3)

callimage=PhotoImage(file='phone.png')

callbutton=Button(root,image=callimage,bg='black',bd=0,activebackground='black',cursor='hand2',command=phoneclick)

kbclogoimage=Image.open('miliniorlogo3.jpeg')
kbclogoimage1=ImageTk.PhotoImage(kbclogoimage)


logolable=Label(centerframe,image=kbclogoimage1,bg="black",width=500,height=300,activebackground="black")
logolable.grid(row=0,column=2)

chart0=PhotoImage(file="Picture0.png")
chart1=PhotoImage(file="Picture1.png")
chart2=PhotoImage(file="Picture2.png")
chart3=PhotoImage(file="Picture3.png")
chart4=PhotoImage(file="Picture4.png")
chart5=PhotoImage(file="Picture5.png")
chart6=PhotoImage(file="Picture6.png")
chart7=PhotoImage(file="Picture7.png")
chart8=PhotoImage(file="Picture8.png")
chart9=PhotoImage(file="Picture9.png")
chart10=PhotoImage(file="Picture10.png")
chart11=PhotoImage(file="Picture11.png")
chart12=PhotoImage(file="Picture12.png")
chart13=PhotoImage(file="Picture13.png")
chart14=PhotoImage(file="Picture14.png")

chart=[chart0,chart1,chart2,chart3,chart4,
       chart5,chart6,chart7,chart8,chart9,
       chart10,chart11,chart12,chart13,chart14
       ]


chrtimagelable=Label(rightframe,image=chart0,bg="black",width=500,height=900)
chrtimagelable.grid(row=0,column=0)

layimage=PhotoImage(file="lay.png")

layimage1=Label(bottomframe,image=layimage,bg="black")
layimage1.grid(row=0,column=1)

question_area=Text(bottomframe,font=("Copperplate Gothic Bold",14,"bold"),wrap="word",width=28,height=2,bg="black",fg="#F8F8FF",bd=0)
question_area.place(x=74,y=12)

question_area.insert(END,questions[0])

LabelA=Label(bottomframe,text="A:",bg="black",fg="white",font=("Copperplate Gothic Bold",15,"bold"))
LabelA.place(x=40,y=110)

LabelB=Label(bottomframe,text="B:",bg="black",fg="white",font=("Copperplate Gothic Bold",15,"bold"))
LabelB.place(x=320,y=110)

LabelC=Label(bottomframe,text="C:",bg="black",fg="white",font=("Copperplate Gothic Bold",15,"bold"))
LabelC.place(x=40,y=190)

LabelD=Label(bottomframe,text="D:",bg="black",fg="white",font=("Copperplate Gothic Bold",15,"bold"))
LabelD.place(x=320,y=190)

optionbutton1=Button(bottomframe,text=first_option[0],font=("Copperplate Gothic Bold",15,"bold"),bd=0,fg="white",bg="black",activebackground="black",activeforeground="white",cursor="hand2")
optionbutton1.place(x=74,y=105)

optionbutton2=Button(bottomframe,text=second_option[0],font=("Copperplate Gothic Bold",15,"bold"),bd=0,fg="white",bg="black",activebackground="black",activeforeground="white",cursor="hand2")
optionbutton2.place(x=350,y=105)

optionbutton3=Button(bottomframe,text=third_option[0],font=("Copperplate Gothic Bold",15,"bold"),bd=0,fg="white",bg="black",activebackground="black",activeforeground="white",cursor="hand2")
optionbutton3.place(x=70,y=185)

optionbutton4=Button(bottomframe,text=fourth_option[0],font=("Copperplate Gothic Bold",15,"bold"),bd=0,fg="white",bg="black",activebackground="black",activeforeground="white",cursor="hand2")
optionbutton4.place(x=350,y=185)

progressbarA=Progressbar(root,orient=VERTICAL,length=120)
progressbarB=Progressbar(root,orient=VERTICAL,length=120)
progressbarC=Progressbar(root,orient=VERTICAL,length=120)
progressbarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarlblA=Label(root,text="A",font=("Copperplate Gothic Bold",17,"bold"),bg="black",fg="white")
progressbarlblB=Label(root,text="B",font=("Copperplate Gothic Bold",17,"bold"),bg="black",fg="white")
progressbarlblC=Label(root,text="C",font=("Copperplate Gothic Bold",17,"bold"),bg="black",fg="white")
progressbarlblD=Label(root,text="D",font=("Copperplate Gothic Bold",17,"bold"),bg="black",fg="white")



optionbutton1.bind('<Button-1>',select)
optionbutton2.bind('<Button-1>',select)
optionbutton3.bind('<Button-1>',select)
optionbutton4.bind('<Button-1>',select)




root.mainloop()


