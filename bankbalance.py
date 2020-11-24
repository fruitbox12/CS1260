from math import sqrt

root2 = sqrt(2)

b = int(input("Enter an Amount "))
r = float(input("Enter an rate "))
n = int(input("Enter an amount of years "))


future  = round(b*((1+(0.01*r)) ** n),2)
print("Your balance in", n, "years", "is", future)


