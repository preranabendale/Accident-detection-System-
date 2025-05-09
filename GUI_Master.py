import tkinter as tk
from PIL import Image , ImageTk
import csv
from datetime import date
import time
import numpy as np
import cv2
from tkinter.filedialog import askopenfilename
import os
import shutil
#from skimage import measure
import Train_FDD_cnn as TrainM

#==============================================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Exam Suspicious Activity Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img78.jpg')
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





#
label_l1 = tk.Label(root, text="Accident detection",font=("Times New Roman", 30, 'bold'),
                    background="#B0E0E6", fg="black", width=70, height=2)
label_l1.place(x=0, y=0)

#============================================================================================================
def create_folder(FolderN):
    
    dst=os.getcwd() + "\\" + FolderN         # destination to save the images
    
    if not os.path.exists(dst):
        os.makedirs(dst)
    else:
        shutil.rmtree(dst, ignore_errors=True)
        os.makedirs(dst)


def CLOSE():
    root.destroy()
#####==========================================================================================================
    
def update_label(str_T):
    # clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25),bg='cyan',fg='black' )
    result_label.place(x=400, y=400)

def train_model():
    Train = ""
    update_label("Model Training Start...............")
    
    start = time.time()

    X=TrainM.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    update_label(msg)

###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    


def run_video(VPathName,XV,YV,S1,S2):

    cap = cv2.VideoCapture(VPathName)
#    cap.set(cv2.CAP_PROP_FPS, 30)

#    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'mp4v'))
    def show_frame():
                    
        ret, frame = cap.read()
        cap.set(cv2.CAP_PROP_FPS, 30)
               
        out=cv2.transpose(frame)
    
        out=cv2.flip(out,flipCode=0)
    
        cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        img   = Image.fromarray(cv2image).resize((S1, S2))
    
        imgtk = ImageTk.PhotoImage(image = img)
        
        lmain = tk.Label(root)
#        lmain.place(x=560, y=190)
        lmain.place(x=XV, y=YV)

        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
                
                
    show_frame()
        
def VIDEO():
    
    global fn
    
    fn=""
    fileName = askopenfilename(initialdir='C:/Users/COMPUTER/Desktop/vaish/Exam Video/', title='Select image',
                               filetypes=[("all files", "*.*")])

    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)
            
    if Sel_F!= 'MOV':
        print("Select Video .mp4 File!!!!!!")
    else:
        run_video(fn,560, 190,753, 485)

                
  
     
def mail():
    import smtplib
    from email.message import EmailMessage
    import imghdr

    Sender_Email = "shrutipatil42003@gmail.com"
    Reciever_Email = "ankita.sctcode@gmail.com"

    Password ='wppb hwrp xbvg ctpo'
    newMessage = EmailMessage()    #creating an object of EmailMessage class
    newMessage['Subject'] = "Suspicious Activity Detection During Academic Examination" #Defining email subject
    newMessage['From'] = Sender_Email  #Defining sender email
    newMessage['To'] = Reciever_Email  #Defining reciever email


    import requests
    import json
    
    # send_url = "http://api.ipstack.com/check?access_key=f0aa3d883536c94977cb4060e2fc4ffb"
    # geo_req = requests.get(send_url)
    # geo_json = json.loads(geo_req.text)
    # latitude = geo_json['latitude']
    # longitude = geo_json['longitude']
    # city = geo_json['city']
    # print(latitude,' ----------',longitude,city)

    # newMessage.set_content('Hi,Please help me urgently... \n Here I attached mylocation: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)) #Defining email body
    with open('abc.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)

def show_FDD_video(video_path):
    ''' Display FDD video with annotated bounding box and labels '''
    from keras.models import load_model
    
    # video_path=r"D:\Alka_python_2019_20\FDD_Main\Video_File\fall-01.mp4"
    img_cols, img_rows = 64,64
    
    FALLModel=load_model('model.h5',compile=False)    #video = cv.VideoCapture(video_path);
    
    video = cv2.VideoCapture(video_path)
        
    # video = cv2.VideoCapture(0)


    if (not video.isOpened()):
        print("{} cannot be opened".format(video_path))
        # return False

    font = cv2.FONT_HERSHEY_SIMPLEX
    green = (0, 255, 0) 
    red = (0, 0, 255)
    # orange = (0, 127, 255)
    line_type = cv2.LINE_AA
    i=1
    
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        img=cv2.resize(frame,(img_cols, img_rows),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.array(img)
        
        X_img = img.reshape(-1, img_cols, img_rows, 1)
        X_img = X_img.astype('float32')
        
        X_img /= 255
        
        predicted =FALLModel.predict(X_img)
        print(predicted[0][0])
        if predicted[0][0] < 0.5:
            predicted[0][0] = 0
            predicted[0][1] = 1
            label = 0
        else:
            predicted[0][0] = 1
            predicted[0][1] = 0
            label = 1
          
        frame_num = int(i)  #.iloc[:1,0])
        # label = int(annotations['label'][i])
        label_text = ""
        
        
        color = (255, 255, 255)
        
        # if  label == 0 :
        #     label_text = "normal"
        #     color = red
            
        if label == 0 :
                    label_text = "Abnormal Activity "
                    color = red
                    cv2.imwrite('abc.png',img)
                    # video.release()
                    mail()
                    
                    # from subprocess import call
                    # call(["python","mail.py"])
      
        else:
             label_text = "Normal Activity"
             color = green

        frame = cv2.putText(
            frame, "Frame: {}".format(frame_num), (5, 30),
            fontFace = font, fontScale = 1, color = color, lineType = line_type
        )
        frame = cv2.putText(
            frame, "Label: {}".format(label_text), (5, 60),
            fontFace = font, fontScale =1, color = color, lineType = line_type
        )

        i=i+1
        cv2.imshow('FDD', frame)
        if cv2.waitKey(30) == 27:
            break

    video.release()
    cv2.destroyAllWindows()
    
    
       
###################################################################################################################  
def Video_Verify():
    
    global fn
    
#    fn=r"D:\Alka_python_2019_20\Alka_python_2019_20\Video Piracy\Piracy_Preserving\result.mp4"
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)
            
    if Sel_F!= 'MOV':
        show_FDD_video(fn)

        print("Select Video File!!!!!!")
    else:
        
        show_FDD_video(fn)
        # run_video(fn,520, 190,400,500)    
########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
        
   
###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            

# button5 = tk.Button(root,command = Video_Verify, text="Activity Detection", width=24,font=("Times new roman", 25, "bold"),bg="cyan",fg="black")
# button5.place(x=100,y=150)

button2 = tk.Button(root, text=" Open Video ",command=Video_Verify,width=12, height=1,font=('times', 20, ' bold '), bg="#B0E0E6", fg="black")
button2.place(x=400, y=250)

button3 = tk.Button(root, text="Exit",command=CLOSE,width=12, height=1,font=('times', 20, ' bold '), bg="#B0E0E6", fg="black")
button3.place(x=400, y=330)


# button5 = tk.Button(root,command = train_model, text="train", width=20,font=("Times new roman", 25, "bold"),bg="cyan",fg="black")
# button5.place(x=100,y=225)

# close = tk.Button(root,command = CLOSE, text="Exit", width=20,font=("Times new roman", 25, "bold"),bg="red",fg="white")
# close.place(x=100,y=300)


root.mainloop()






