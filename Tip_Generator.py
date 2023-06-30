bill=input("What is your total bill? ")
tip=input("How much tip woukd you like to give : 10,12,15? ")
people=input("How many people are there?")
sp1=float(bill)/int(people)
sp2=(float(bill)/int(people))*(float(tip)/100)
split=sp1+sp2
split_f=round(split,2)
print(f"Each person has to pay rupees {split_f} ")
