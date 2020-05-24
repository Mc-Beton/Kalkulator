import logging
import math
import numpy
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

#Input numbers to program
def input_num(func):
    def wrap():
        try:
            while True:
                a = list(map(int, input("Enter the numbers each after space and then press enter ").split()))
                func(*a)
                break
        except ValueError:
            print("It is not a number")
    return wrap

#Substraction
@input_num
def substr(*args):
    result = args[0] - sum(args[1:])
    print(f"The result is {result}")

#Divide
@input_num
def div(*args):
    result = args[0]/(numpy.prod(args[1:]))
    print(f"The result is {result}")

#Addition
@input_num
def addit(*args):
    result = sum(args)
    print(f"The result of suming all the numbers is {result}")

#Multiply
@input_num
def multi(*args):
    result = numpy.prod(args)
    print(f"The reuslt of multiplying all numbers is {result}")
    
#Choose task
def what_task():
    while True:
        task = input("Type in the number of task you would like to execute: 1 Addition, 2 Substraction, 3 Multiply, 4 Divide or exit to quit ")
        logging.debug(f"The chosen task is {task}")
        if task == "1":
            addit()
        if task == "2":
            substr()
        if task == "3":
            multi()
        if task == "4":
            div() 
        if task == "exit":
            print("Bye")
            break
        
#wywołanie programu
if __name__ == "__main__":
    what_task()


    

    
    

