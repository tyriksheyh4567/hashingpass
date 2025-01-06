import hashlib
import maskpass as mp
def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()

password = '974a36183a171f87abefe10d6a84d855edc10962cc18884f325e167ab334a33b3e8ff50ebc7fe7ec4c988ed9488264098a882d5aeada5daab01ac815980faa79'

input_password = mp.advpass("amogus! password: ")
if hash_password(input_password) == password:
    print("amogus! password is correct!")
else:
    print("amogus! password is incorrect! you're dol...phin!")