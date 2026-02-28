p = int(input("Enter principle "))
r = int(input('Enter rate of interest '))
t = int (input("Enter time period "))

#simple interest is
si = (p*r*t)/100
print(f"Simple interest is {si}")

#compund interest 
amount = p*(1+r/100)*t
ci = amount - p
print(f"the compund interest is {ci}")