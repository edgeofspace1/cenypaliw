import random
import time
from sklep import Sklep, Cennik, WygranaGra, PrzegranaGra


global coins
coins = 0
global dostawy
dostawy=0
global owoce
owoce=5
global warzywa
warzywa=10
global słodycze
słodycze=1
global inPRZ
inPRZ=0

sklep = Sklep()
cennik = Cennik()
wygranagra = WygranaGra()
przegranagra = PrzegranaGra()



def menu():
  print(f"\nMonety: {coins}")
  print(f"Dostawy: {dostawy}")
  print(f"Owoce: {owoce}")
  print(f"Warzywa: {warzywa}")
  print(f"Słodycze: {słodycze}")
  print(f"Inne przedmioty: {inPRZ}")


def sprz():
  global coins, owoce, warzywa, słodycze, inPRZ, dostawy
  while True:
    odp = input("Co chcesz sprzedać? Warzywa - W, Owoce - O, Słodycze - S, Inne przedmioty - I, przejsc dalej - C:   ")

    if odp == "W" and warzywa >= 1:
      coins = coins + 15
      warzywa = warzywa - 1
      print("Sprzedałeś warzywo!")
    
    if odp == "O" and owoce >= 1:
        coins = coins + 10
        owoce = owoce - 1
        print("Sprzedałeś owoc")

    if odp == "S" and słodycze >= 1:
        coins = coins + 20
        słodycze = słodycze - 1
        print("Sprzedałeś słodycz")

    if odp == "I" and inPRZ >= 1:
        coins = coins + 5
        inPRZ = inPRZ - 1
        print("Sprzedałeś inny przedmiot")

    if odp == "C":
      break



def dost():
  global coins, owoce, warzywa, słodycze, inPRZ, dostawy
  odp = input("\nCzy chcesz zamówić dostawę? ")
  if odp == "Tak" and coins >= 50:
    l = random.randint(1,10)
    dostawy += 1
    coins -= 50
    owoce += l
    warzywa = warzywa + l
    słodycze += l
    inPRZ += l
    print("dostawa zamówiona")
  else:
    print(f"\nMasz za mało monet, twoja liczba monet to {coins}.")

def cz():
  global coins, owoce, warzywa, słodycze, inPRZ
  i = 0
  while i < 2:
    odp = input("\nCo chcesz teraz zrobić? Sprzedać/Zamówić dostawę/Sprawdzić ekwipunek/Sprawdzić swój cennik/Nic  ")
    if odp == "Sprzedać":
      sprz()
      i += 1
    if odp == "Zamówić dostawę":
      dost()
      i += 1
    if odp == "Sprawdzić ekwipunek":
      menu()
      i += 1
    if odp == "Sprawdzić swój cennik":
      cennik.cenk()
      i += 1
    if odp == "Nic":
      break

def pkn():
  global coins, owoce, warzywa, słodycze, inPRZ
  print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
  odp = input("\nPrzyszedł do ciebie chłopiec z okolicy, chcesz z nim pograć? ")
  if odp == "Tak" or odp == "tak" or odp == "TAK":
    print("\nGracie w papier, kamień, nożyce.")
    #PAPIER-1, KAMIEŃ-2, NOŻYCE-3
    p = 0
    ptkU = 0
    ptkC = 0
    while p < 3:
      wyC = random.randint(1,3)
      wyb = input("\nCo wybierasz? ")
      print("3")
      time.sleep(1)
      print("2")
      time.sleep(1)
      print("1")
      time.sleep(1)
      if wyb == "papier"  and wyC == 1:
        print("-REMIS-")
        p += 1
        print(f"{ptkU} : {ptkC}")
      if wyb == "papier"  and wyC == 2:
        ptkU += 1
        print("-PUNKT DLA CIEBIE-")
        p += 1
        print(f"{ptkU} : {ptkC}")
      if wyb == "papier" and wyC == 3:
        ptkC += 1
        print("-PUNKT DLA CHŁOPCZYKA-")
        p += 1
        print(f"{ptkU} : {ptkC}")

      
      if wyb == "kamień" and wyC == 1:
        print("-PUNKT DLA CHŁOPCZYKA-")
        ptkC += 1
        print(f"{ptkU} : {ptkC}")
        p += 1
      if wyb == "kamień" and wyC == 2:
        print("-REMIS-")
        print(f"{ptkU} : {ptkC}")
        p += 1
      if wyb == "kamień" and wyC == 3:
        print("-PUNKT DLA CIEBIE-")
        ptkU += 1
        print(f"{ptkU} : {ptkC}")
        p += 1

      if wyb == "nożyce" and wyC == 1:
        print("-PUNKT DLA CIEBIE-")
        ptkU += 1
        p += 1
        print(f"{ptkU} : {ptkC}")
      if wyb == "nożyce" and wyC == 2:
        print("-PUNKT DLA CHŁOPCZYKA-")
        ptkC += 1
        p += 1
        print(f"{ptkU} : {ptkC}")
      if wyb == "nożyce" and wyC == 3:
        print("-REMIS-")
        p += 1
        print(f"{ptkU} : {ptkC}")

      if p == 3 and ptkU > ptkC:
        coins = coins + 10

      if p == 3 and ptkC > ptkU:
        coins = coins - 20

  print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")

def zl():
  global coins, owoce, warzywa, słodycze, inPRZ
  print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
  odp = input("\nPrzyszedł do ciebie chłopiec z okolicy, chcesz z nim pograć? ")
  if odp == "Tak" or odp == "tak" or odp == "TAK":
    print("\nOdgadnij liczbę między 1, a 10.")
    k = random.randint(1,10)
    odp = input("Twoja sugestia: ")
    s = int(odp)
    if s == k:
      print("-WYGRAŁEŚ-")
      coins = coins + 100

    else:
      print(f"Niestety nie udało ci się zgadnąć, odpowiedź to {k}")
  print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")

sklep.dis()
print("\n-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
sprz()
cz()
pkn()
cz()
zl()
cz()
pkn()
cz()
zl()

if coins >= 900:
  print(f"Osiągnąłeś tygodniowy cel, wygrywasz grę! twoje pieniądze {coins}")

  wygranagra.wygrana()


else:
  print(f"Nie udało ci się zdobyć oczekiwanej ilości pieniędzy, przegrywasz grę! twoje pieniądze {coins}")

  przegranagra.przegrana()