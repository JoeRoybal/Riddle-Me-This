import os
import cryptography
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def password():
    password_provided = "password" # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = b"\xf0R\xfcEZ\xf1\xcdil:\x87\xc5''\xaeu" 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(key)

def fileFind():
    os.chdir(r'E:\Users\Joe Roybal\Documents\Ransomware_Test')
    targets = os.listdir()
    print(targets)
 

password()
fileFind()
