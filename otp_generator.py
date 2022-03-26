import os
import math
import random
import smtplib
import re


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
digits="0123456789"
OTP=""
for i in range(3):
    
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP
b=""
for i in range(3):
    a=random.randint(97,123)
    b+=chr(a)
msg= otp+b
msgnew = "".join(random.sample(msg,len(msg)))


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("otpverify83@gmail.com", "lycyitoedkvqruuv")
emailid = input("Enter your email: ")
if(re.fullmatch(regex, emailid)):
        print("Valid Email")
        s.sendmail('&&&&&&&&&&&',emailid,msgnew)
        a = input("Enter Your OTP >>: ")
        if a == msgnew:
            print("Verified")
        else:
            print("Please Check your OTP again")
 
else:
    print("Invalid Email")




 

