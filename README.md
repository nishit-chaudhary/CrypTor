# CrypTor
This is a file encryption software which can encrypt and decrypt various file formats such as pdfs, csv, image, audio, video, etc. It sends the encrypted file through email and the key encrypted with RSA through SMS.
First you need to install following packages : cryptography, PyPDF2, twilio, pillow, secure-smtplib 
You will also need to create a twilio account and change the authentication token, account sid & the phone number. If you use a trial account, you won't be able to send sms to unverified accounts.
Then when you run the main.py the key will be encrypted using the receiver's public key, that will be sent in sms, the receiver will input the received key in key_decryptor.py
After that, the key which you get in key_decryptor.py can be used to decrypt the file received in email.
