import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def calculate(task, a, b):
    #result=""
    #result = result + "Wynik działania nr %d.\n" % task
    #dodawanie
    if task == "1":
        suma = a+b
        print(f"Dodaję {a} i {b}")
        return f"Wynik to {suma}"
    #odejmowanie
    elif task == "2":
        result = a-b
        print(f"Odejmuję {a} od {b}")
        return f"Wynik to {result}"
    #mnożenie
    elif task == "3":
        result = a*b
        print(f"Mnożę {a} i {b}")
        return f"Wynik to {result}"
    #dzielenie
    elif task == "4":
        result = a/b
        print(f"Dzielę {a} przez {b}")
        return f"Wynik to {result}"

if __name__ == "__main__":
    task = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie ")
    a = input("Podaj pierwszą liczbę ")
    b = input("Podaj drugą liczbę ")
    a=int(a)
    b=int(b)
    print(calculate(task, a, b))
    
    

    
    

