import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
x = float(input("Podaj składnik 1. "))
y = float(input("Podaj składnik 2. "))
act = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if act == '1':
    logging.info("Dodaję %s i %s" %(x,y))
    print(x+y)
elif act == '2':
    logging.info(" Odejmuję od %s  %s" %(x,y))
    print(x-y)
elif act == '3':
    logging.info(" Mnożę %s i %s" %(x,y))
    print(x*y)
elif act == '4':
    logging.info(" Dzielę %s przez %s" %(x,y))
    print(x/y)