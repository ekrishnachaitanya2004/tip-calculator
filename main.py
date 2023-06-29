#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill =input("What was the total bill?")
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
peple=input("How many people to split the bill?")
if tip == 10:
    a=(int(total_bill)/int(peple))*1.10
elif tip == 12:
    a=(int(total_bill)/int(peple))*1.12
elif tip == 15:
    a=(int(total_bill)/int(peple))*1.15
else:
    a="enter a valid tip percentage"


print("Each person should pay:"+str(a))
