import logging
  
def calculate(act, num_1, num_2):
  if act == '1':
    logging.info("Dodaję %s i %s" %(x,y))
    print("Wynik to: ", x+y)
  elif act == '2':
    logging.info("Odejmuję od %s  %s" %(x,y))
    print("Wynik to: ", x-y)
  elif act == '3':
    logging.info("Mnożę %s i %s" %(x,y))
    print("Wynik to: ", x*y)
  elif act == '4':
    logging.info("Dzielę %s przez %s" %(x,y))
    print("Wynik to: ", x/y)
    
if __name__=="__main__":
  logging.basicConfig(level=logging.INFO, format='%(message)s')
  act = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
  while True:
    try:
      x = float(input("Podaj składnik 1. "))
      y = float(input("Podaj składnik 2. "))
    except ValueError:
      print("Błąd nieprawidłowy składnik. ")
      continue
    break
  calculate(act, x, y)
