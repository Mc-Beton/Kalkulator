import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def calculate(task, numbers):
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
