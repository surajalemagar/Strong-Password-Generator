import string
import random
def myfun(n):
    return "".join(random.choice(characters) for x in range(n))
n=int(input("How Many Character in Your Password:"))
characters = string.ascii_letters + string.punctuation  + string.digits
password=myfun(n)
print("Password is:",password)