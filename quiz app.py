from tkinter import*
from tkinter.font import*
import random
import os

global m
m=1
def im1():
    global label8
    label8=Label(window,image=image1,height=150,width=150)
    label8.place(x=10,y=2)

def im2():
    global label9
    label9=Label(window,image=image2,height=150,width=150)
    label9.place(x=174,y=2)


def im3():
     global label10
     label10=Label(window,image=image3,height=150,width=150)
     label10.place(x=338,y=2)

# def homepage():
#     m=3
#     print("hello abrar ahamad")
#     im1()
#     im2()
#     im3()

def destroy_home_and_other():
    #destroying homepage content to open python quiz
    label8.destroy()
    label9.destroy()
    label10.destroy()
    HomePageNote.destroy()

def login_page_destroy():
    global entry1, entry2, entry3
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()

    entry1.destroy()
    entry2.destroy()
    entry3.destroy()

    r1.destroy()
    r2.destroy()
    r3.destroy()

    button1.destroy()
    button3.destroy()

# we will going to generate random number for display random question
sequences = []
def gen():
    global sequences
    while (len(sequences) < 6):    #only 10 question will show in the quiz
        x = random.randint(0, 14)
        if x in sequences:
            continue
        else:
            sequences.append(x)
        # note:: we can write direct  sequences.append(x)  but when it generate same random number then
        # same number(question) will come in the question so we write here if else condition
    print(sequences)

def delete1():
    window1.destroy()

def delete2():
    window2.destroy()

def delete3():
    window3.destroy()


def user_not_found():
    global window1
    window1=Toplevel(window)
    # window1.config(background="lightblue")
    # window1.title("")
    window1.geometry("350x100+180+165")
    Label(window1,text="User not found,Sign up first!!",font=nav_font).pack()
    Button(window1,text="OK",command=delete1,font=("italic",15),width=5).pack()

def regnum_not_recognize():
    global window2
    window2=Toplevel(window)
    # window2.title("")
    window2.geometry("360x100+180+165")
    Label(window2,text="Entered reg number or Section is wrong!!",font=nav_font).pack()
    Button(window2,text="OK",command=delete2,font=("italic",15),width=5).pack()


def sec_not_recognize():
    global window3
    window3=Toplevel(window)
    # window3.title("")
    window3.geometry("350x100+180+165")
    Label(window3,text="Entered section is wrong!!",font=nav_font).pack()
    Button(window3,text="OK",command=delete3,font=("italic",15),width=5).pack()


def startispressed():
        login_page_destroy()

        gen()
        # if we write after startQuiz() then error::list index out of range bcoz list will empty before execut in gen()

        global username_verify, regnumber_verify, section_verify

        username1 = username_verify.get()
        regnumber1 = regnumber_verify.get()
        section1 = section_verify.get()


        list_of_files = os.listdir()
        print(list_of_files)
        if username1 in list_of_files:
            file1 = open(username1,"r")
            verify = file1.read().splitlines()
            if regnumber1 in verify:
                if section1 in verify:
                    # login_succes()
                    startQuiz()
                else:
                    Python_quiz()
                    sec_not_recognize()

            else:

                Python_quiz()
                regnum_not_recognize()
        else:

            Python_quiz()
            user_not_found()


def sign_up():
    login_page_destroy()
    # mcq_question_page_destroy()
    destroy_home_and_other()
    signup_page()

#form validation
def Name_validation(num):

        if num is " ":
            return True
        elif num is ".":
            return True
        elif num.isalpha():      #for string if one char will digit then it return false
            return True
        elif num is "":
            return True
        else:
            return False


def regN_validation(num):
        if num.isdigit():
            return True
        elif num is "":
            return True
        else:
            return False

def sec_validation(num):
        if num.isdigit():
            return True
        elif num is "":
            return True
        elif num.isalpha():
            return True
        else:
            return False

def show_result(mark):
    labelQuestion.destroy()
    rq1.destroy()
    rq2.destroy()
    rq3.destroy()
    rq4.destroy()
    button2.destroy()
    labelNote.destroy()

    labelimage=Label(window,)
    labelimage.pack()
    labelresulttext=Label(window, font = ("consolas",20),
                          )
    labelresulttext.pack()
    if mark > 20:
        img=PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\excellent.gif")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You are excellent!!",bg="lightblue",font=nav_font4,fg="green")
    elif (mark>=10 and mark <= 20):
        img = PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\mediam performance.gif")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You can be better!!",bg="lightblue",font=nav_font4,fg="orange")
    else:
        img = PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\poor perform.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You should work hard!!",bg="lightblue",font=nav_font4,fg="red")

    label15=Label(text="Total obtained mark by you::", bg="lightblue",font=nav_font4)
    label15.place(x=20,y=210)

    label15 = Label(text=mark, bg="lightblue", font=nav_font4)
    label15.place(x=440, y=210)

    label15=Label(text="Correct Answer::", bg="lightblue",font=nav_font4,fg="green")
    label15.place(x=20,y=240)

    label15 = Label(text=a_correct, bg="lightblue", font=nav_font4,fg="green")
    label15.place(x=270, y=240)

    label15=Label(text="Wrong Answer::", bg="lightblue",font=nav_font4,fg="red")
    label15.place(x=20,y=270)

    label15 = Label(text=a_wrong, bg="lightblue", font=nav_font4,fg="red")
    label15.place(x=260, y=270)




def calculate():
    global choosed_answer,correct_answer,sequences,X   # X is use for hard,medium,easy radio button
    global a_correct,a_wrong
    x = 0
    score = 0
    a_correct = 0   # how many given answer is correct
    a_wrong = 0     # how many given answer is wrong
    if X == 1:
      for i in sequences:
        if choosed_answer[x] == correct_answer[i]:
            score += 5
            a_correct += 1
        else:
            a_wrong += 1
        x += 1
    elif X == 2:
        for i in sequences:
            if choosed_answer[x] == correct_answer1[i]:
                score += 5
                a_correct += 1
            else:
                a_wrong += 1
            x += 1
    else:
        for i in sequences:
            if choosed_answer[x] == correct_answer2[i]:
                score += 5
                a_correct += 1
            else:
                a_wrong += 1
            x += 1
    score -= 1*a_wrong
    show_result(score)


# selected() will tell that which question is selected and also show the next question
ques=1
def ques_next():
  global ques,y,rvar,X
  choosed_answer.append(y)
  if ques < 6:
      if X == 1:
          labelQuestion.config(text=questions[sequences[ques]])
          rq1["text"] = answer_options[sequences[ques]][0]
          rq2["text"] = answer_options[sequences[ques]][1]
          rq3["text"] = answer_options[sequences[ques]][2]
          rq4["text"] = answer_options[sequences[ques]][3]
      elif X == 2:
          labelQuestion.config(text=questions1[sequences[ques]])
          rq1["text"] = answer_options1[sequences[ques]][0]
          rq2["text"] = answer_options1[sequences[ques]][1]
          rq3["text"] = answer_options1[sequences[ques]][2]
          rq4["text"] = answer_options1[sequences[ques]][3]
      else:
          labelQuestion.config(text=questions2[sequences[ques]])
          rq1["text"] = answer_options2[sequences[ques]][0]
          rq2["text"] = answer_options2[sequences[ques]][1]
          rq3["text"] = answer_options2[sequences[ques]][2]
          rq4["text"] = answer_options2[sequences[ques]][3]

      # showing next question

  else:
      calculate()
  ques += 1
  print(choosed_answer)


choosed_answer = []
def selected():
    print("option selected at the index")
    global rvar, choosed_answer,y,X
    global labelQuestion, rq1, rq2, rq3, rq4
    global ques
    y = rvar.get()
    X=radvar.get()


def delete4():
    window4.destroy()

def user_registered():
    global window4
    window4=Toplevel(window)
    # window4.config(background="lightblue")
    # window4.title("")
    window4.geometry("350x100+180+165")
    Label(window4,text="User registered successfully!!",font=nav_font).pack()
    Button(window4,text="OK",command=delete4,font=("italic",15),width=5).pack()


def register_user():
    global username, regnumber,section
    username_info = username.get()
    reg_info = regnumber.get()
    section_info=section.get()

    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(reg_info+"\n")
    file.write(section_info)

    entry11.delete(0, END)
    entry22.delete(0, END)
    entry33.delete(0, END)

    user_registered()


questions = [" Is Python case sensitive when dealing with identifiers?",
               " Which of these in not a core data type?",
               "Which of the following statements create a dictionary?",
               "'a'+'bc'?",
               "The output of executing string.ascii_letters can also be achieved by:?",
               " print(0xA + 0xB + 0xC)?",
               "Which of the following commands will create a list?",
               " Suppose list1 is [2445,133,12454,123], what is max(list1)??",
                "Which of the following functions is a built-in function in python?",
               "round(4.576)?",
               "The function pow(x,y,z) is evaluated as:?",
               "import math\n"
                "abs(math.sqrt(25))?",
               "Suppose t = (1, 2, 4, 3), which of the following is incorrect?",
               "To include the use of functions which are present in the random library, we must use the option:?",
               " which is used to create an object.?",
                                                       ]
answer_options = [["yes", "No", "Machine dependent", "none of these", ],
             ["Tuple", "Class", "Tuple", "Dictonary", ],
             [" d = {}", " d = {“john”:40, “peter”:45}", "d = {40:”john”, 45:”peter”}", " All of the mentioned", ],
             ["a", "bc", "bca", "abc", ],
             ["string.ascii_lowercase_string.digits", "string.ascii_lowercase+string.ascii_upercase", " string.letters", " string.lowercase_string.upercase", ],
             ["0xA0xB0xC", "Error", "0X22", "33", ],
             ["list1 = list()", " list1 = []", " list1 = list([1, 2, 3])", "all of the mentioned", ],
             ["2445" , "133", "12454", "123",],
             ["seed()", "sqrt()", " factorial()", "print()", ],
             ["4.5", "5", "4", "4.6", ],
             ["(x**y)**z", "(x**y) / z", "(x**y) % z", "(x**y)*z", ],
             ["error", "-5", "5", "5.0", ],
             ["print(t[3])", "t[3] = 45", "print(max(t))", "print(len(t))", ],
             ["import random", "random.h", "import.random", "random.random", ],
             ["class", "constructor", "User-defined functions", "In-built functions", ],
                                    ]

correct_answer = [0,1,3,3,1,1,3,2,3,1,2,3,1,0,1]   #here i gave the sequence(index)


questions1 = [" medium Is Python case sensitive when dealing with identifiers?",
               " medium Which of these in not a core data type?",
               " medium Which of the following statements create a dictionary?",
               " medium Python is which type of language4 ?",
               " medium Python is which type of language5 ?",
               " medium Python is which type of language6 ?",
               " medium Python is which type of language7 ?",
               "Python is which type of language8 ?",
               "Python is which type of language9 ?",
               "Python is which type of language10 ?",
               "Python is which type of language11 ?",
               "Python is which type of language12 ?",
               "Python is which type of language13 ?",
               "Python is which type of language14 ?",
               "Python is which type of language15 ?",
                                                       ]
answer_options1 = [["m yes", "No", "Machine dependent", "none of these", ],
             [" m Tuple", "Class", "Tuple", "Dictonary", ],
             ["m  d = {}", " d = {“john”:40, “peter”:45}", "d = {40:”john”, 45:”peter”}", " All of the mentioned", ],
             ["m 1", "2", "3", "4", ],
             ["m 1", "2", "3", "4", ],
             ["m 1", "2", "3", "4", ],
             ["m 1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
                                    ]

correct_answer1 = [0,1,3,2,0,1,3,1,1,2,0,1,0,3,2,]   #here i gave the sequence(index)

questions2 = [" hard Is Python case sensitive when dealing with identifiers?",
               " hard Which of these in not a core data type?",
               " hard Which of the following statements create a dictionary?",
               " hard Python is which type of language4 ?",
               " hard Python is which type of language5 ?",
               " hard Python is which type of language6 ?",
               " hard Python is which type of language7 ?",
               "Python is which type of language8 ?",
               "Python is which type of language9 ?",
               "Python is which type of language10 ?",
               "Python is which type of language11 ?",
               "Python is which type of language12 ?",
               "Python is which type of language13 ?",
               "Python is which type of language14 ?",
               "Python is which type of language15 ?",
                                                       ]
answer_options2 = [["h yes", "No", "Machine dependent", "none of these", ],
             ["h Tuple", "Class", "Tuple", "Dictonary", ],
             ["h d = {}", " d = {“john”:40, “peter”:45}", "d = {40:”john”, 45:”peter”}", " All of the mentioned", ],
             ["h 1", "2", "3", "4", ],
             ["h 1", "2", "3", "4", ],
             ["h 1", "2", "3", "4", ],
             ["h 1", "2", "3", "4", ],
             ["h 1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
             ["1", "2", "3", "4", ],
                                    ]

correct_answer2 = [0,1,3,2,0,1,3,1,1,2,0,1,0,3,2,]   #here i gave the sequence(index)

window=Tk()
window.config(background="lightblue")
window.resizable(0,0)
window.title("Learning app")

p_image = PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\images.gif")
p1_image = PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\today quiz.gif")
nav_font = Font(size=15, family="Times New Roman")
nav_font1 = Font(size=20, family="italic")
nav_font2 = Font(size=12, family="Times New Roman")
nav_font3 = Font(size=16, family="Times New Roman")
nav_font4 = Font(size=20, family="Lucida Calligraphy")



def startQuiz():
  global labelQuestion,rq1,rq2,rq3,rq4,button2
  global labelNote
  global rvar,radvar
  rvar=IntVar()
  rvar.set(-1)
  #set(-1) bydefault check one radio button

  X=radvar.get()
  if X == 1:
      labelQuestion = Label(window, text=questions[sequences[0]],
                        font=("italic", 17), width=500, wraplength=400, justify="center",
                        bg="lightblue", )
      labelQuestion.pack()

      rq1=Radiobutton(window,text=answer_options[sequences[0]][0],bg="lightblue",
                        font=(("italic",16)),value=0,variable=rvar,command=selected,)
      rq1.pack()
    #in rq1 we write sequences[0] bcoz we want to show the answer choices corresponding to questions

      rq2=Radiobutton(window,text=answer_options[sequences[0]][1],bg="lightblue",
                        font=(("italic",16)),value=1,variable=rvar,command=selected,)
      rq2.pack()

      rq3 = Radiobutton(window, text=answer_options[sequences[0]][2], bg="lightblue",
                          font=("italic", 16), value=2, variable=rvar,command=selected,)
      rq3.pack()

      rq4=Radiobutton(window,text=answer_options[sequences[0]][3],bg="lightblue",
                        font=("italic",16),value=3 ,variable=rvar,command=selected,)
      rq4.pack()

      button2 = Button(window, text="Next", font=nav_font4, fg="green", bg="pink", relief="flat",
                   command=ques_next)
      button2.pack()
  elif X ==  2:
      labelQuestion = Label(window, text=questions1[sequences[0]],
                            font=("italic", 17), width=500, wraplength=400, justify="center",
                            bg="lightblue", )
      labelQuestion.pack()

      rq1 = Radiobutton(window, text=answer_options1[sequences[0]][0], bg="lightblue",
                        font=(("italic", 16)), value=0, variable=rvar, command=selected, )
      rq1.pack()
      # in rq1 we write sequences[0] bcoz we want to show the answer choices corresponding to questions

      rq2 = Radiobutton(window, text=answer_options1[sequences[0]][1], bg="lightblue",
                        font=(("italic", 16)), value=1, variable=rvar, command=selected, )
      rq2.pack()

      rq3 = Radiobutton(window, text=answer_options1[sequences[0]][2], bg="lightblue",
                        font=("italic", 16), value=2, variable=rvar, command=selected, )
      rq3.pack()

      rq4 = Radiobutton(window, text=answer_options1[sequences[0]][3], bg="lightblue",
                        font=("italic", 16), value=3, variable=rvar, command=selected, )
      rq4.pack()

      button2 = Button(window, text="Next", font=nav_font4, fg="green", bg="pink", relief="flat",
                       command=ques_next)
      button2.pack()
  else:
      labelQuestion = Label(window, text=questions2[sequences[0]],
                            font=("italic", 17), width=500, wraplength=400, justify="center",
                            bg="lightblue", )
      labelQuestion.pack()

      rq1 = Radiobutton(window, text=answer_options2[sequences[0]][0], bg="lightblue",
                        font=(("italic", 16)), value=0, variable=rvar, command=selected, )
      rq1.pack()
      # in rq1 we write sequences[0] bcoz we want to show the answer choices corresponding to questions

      rq2 = Radiobutton(window, text=answer_options2[sequences[0]][1], bg="lightblue",
                        font=(("italic", 16)), value=1, variable=rvar, command=selected, )
      rq2.pack()

      rq3 = Radiobutton(window, text=answer_options2[sequences[0]][2], bg="lightblue",
                        font=("italic", 16), value=2, variable=rvar, command=selected, )
      rq3.pack()

      rq4 = Radiobutton(window, text=answer_options2[sequences[0]][3], bg="lightblue",
                        font=("italic", 16), value=3, variable=rvar, command=selected, )
      rq4.pack()

      button2 = Button(window, text="Next", font=nav_font4, fg="green", bg="pink", relief="flat",
                       command=ques_next)
      button2.pack()

  labelNote = Label(window, text="Note::\n1) One question is for 5 mark and if one question will wrong then you'll get -1 mark",
                    fg="purple",font=nav_font4, bg="lightblue", width=500, wraplength=400, justify="center" )
  labelNote.pack()


def signup_page():
    global window5,m
    m=2
    window5 = Toplevel(window)
    window5.config(background="lightblue")
    window5.title("Learning app")
    window5.geometry("500x450+120+120")

    global username, regnumber,section
    global entry11,entry22,entry33
    global label1,label12,label13
    global button11,button12

    username=StringVar()
    regnumber=StringVar()
    section=StringVar()

    label11 = Label(window5, text="Name:",
                   font=nav_font1,
                   bg="lightblue")
    label11.place(x=50, y=50)

    entry11 = Entry(window5, textvariable=username, font=nav_font)
    # entry1.insert(0,"Enter your name...........")      it is same as value
    entry11.place(x=155, y=59, height=25, width=250)
    reg = window5.register(Name_validation)
    entry11.config(validate="key", validatecommand=(reg, "%S"))

    label12 = Label(window5, text="Reg No:",
                   font=nav_font1,
                   bg="lightblue")
    label12.place(x=50, y=90)

    entry22 = Entry(window5, textvariable=regnumber, font=nav_font, )
    entry22.place(x=155, y=99, height=25, width=250)
    reg1 = window5.register(regN_validation)
    entry22.config(validate="key", validatecommand=(reg1, "%P"))

    label13 = Label(window5, text="Section:",
                   font=nav_font1,
                   bg="lightblue")
    label13.place(x=50, y=130)

    entry33 = Entry(window5, textvariable=section, font=nav_font)
    entry33.place(x=155, y=139, height=25, width=250)
    reg2 = window5.register(sec_validation)
    entry33.config(validate="key", validatecommand=(reg2, "%S"))

    button11 = Button(window5, text="Register", font=nav_font4, fg="green", bg="pink", relief="groove",
                             command=register_user)
    button11.place(x=180, y=185, height=40, width=190)

    button12 = Button(window5, text="Go to login page", font=nav_font4, fg="green", bg="pink", relief="groove",
                             command=Python_quiz)
    button12.place(x=150, y=230, height=40, width=245)

# after clicking the PYTHON QUIZ following code will be execute
def Python_quiz():
    #homepage widgets destroying
    main_menu.destroy()
    if m == 2:
      window5.destroy()


    global username_verify, regnumber_verify, section_verify
    global label1,label2,label3,label4,label5
    global label11


    global entry1, entry2, entry3
    global r1,r2,r3
    global button1,button3


    username_verify = StringVar()
    regnumber_verify = StringVar()
    section_verify = StringVar()

    global radvar
    radvar = IntVar()
    radvar.set(-1)

    destroy_home_and_other()
    label1=Label(window,image=p_image,height=108,width=210)
    # canvas1=Canvas(window,height=108,width=210)
    # canvas1.create_image(0,0,image=p1_image,anchor=NW)
    label1.place(x=155,y=8)

    #creating form
    label2= Label(window,text="Name:",
                  font=nav_font1,
                 bg="lightblue")
    label2.place(x=50,y=120)
    entry1=Entry(window,textvariable=username_verify,font=nav_font)
    #entry1.insert(0,"Enter your name...........")      it is same as value
    entry1.place(x=155,y=129,height=25,width=250)
    reg = window.register(Name_validation)
    entry1.config(validate="key", validatecommand=(reg,"%S"))

    label3= Label(window,text="Reg No:",
                font=nav_font1,
                bg="lightblue")
    label3.place(x=50,y=160)

    entry2=Entry(window,textvariable=regnumber_verify,font=nav_font,)
    entry2.place(x=155,y=169,height=25,width=250)
    reg1=window.register(regN_validation)
    entry2.config(validate="key",validatecommand=(reg1,"%P"))

    label4= Label(window,text="Section:",
                  font=nav_font1,
                  bg="lightblue")
    label4.place(x=50,y=200)

    entry3=Entry(window,textvariable=section_verify,font=nav_font)
    entry3.place(x=155,y=209,height=25,width=250)
    reg2 = window.register(sec_validation)
    entry3.config(validate="key", validatecommand=(reg2,"%S"))

    label5 = Label(window, text="Choose\nlevel:",
                  font=nav_font1,
                   bg="lightblue")
    label5.place(x=50, y=260)

  #radiobutton
    r1=Radiobutton(window,text="Easy",bg="lightblue",font=nav_font3,value=1,variable=radvar)
    r1.place(x=175,y=250,)

    r2 = Radiobutton(window, text="Medium",bg="lightblue", font=nav_font3,value=2,variable=radvar)
    r2.place(x=175, y=280, )

    r3 = Radiobutton(window, text="Tough",bg="lightblue", font=nav_font3,value=3,variable=radvar)
    r3.place(x=175, y=310 )

    button3 = Button(window, text="Sign Up", font=nav_font4, fg="green", bg="pink", relief="flat",
                  command=sign_up)
    button3.place(x=70, y=350, width=180)

    button1=Button(window,text="Start Quiz",font=nav_font4,fg="green",bg="pink",relief="flat",command=startispressed)
    button1.place(x=255,y=350,width=180)


main_menu=Menu(window)

#  home
homemenu=Menu(main_menu)
main_menu.add_command(label="Home")

#course
course_menu=Menu(main_menu)
main_menu.add_cascade(label="Course",menu=course_menu)
course_menu.add_command(label="C")
course_menu.add_command(label="C++")
course_menu.add_command(label="java")
course_menu.add_command(label="python")

#quiz
quiz_menu=Menu(main_menu)
main_menu.add_cascade(label="Quiz",menu=quiz_menu)
quiz_menu.add_command(label="C quiz")
quiz_menu.add_command(label="C++ quiz")
quiz_menu.add_command(label="java quiz")
quiz_menu.add_command(label="python quiz",command=Python_quiz)


window.config(menu=main_menu)

image1=PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\images.gif")
image2=PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\today quiz.gif")
image3=PhotoImage(file="C:\\Users\\ABRAR AHAMAD\\Documents\\Computer-Science-Interview-questions.gif")

#adding a Note to the home page
HomePageNote = Label(window, text="Note::To give the quiz comptition go to\nQuiz tab then click on python quiz, \nit will directed to the login page\nCommand:: Quiz -> python quiz",
                  font=nav_font1,
                   bg="lightblue",
                   fg="navyblue")
HomePageNote.place(x=20, y=175)

im1()
im2()
im3()

window.geometry("500x450+120+120")
window.mainloop()