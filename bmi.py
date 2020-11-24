print(r"""\

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   ಠ ಠ. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)
var =str(input("metric or english? type m for metric or e for english "))
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def metric():
    kg = float(input("enter your weight in kg "))
    m = float(input("enter your height in meters "))
    bmi=kg/(m**2)
    print("your bmi is", round(bmi,2))
def eng():
    lbs = float(input("enter your weight in lbs "))
    inch = float(input("enter your height in inches "))
    bmi=(lbs*703)/(inch**2)
    print("your bmi is", round(bmi,2))
if var == "m":
    metric()

elif var == "e":
    eng()
else:
    print("enter m or e")
bmi = float(input('\033[1m' + "Please Enter the bmi displayed to tell you your level of health "))
def message(bmi):
    if bmi < 18.999:
        print ('\x1b[6;30;42m' + "Since your BMI is ", bmi, ".", " That is considered underweight.", sep='')
    elif 19 <= bmi <= 24.999: 
        print('\033[92m' + "Since your BMI is ", bmi, ".", " That is normal healthy weight.", sep='')
    elif 25 <= bmi <= 29.999: 
        print('\033[36m' + "Since your BMI is ", bmi, ".", " That is considered overweight.", sep='')
    elif 30 <= bmi <= 39.999: 
        print('\033[91m' + "Since your BMI is ", bmi, ".", " That is considered obese.", sep='')
    elif bmi >= 40: 
        print('\033[91m' + "Since your BMI is ", bmi, ".", " That is considered morbidly obese.", sep='')
message(bmi)
