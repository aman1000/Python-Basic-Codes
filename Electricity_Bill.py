print("**Electricity Bill**")
a=float(input("Enter Meter Reading:"))
if (a<=100):
 amnt=a*5.95
else:
 amnt1= 100*5.95
 amnt2=(a-100)*6.95
 amnt=amnt1+amnt2
print("Total Bill Amount:",amnt)


