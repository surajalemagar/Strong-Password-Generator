import string
import random

def passordw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

n=int(input('How many characters in your password?'))
password=password_gen(n)
print(password)