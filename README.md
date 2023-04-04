<h1 align="center">
  <br>
  <img src="./Assets/logo1.png" alt="CrypTor" width="200">
  <br>
</h1>

<h4 align="center">A file encryption software which can encrypt and decrypt various file formats such as pdfs, csv, image, audio, video, etc. It sends the encrypted file through email and the key encrypted with RSA through SMS.</h4>
<br>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#support">Support</a>
</p>

<!-- ![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif) -->

## Key Features

* File Encryption
  - Different encryptions algorithms defined for various file types, so you can use whichever one you like.
* Secured with RSA encryption
  - You can ask for the receiver's public key and encrypt the key with it.
* Sending encrypted file through email
* Sending encrypted key through SMS
* Decryption of file and key
  - The receiver can decrypt the file and key using the key decrypted with RSA using his own private key.

## How To Use

* First set up the email account you wish to send the mails from.
    - EmailID and password 
<br>

* You will also need to create a twilio account and change the authentication token, account sid & the phone number. If you use a trial account, you won't be able to send sms to unverified accounts. 

* From your command line:

```bash
# Clone this repository
$ git clone https://github.com/nishit-chaudhary/CrypTor.git

# Install dependencies (libraries required)
$ pip install cryptography PyPDF2 twilio pillow secure-smtplib 

# Run the rsa.py file to generate the public and private keys
$ python rsa.py

# Run the main.py file
$ python main.py
```

* From the receiver's command line:
```bash
# Clone this repository
$ git clone https://github.com/nishit-chaudhary/CrypTor.git

# Install dependencies (libraries required)
$ pip install cryptography PyPDF2 twilio pillow secure-smtplib 

# Run the rsa.py file to generate the public and private keys
$ python rsa.py

# Copy the key received from the sender and paste it in the terminal after running the key_decryptor.py file
$ python key_decryptor.py

# Copy the decrypted key and paste it after selecting the encrypted file when running the main.py file
$ python main.py
```
<br>

## Support

<br>

> GitHub [@nishit-chaudhary](https://github.com/nishit-chaudhary) &nbsp;&middot;&nbsp;
> LinkedIn [Nishit Chaudhary](https://www.linkedin.com/in/nishit-chaudhary-383a07229/)&nbsp;&middot;&nbsp;
> Instagram [@nishit._.chaudhary](https://www.instagram.com/nishit._.chaudhary/) 
