salary=float(input("enter gross employee salary "))
days=int(input("enter no of working days  "))
ta=1000
da=1000
tax=10/100*salary
total=(salary+ta+da)-tax
total1=total/31
total2=total1*25
print("the total salary of employee is",total2)

