import random 
import string

chars = string.ascii_letters+string.digits+string.punctuation
# password = ""
size = 12
# for i in range(size):
#     password += random.choice(chars)
password = "".join([random.choice(chars) for i in range(size)])
print("Your random passowrd is :",password)