from cryptography.fernet import Fernet

#This is used for key checking

file = open('key.key','rb')
key = file.read()
file.close()
print(key)



#Used for key generation

#key = Fernet.generate_key()
#print(key)

#file = open('key.key','wb')
#file.write(key)
#file.close