import random
import logging
while True:
    logging.basicConfig(filename="ex.log", level=logging.INFO)
    logging.info("Programm started")
    try:
        n = int(input())
        logging.info(f"Users nuber is {n}")
    except ValueError:
        print("Вы ввели некорректные данные")
        logging.error("ValueError.")
        continue
    if n <= 0:
        print("Вы ввели некорректные данные")
        logging.error("ValueError.")
        continue
    numbers = []
    print("Первое выпавшее число: ", end="")
    while len(numbers) != n:
        number = random.randint(1,n)
        if number not in numbers:
            numbers.append(number)
            print(number)
            logging.info(f"Program printed {number}")
            input('Для получения следующего числа на бочонке нажмите "ENTER"')
    print("Все выпавшие номера: ", numbers)
    logging.info(f"All nubers is: {numbers}")
    logging.info("Programms end")