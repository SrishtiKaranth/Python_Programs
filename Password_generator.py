import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator!")
nl=int(input("How many letters would you like?"))
nn=int(input("How many numbers would you like?"))
ns=int(input("How many symbols would you like?"))
#letcombo=""
#numcombo=""
#symcombo=""
#password=""
password=[]
for i in range(nl):
  password.append(random.choice(letters))
  #password+=random.choice(letters)
  #let=random.choice(letters)
  #letcombo=letcombo+let
for j in range(nn):
  password.append(random.choice(numbers))
  #password+=random.choice(numbers)
  #num=random.choice(numbers)
  #numcombo=numcombo+num
for k in range(ns):
  password.append(random.choice(symbols))
  #password+=random.choice(symbols)
  #sym=random.choice(symbols)
  #symcombo=symcombo+sym
#passcode=letcombo+numcombo+symcombo
random.shuffle(password)
print("Your password is :" + "".join(password))
