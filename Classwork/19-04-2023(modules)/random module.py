import random

# it will give random values in float
x = random.random()

#  for getting random value in integer
otp = random.randint(9999,99999)

print(x)
print(otp)

# for captcha code this module is used

captcha = ["asde","UsjkK","1EckO9","PauHbG","YnHvvFd","WVvcD"]
cpt = random.choice(captcha)
print(cpt)

# to shuffle the non-empty sequence
random.shuffle(captcha)
print(captcha)