import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


#Substraction
def substr(a, b):
    result = a-b
    logging.info(f"Substracting {a} from {b}")
    print(f"The result is {result}")

#Divide
def div(a, b):
    result = a/b
    logging.info(f"Divinding {a} by {b}")
    print(f"The result is {result}")

#Addition
def addit(a):
    result = 0
    for ele in a:
        result = result + ele
    print(f"The result of suming all the numbers is {result}")

#Multiply
def multi(a):
    result=1
    for ele in a:
        result = result * ele
    print(f"The reuslt of multiplying all numbers is {result}")

#Choose task
def what_task(task):
    if task == "1":
        a = input("Podaj liczby, które chcesz do siebie dodać rozdzielając każdą spacją. Następnie zatwierdz enterem: ")
        suma = [float(arg) for arg in a.split() if arg.isdigit()]
        addit(suma)
    elif task == "2":
        try:
            while True:
                a = float(input("What is your first number? "))
                b = float(input("What is your second number? "))
                logging.debug(f"Given numbers are {a}, {b}")
                substr(a, b)
        except ValueError:
            print("It is not a number")
    elif task == "3":
        a = input("Podaj liczby, które chcesz ze sobą pomnożyć rozdzielając każdą spacją. Następnie zatwierdz enterem: ")
        mult = [float(arg) for arg in a.split() if arg.isdigit()]
        multi(mult)
    elif task == "4":
        try:
            while True:
                a = float(input("What is your first number? "))
                b = float(input("What is your second number? "))
                logging.debug(f"Given numbers are {a}, {b}")
                div(a, b)
        except ValueError:
            print("It is not a number")

#wywołanie programu
if __name__ == "__main__":
    task = input("Type in the number of task you would like to execute: 1 Addition, 2 Substraction, 3 Multiply, 4 Divide ")
    logging.debug(f"The chosen task is {task}")
    what_task(task)

    

    
    

