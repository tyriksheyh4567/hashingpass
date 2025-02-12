#Orignal author: yaros/tyriksheyh4567/Yaromir Sheydaev. No need for credit if you fork it (even if your code will be closed source).
#This is public domain, everything about things you can do with the code is in the LICENSE file.
#Ver 1.1. Made in 04.02.2025. Updated the comments.
import hashlib #library to hash
import maskpass as mp #library to hide the password
def hash_password(password): #function to hash the password
    return hashlib.sha512(password.encode()).hexdigest()
#WARNING! You should change the value of "password" variable to hashed one (instruction below)
password = 'your_hashed_password' 
#^
#| use the hash_password function to hash and print the password, then enter the hashed result as a value of "password" variable.


input_password = mp.advpass("amogus! password: ") #input password, but hidden with asterisks
if hash_password(input_password) == password: #check the hashed version of inputed password and compare to right password
    print("amogus! password is correct!")
else:
    print("amogus! password is incorrect! you're dol...phin!")
