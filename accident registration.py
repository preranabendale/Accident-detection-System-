import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os



root = tk.Tk()
root.configure(background="#fff")
# root.geometry("1300x700")

root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("registration")

#window = tk.Tk()
#Window.geometry("700x700+200+50")
#window.title("REGISTRATION FORM")
#window.configure(background="#85929e")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

# value = random.randint(1, 1000)
# print(value)

# # database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS new_reg"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno INTEGER,Gender INTEGER,Age INTEGER , password TEXT)")
db.commit()

def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 
def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM new_reg WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO new_reg(Fullname, address, username, Email, Phoneno, Gender, Age,password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time,pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            root.destroy()
            from subprocess import call
            call(["python", "accident login.py"])

#####################################################################################################################################################

#from subprocess import call
#call(["python", "lecture_login.py"])


# assign and define variable
# def login():

#####For background Image
image2 = Image.open('b1.jpg')
image2 = image2.resize((1550, 900), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


Login_frame = tk.LabelFrame(root, text="Registration Form", width=500, height=550, bd=5, font=('times',22, ' bold '),bg="black",fg="white")
Login_frame.grid(row=0, column=0, sticky='nw')
Login_frame.place(x=60, y=100)

#l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="black", fg="white")
#l1.place(x=190, y=50)

# that is for label1 registration

l2 = tk.Label(Login_frame, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="black",fg="white")
l2.place(x=65, y=15)
t1 = tk.Entry(root, textvar=Fullname, width=20, font=('', 15))
t1.place(x=310, y=150)
# that is for label 2 (full name)


l3 = tk.Label(root, text="Address :", width=12, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l3.place(x=130, y=200)
t2 = tk.Entry(root, textvar=address, width=20, font=('', 15))
t2.place(x=310, y=200)
# that is for label 3(address)


l5 = tk.Label(root, text="E-mail :", width=12, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l5.place(x=130, y=250)
t4 = tk.Entry(root, textvar=Email, width=20, font=('', 15))
t4.place(x=310, y=250)
# that is for email address

l6 = tk.Label(root, text="Phone number :", width=12, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l6.place(x=130, y=300)
t5 = tk.Entry(root, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=310, y=300)
# phone number
l7 = tk.Label(root, text="Gender :", width=12, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l7.place(x=130, y=350)
# gender
tk.Radiobutton(root, text="Male", padx=5, width=5, bg="#a6acaf", font=("bold", 15), variable=var, value=1).place(x=310,
                                                                                                                y=350)
tk.Radiobutton(root, text="Female", padx=20, width=4, bg="#a6acaf", font=("bold", 15), variable=var, value=2).place(
    x=420, y=350)

l8 = tk.Label(root, text="Age :", width=12, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l8.place(x=130, y=400)
t6 = tk.Entry(root, textvar=age, width=20, font=('', 15))
t6.place(x=310, y=400)

l4 = tk.Label(root, text="User Name :", width=12, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l4.place(x=130, y=450)
t3 = tk.Entry(root, textvar=username, width=20, font=('', 15))
t3.place(x=310, y=450)

l9 = tk.Label(root, text="Password :", width=12, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l9.place(x=130, y=500)
t9 = tk.Entry(root, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=310, y=500)

l10 = tk.Label(root, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"),  bg="black",fg="white")
l10.place(x=120, y=550)
t10 = tk.Entry(root, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=310, y=550)

btn = tk.Button(root, text="Register", bg="#0d73d1",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=230, y=620)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
root.mainloop()