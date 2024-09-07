import time
import pyotp
import qrcode


key = "gurucharan"


uri = pyotp.totp.TOTP(key).provisioning_uri(
  name="gurucharan"
  issuer_name="mywebpage"
)

uri = pyotp.totp.TOTP(key).provisioning_uri(

name="Gurucharan R",
issuer_name="Charan webpage")

print(uri)
qrcode.make(uri).save("qr.png") 

totp = pyotp.TOTP(key) 
  
# verifying the code 
while True: 
  print(totp.verify(input(("Enter the Code : "))))
