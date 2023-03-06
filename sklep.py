import random

class Sklep:

    nazwa = None

    def __init__(self):
        self.nazwa = input("Wybierz nazwę dla swojego stoiska")

    def dis(self):
        print("      __________________________    ")
        print("     |                            | ")
        print(f"         STOISKO {self.nazwa} ")
        print("     |____________________________| ")
        print("     |                            | ")
        print("     |           ___              | ")
        print("     |          / _ _ \           | ")
        print("     |          \_____/           | ")
        print("     |__________/_____\___________| ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |  ______________________    | ")
        print("     |__|                     |__|  ")

class Cennik:
    def cenk(self):
        print(" ___________________________ ")
        print("|           CENNIK            | ")
        print("| DOSTAWA – 50 monet          | ")
        print("| 1x owoc – 10 monet          | ")
        print("| 1x warzywo – 15 monet       | ")
        print("| 1x słodycze – 20 monet      | ")
        print("| 1x inny przedmiot – 5 monet | ")
        print("|_____________________________|")

class PrzegranaGra:
    def przegrana(self):
        print("      __________________________    ")
        print("     |                            | ")
        print(f"         STOISKO ZAMKNIĘTE"         )
        print("     |____________________________| ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |____________________________| ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |    B A N K R U C T W O     | ")
        print("     |                            | ")
        print("     |  ______________________    | ")
        print("     |__|                     |__|  ")

class WygranaGra:
    def wygrana(self):
        print("      __________________________    ")
        print("     |                            | ")
        print(f"         STOISKO  - POPULARNE    | ")
        print("     |____________________________| ")
        print("     |                            | ")
        print("     |           ___              | ")
        print("     |          / V_V \           | ")
        print("     |          \_____/           | ")
        print("     |__________/_____\___________| ")
        print("     |                            | ")
        print("     |                            | ")
        print("     |       PEŁNE OBROTY         | ")
        print("     |           STONKS     | ")
        print("     |  ______________________    | ")
        print("     |__|                     |___|  ")

