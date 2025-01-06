import hashlib #library to hash
import maskpass as mp #library to hide the password
def hash_password(password): #function to hash the password
    return hashlib.sha512(password.encode()).hexdigest()

password = 'your_hashed_password' #use the hash_password function to hash and print the password, then enter the hashed result

input_password = mp.advpass("amogus! password: ") #input password, but hidden with asterisks
if hash_password(input_password) == password: #check the hashed version of inputed password and compare to right password
    print("amogus! password is correct!")
else:
    print("amogus! password is incorrect! you're dol...phin!")
