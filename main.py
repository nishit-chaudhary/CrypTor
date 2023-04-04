from tkinter import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
from cryptography.fernet import Fernet
from PyPDF2 import PdfFileWriter, PdfFileReader
import time
import random
from base64 import b64encode
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from twilio.rest import Client
from Crypto.PublicKey import RSA

fromaddr = "example@mail.com"
password = "password"

account_sid = "Your account sid"
auth_token = "Your authentication token"

f = open("public.pem", "r")
pub_key = RSA.import_key(f.read())
f.close()

#--------------------------------------------------------------------Send Msg-------------------------------------------------------------------------------------------#

def send_sms(phone_no,key):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="Key : "+key, from_=+15626207380, to=int (phone_no))
    
#--------------------------------------------------------------------Send Msg-------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------Send Email-----------------------------------------------------------------------------------------#

def send_email(filename,attatchment,toaddr,subject):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    
    body = subject
    msg.attach(MIMEText(body,'plain'))
    
    attatchment = open(attatchment,'rb')

    P = MIMEBase('application','octet-stream')
    P.set_payload((attatchment).read())
    encoders.encode_base64(P)

    P.add_header('Content-Disposition','attatchment : filename="%s"' % filename)
    msg.attach(P)

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromaddr,password)
    text = msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()


#--------------------------------------------------------------------Send Email-----------------------------------------------------------------------------------------#

#--------------------------------------------------------------------Encryption---------------------------------------------------------------------------------------
f = None

# ----------------------------------------------------------------------CSV-------------------------------------------------------------------------------------------- #

def file_encryption_csv(filename):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    p = filename.split("/")
    p[-1] = "encrypted.csv"
    p = "/".join(p)
    with open(p, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    key = key.decode('utf-8')
    Label(root, text='Key : '+str(key), background='#282828', foreground='#87ceeb').pack(side = TOP, pady=10)
    return key,p

def file_decryption_csv(key,p):
    key = key.encode('utf-8')
    fernet = Fernet(key)
    with open(p, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)
    p = p.split("/")
    p[-1] = "decrypted.csv"
    p = "/".join(p)
    with open(p, 'wb') as dec_file:
        dec_file.write(decrypted)


# ------------------------------------------------------------------------CSV --------------------------------------------------------------------#


#-----------------------------------------------------------------------------Word----------------------------------------------------------------#

def file_encryption_doc(filename):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    p = filename.split("/")
    p[-1] = "encrypted.doc"
    p = "/".join(p)
    with open(p, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    key = key.decode('utf-8')
    Label(root, text='Key : '+str(key), foreground='white').pack(side = TOP, pady=10)
    return key,p

def file_decryption_doc(key,p):
    key = key.encode('utf-8')
    fernet = Fernet(key)
    with open(p, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)
    p = p.split("/")
    p[-1] = "decrypted.doc"
    p = "/".join(p)
    with open(p, 'wb') as dec_file:
        dec_file.write(decrypted)


#-----------------------------------------------------------------------------Word----------------------------------------------------------------#

#----------------------------------------------------------------------------- image------------------------------------------------------------------------------------- #

def file_encryption_image(filename):
    key = random.randint(0,255)
    fin = open(filename,'rb')
    image = fin.read()
    fin.close()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(filename, 'wb')
    fin.write(image)
    fin.close()
    return key,filename

def file_decryption_image(key,p):
    key = int(key)
    fin = open(p,'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(p, 'wb')
    fin.write(image)
    fin.close()

# -----------------------------------------------------------------------image------------------------------------------------------------------------------------------- #

#------------------------------------------------------------------------mkv--------------------------------------------------------------------------------------------#
def file_encryption_movie(filename):
    key = random.randint(0,255)
    fin = open(filename,'rb')
    movie = fin.read()
    fin.close()
    movie = bytearray(movie)
    for index, values in enumerate(movie):
        movie[index] = values ^ key
    fin = open(filename, 'wb')
    fin.write(movie)
    fin.close()
    return key,filename

def file_decryption_movie(key,p):
    key = int(key)
    fin = open(p,'rb')
    movie = fin.read()
    fin.close()
    movie = bytearray(movie)
    for index, values in enumerate(movie):
        movie[index] = values ^ key
    fin = open(p, 'wb')
    fin.write(movie)
    fin.close()

#------------------------------------------------------------------------mkv--------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------audio---------------------------------------------------------------------------------------------#

def file_encryption_mp3(filename):
    key = random.randint(0,255)
    fin = open(filename,'rb')
    audio = fin.read()
    fin.close()
    audio = bytearray(audio)
    for index, values in enumerate(audio):
        audio[index] = values ^ key
    fin = open(filename, 'wb')
    fin.write(audio)
    fin.close()
    return key,filename

def file_decryption_mp3(key,p):
    key = int(key)
    fin = open(p,'rb')
    audio = fin.read()
    fin.close()
    audio = bytearray(audio)
    for index, values in enumerate(audio):
        audio[index] = values ^ key
    fin = open(p, 'wb')
    fin.write(audio)
    fin.close()


#---------------------------------------------------------------------audio---------------------------------------------------------------------------------------------#



# --------------------------------------------------------------password-generator--------------------------------------------------------------------------------------#

def generate_password():
    alphabets = ['a','b','c','d','e','f','g','h','i','j' 'k','l','m','n','o','p'
                 ,'q','r','s','t','u','v','w','x','y','z']
    chars = ['.','/',',','!','@','#','$','%','^','&','*',]
    nums = ['0','1','2','3','4','5','6','7','8','9']
    random.shuffle(alphabets)
    random.shuffle(chars)
    random.shuffle(nums)
    l = alphabets[:8]+chars[:3]+nums[:3]
    l = list(l)
    random.shuffle(l)
    l = "".join(l)
    return l


# -----------------------------------------------------------password-generator---------------------------------------------------------------------------------------- #

# ---------------------------------------------------------------pdf--------------------------------------------------------------------------------------------------- #

def file_encryption_pdf(filename):
    out = PdfFileWriter()
    file = PdfFileReader(filename)
    num = file.numPages

    for idx in range(num):
        page = file.getPage(idx)
        out.addPage(page)

    password = generate_password()
    out.encrypt(password)
    
    p = filename.split("/")
    p[-1] = "encrypted.pdf"
    p = "/".join(p)

    with open(p,'wb') as f:
        out.write(f)

    return password,p

def file_decryption_pdf(key,p):
    key = str(key)
    out = PdfFileWriter()
    file = PdfFileReader(p)
    password = key

    if file.isEncrypted:
        file.decrypt(password)
        for idx in range(file.numPages):
            page = file.getPage(idx)
            out.addPage(page)

    p = p.split("/")
    p[-1] = "decrypted.pdf"
    p = "/".join(p)

    with open(p, "wb") as f:
        out.write(f)

# ----------------------------------------------------------------------pdf-------------------------------------------------------------------------------------------- #



root = Tk()
root.geometry("400x700")
root.title("CrypTor: Encrypt and Decrypt Files")
root.configure(background='#28282B')

canvas = Canvas(root, width = 233, height = 250, bd=0, highlightthickness=0, relief='ridge')
canvas.config(bg='#28282B')
canvas.pack()

img1 = Image.open("./Assets/logo1.png")
image1 = img1.resize((233,250), Image.ANTIALIAS)
# set image border to 0
img = ImageTk.PhotoImage(image1)
canvas.create_image(0,0, anchor=NW, image=img)

def open_file():
    file = askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv'),('Image Files', ['.jpeg', '.jpg', '.png', '.gif','.tiff', '.tif', '.bmp']),('PDF Files', '*.pdf'),('Movie Files', ['.mkv','.mp4','.mov','.wmv','.avi']),('Audio Files', '*.mp3'),('Word Files', '*.doc')])
    if file is not None:
        global f
        f = str(file.name)
        pass

def Encrypt():
    if f is None:
        Label(root, text='Not uploaded a file yet!!',background='#282828', foreground='red').pack(side = TOP, pady=10)
    else:
        if(f[-3:]=="csv"):
            t,q = file_encryption_csv(f)
        elif(f[-3:]=="png"):
            t,q = file_encryption_image(f)
        elif(f[-4:]=="jpeg"):
            t,q = file_encryption_image(f)   
        elif(f[-3:]=="jpg"):
            t,q = file_encryption_image(f) 
        elif(f[-3:]=="gif"):
            t,q = file_encryption_image(f)
        elif(f[-4:]=="tiff"):
            t,q = file_encryption_image(f)
        elif(f[-3:]=="tif"):
            t,q = file_encryption_image(f)
        elif(f[-3:]=="bmp"):
            t,q = file_encryption_image(f)
        elif(f[-3:]=='pdf'):
            t,q = file_encryption_pdf(f)
        elif(f[-3:]=='mkv'):
            t,q = file_encryption_movie(f)
        elif(f[-3:]=='mp4'):
            t,q = file_encryption_movie(f)
        elif(f[-3:]=='mov'):
            t,q = file_encryption_movie(f)
        elif(f[-3:]=='wmv'):
            t,q = file_encryption_movie(f)
        elif(f[-3:]=='avi'):
            t,q = file_encryption_movie(f)
        elif(f[-3:]=='mp3'):
            t,q = file_encryption_mp3(f)
        elif(f[-3:]=='doc'):
            t,q = file_encryption_doc(f)      
        else:
            print(f[-3:])
    
    Label(root, text='File Encrypted Successfully!', foreground='green' ,background='#28282B').pack(side = TOP, pady=10)

    Label(root, text='Enter the Email Address you want to send the file',background='#282828', foreground='white').pack(side = TOP)
    emaddr = Entry(root)
    emaddr.pack(side=TOP,pady=5)

    Label(root, text='Enter the Phone Number you want to send the key',background='#282828', foreground='white').pack(side = TOP)
    phnno = Entry(root)
    phnno.pack(side=TOP,pady=5)


    def send_info(t):
        send_email("File",q,str(emaddr.get()),"Encrypted File")
        time.sleep(1)

        # Encrypt t with RSA pubic key
        t = bytes_to_long(t.encode())
        # print(t)
        enc = pow(t, pub_key.e, pub_key.n)
        enc = b64encode(long_to_bytes(enc)).decode()
        print(enc)
        send_sms("+91"+str(phnno.get()),enc)
        
    btn = Button(root, bg='#FAFA33', fg='#010101', text ='Send Info', command = lambda:send_info(t))
    btn.pack(side = TOP, pady = 5)
    print(t)
    print(q)

def Decrypt(key):
    key = key.get()
    if(f[-3:]=='csv'):
        try:
            file_decryption_csv(key,f)
            
            Label(root, text='File Decrypted Successfully!', foreground='green' ,background='#28282B').pack( side = TOP, pady=10)

        except:
            Label(root, text='Error', foreground='blue').pack(side = TOP,pady=10)

    elif(f[-3:]=='png' or f[-4:]=='jpeg' or f[-3:]=='jpg' or f[-3:]=='gif' or f[-4:]=='tiff' or f[-3:]=='tif' or f[-3:]=='bmp'):
        try:
            file_decryption_image(key,f)
            
            Label(root, text='File Decrypted Successfully!', foreground='green' ,background='#28282B').pack( side = TOP, pady=10)

        except:
            Label(root, text='Error', foreground='blue').pack(side = TOP,pady=10)

    elif(f[-3:]=='pdf'):
        try:
            file_decryption_pdf(key,f)
            
            Label(root, text='File Decrypted Successfully!', foreground='green' ,background='#28282B').pack( side = TOP, pady=10)

        except:
            Label(root, text='Error', foreground='blue').pack(side = TOP, pady=10)
    
    elif(f[-3:]=='mkv' or f[-3:]=='mp4' or f[-3:]=='avi' or f[-3:]=='wmv' or f[-3:]=='mov'):
        try:
            file_decryption_movie(key,f)
           
            Label(root, text='File Decrypted Successfully!', foreground='green' ,background='#28282B').pack( side = TOP, pady=10)

        except:
            Label(root, text='Error', foreground='blue').pack(side = TOP, pady=10)

    elif(f[-3:]=='mp3'):
        try:
            file_decryption_mp3(key,f)
            
            Label(root, text='File Decrypted Successfully!', foreground='green' ,background='#28282B').pack( side = TOP, pady=10)

        except:
            Label(root, text='Error', foreground='blue').pack(side = TOP, pady=10)
    
    elif(f[-3:]=='doc'):
        try:
            file_decryption_doc(key,f)
            
            Label(root, text='File Decrypted Successfully!', foreground='green' ,background='#28282B').pack( side = TOP, pady=10)

        except:
            Label(root, text='Error', foreground='blue').pack(side = TOP, pady=10)

    else:
        print(f[-3:])

# add space between logo1 and browse files btn
Label(root, text='', background='#28282B').pack()

btn = Button(root, bg='#FAFA33', fg='#010101', text ='Browse Files',command = lambda:open_file())
btn.pack(side = TOP, pady = 5)

upld = Button(root, bg='#FAFA33', fg='#010101', text='Encrypt', command=Encrypt)
upld.pack(side = TOP, pady=5)

Label(root, text='Enter the Decryption Key',background='#28282B', foreground='white').pack(side =TOP, pady=10)

inputtxt = Entry(root)
inputtxt.pack(side=TOP,pady=5)

dec = Button(root, bg='#FAFA33', fg='#010101', text='Decrypt',command = lambda:Decrypt(inputtxt))
dec.pack(side = TOP,pady = 5)

root.mainloop()
