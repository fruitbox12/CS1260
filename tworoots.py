from math import sqrt

a = int(input("Enter int for a: "))
b = int(input("Enter int for b: "))
c = int(input("Enter int for c: "))


addSQRT = (-b + sqrt(b**2 - 4*a*c))/(2*a)

minusSQRT = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(addSQRT)
print(minusSQRT)
