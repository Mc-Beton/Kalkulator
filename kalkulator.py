import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


#Funkcja odejmowania i dzielenia
def calculate(task, a, b):
    #odejmowanie
    if task == "2":
        result = a-b
        logging.info(f"Odejmuję {a} od {b}")
        logging.info(f"Wynik to {result}")

    #dzielenie
    elif task == "4":
        result = a/b
        logging.info(f"Dzielę {a} przez {b}")
        logging.info(f"Wynik to {result}")

#Funkcja dodawania i mnożenia
def calculate2(task, a):
    #dodawanie
    if task == "1":
        result = 0
        for ele in a:
            result = result + ele
        logging.info(f"Suma wszystkich liczb to {result}")
    #mnożenie
    elif task == "3":
        result=1
        for ele in a:
            result = result * ele
        logging.info(f"wynik mnożenia wszystkich liczb to {result}")

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
            calculate2(task, a)
    elif task == "2" or task == "4":
        try:
            while True:
                a = float(input("Podaj pierwszą liczbę "))
                b = float(input("Podaj drugą liczbę "))
                logging.debug(f"Wprowadzono liczby {a}, {b}")
                logging.info(calculate(task, a, b))
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
            calculate2(task, a)


#wywołanie programu
if __name__ == "__main__":
    task = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie ")
    logging.debug(f"Zostało wywołane działanie numer {task}")
    what_task(task)
    
    

    
    

