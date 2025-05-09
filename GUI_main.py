import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="#104E8B")
root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Accident detection")


# ++++++++++++++++++++++++++++++++++++++++++++
#For background Image
image2 = Image.open('back2.jpg') 
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#label_l1 = tk.Label(root,background="#104E8B", fg="white", width=67, height=2)
#label_l1.place(x=0, y=0)

label=tk.Label(root,text="𝐀𝐂𝐂𝐈𝐃𝐄𝐍𝐓 𝐃𝐄𝐓𝐄𝐂𝐓𝐈𝐎𝐍",font=("Algerian",45),
               bg="black",fg="orange",
               width=44,
               height=1)
label.place(x=0,y=0)



#img = Image.open('road.png')
#logo_image = ImageTk.PhotoImage(img)
#img = img.resize((100,75), Image.LANCZOS)
#logo_label = tk.Label(root, image=logo_image)
#logo_label.image = logo_image
#logo_label.place(x=21, y=10)




#img=ImageTk.PhotoImage(Image.open("image4.jpg"))
#img2=ImageTk.PhotoImage(Image.open("image2.jpg"))
#img3=ImageTk.PhotoImage(Image.open("image3.jpg"))


#logo_label=tk.Label()
#logo_label.place(x=0,y=95)


#logo_label1=tk.Label(text='\n\n ...Road Pothole Detection Using YOLO v8... \n \n Road Pathole Identification: To detect potholes in road scenes in real time,\n the system makes use of YOLO v8 a cutting-edge \n object identification model .because of its great accuracy and speed in object \n detection tasks, YOLO V8 is a good choice for applications \n that need to analyze huge data sets quickly. \n \n',compound='bottom',font=("Times New Roman", 15, 'bold', 'italic'),bd=5,width=60, bg="snow", fg="black")
#logo_label=tk.Label(height=500, width=400)
#logo_label1.place(x=35,y=500)

#logo_label4=tk.Label(logo_label1,text='*****************************************************************',compound='bottom',font=("Times New Roman", 20, 'bold', 'italic'),bd=5,width=65, bg="#CD6090", fg="white")
#logo_label=tk.Label(height=500, width=400)
#logo_label4.place(x=0,y=0)

#logo_label4=tk.Label(logo_label1,text='****************************************************************',compound='bottom',font=("Times New Roman", 20, 'bold', 'italic'),bd=5,width=65, bg="#CD6090", fg="white")
#logo_label=tk.Label(height=500, width=400)
#logo_label4.place(x=0,y=260)

# using recursion to slide to next image
#x = 1



# function to change to next image
#def move():
	#global x
	#if x == 4:
		#x = 1
	#if x == 1:
		#logo_label.config(image=img,width=1800,height=700)
	#elif x == 2:
		#logo_label.config(image=img2,width=1800,height=700)
	#elif x == 3:
		#logo_label.config(image=img3,width=1800,height=700)
	#x = x+1
	#root.after(2000, move)

# calling the function
#move()
bg_icon=ImageTk.PhotoImage(file="back2.jpg")

frame_alpr = tk.LabelFrame(root, text=" --​🇱​​🇴​​🇬​​🇮​​🇳​ & ​🇷​​🇪​​🇬​​🇮​​🇸​​🇹​​🇪​​🇷​--", width=300, height=300, bd=5, font=('times', 20, ' bold '),bg="black",fg="orange")
frame_alpr.grid(row=3, column=3, sticky='nw')
frame_alpr.place(x=30, y=300)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def log():
    from subprocess import call
    call(["python","accident login.py"])
    #root.destroy()
    
def reg():
    from subprocess import call
    call(["python","accident registration.py"])
    #root.destroy()
    
def window():
  root.destroy()
  
  

#####################################################################################################################

button1 = tk.Button(frame_alpr, text="Login", command=log, width=15, height=1,font=('times', 14, ' bold '), bg="#0d73d1", fg="black")
button1.pack(pady=20)

button2 = tk.Button(frame_alpr, text="Registration",command=reg,width=15, height=1,font=('times', 14, ' bold '), bg="#0d73d1", fg="black")
button2.pack(pady=10)

button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=150, y=300)


#label_l1 = tk.Label(root, text="** Road Pythol Detection Using YOLOT @ 2021 by _____________ **",font=("Times New Roman", 10, 'bold'),
                   # background="black", fg="white", width=100, height=2)
#label_l1.place(x=400, y=798)


root.mainloop()