
""" 
#Övning 1
def FizzBuzz():
    for i in range(1, 101):
        if(i % 3 == 0 & i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
       
FizzBuzz()

"""
#Övning 2

def skottår():
    
    year = int(input("Mata in ett år: "))

    if(year % 400 == 0):
        print("Året är ett skottår")
    elif(year % 4 == 0 and year % 100 != 0):
        print("Året är ett skottår")
    else:
        print("Året är inte ett skottår")

skottår()