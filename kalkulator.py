import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def calculate(task, a, b):
    #dodawanie
    if task == 1:
        result = a+b
        return result
    #odejmowanie
    elif task == 2:
        result = a-b
        return result
    #mnożenie
    elif task == 3:
        result = a*b
        return result
    #dzielenie
    elif task == 4:
        result = a/b
        return result

if __name__ == "__main__":
    task = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
    a = input("Podaj pierwszą liczbę")
    b = input("Podaj drugą liczbę")
    calc_result = calculate(task, a, b)
    print(calc_result)
