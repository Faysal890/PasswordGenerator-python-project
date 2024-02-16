import random 
import string

chars = string.ascii_letters+string.digits+string.punctuation
size = 12
password = "".join([random.choice(chars) for i in range(size)])
print("Your random passowrd is :",password)