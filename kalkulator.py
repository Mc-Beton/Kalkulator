import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


#Funkcja odejmowania
def odejmij(a, b):
    result = a-b
    logging.info(f"Odejmuję {a} od {b}")
    print(f"Wynik to {result}")

#Funkcja dzielenia
def dzielenie(a, b):
    result = a/b
    logging.info(f"Dzielę {a} przez {b}")
    print(f"Wynik to {result}")

#Funkcja dodawania
def dodawanie(a):
    result = 0
    for ele in a:
        result = result + ele
    print(f"Suma wszystkich liczb to {result}")

#Funkcja mnożenia
def mozenie(a):
    result=1
    for ele in a:
        result = result * ele
    print(f"wynik mnożenia wszystkich liczb to {result}")

#funkcja wyboru działania
def what_task(task):
    if task == "1":
        logging.info("Podaj liczby jakie chcesz dodać kolejno je zatwierdzając i zakończ wpisaniem stop")
        try: 
            a = [] 
            while True: 
                a.append(float(input())) 
        except:
            logging.debug(f"Wprowadzono następujące liczby {a}")
            dodawanie(a)
    elif task == "2":
        try:
            while True:
                a = float(input("Podaj pierwszą liczbę "))
                b = float(input("Podaj drugą liczbę "))
                logging.debug(f"Wprowadzono liczby {a}, {b}")
                odejmij(a, b)
        except:
            print("To nie jest liczba!")
    elif task == "3":
        print("Podaj liczby jakie chcesz pomnożyć ze sobą kolejno je zatwierdzając i zakończ wpisaniem stop")
        try: 
            a = [] 
            while True: 
                a.append(float(input())) 
        except: 
            logging.debug(f"Wprowadzono następujące liczby {a}")
            mnozenie(a)
    elif task == "4":
        try:
            while True:
                a = float(input("Podaj pierwszą liczbę "))
                b = float(input("Podaj drugą liczbę "))
                logging.debug(f"Wprowadzono liczby {a}, {b}")
                dzielenie(a, b)
        except:
            print("To nie jest liczba!")

#wywołanie programu
if __name__ == "__main__":
    task = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie ")
    logging.debug(f"Zostało wywołane działanie numer {task}")
    what_task(task)

    

    
    

