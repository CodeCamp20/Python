import random
import string

def randomPswd(pswdlen = 10):

       letters = string.ascii_letters

       return ''.join(random.choice(letters) for i in range(pswdlen))

print("Random Password : \n",randomPswd( ))
