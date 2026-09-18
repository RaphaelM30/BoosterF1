import time
from booster import Booster
from card_class.circuit import Circuit
from card_class.team_principal import TeamPrincipal
from card_class.pilote import Pilote
from card_class.ecurie import Ecurie

class Menu:
    def __init__(self):
        print(" Welcome in the F1 Booster opening ".center(45, "="))

        self.pilotes = Pilote.create_instances()
        self.team_principals = TeamPrincipal.create_instances()
        self.ecuries = Ecurie.create_instances()
        self.circuits = Circuit.create_instances()
        self.run()

    def run(self):
        while True:
            print("\n1. Open a booster")
            print("2. Exit")

            try:
                choice = int(input("Choice a number . . . "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            match choice:
                case 1:
                    print("Opening booster...")
                    time.sleep(1)
                    booster = Booster(5,self.pilotes,self.team_principals,self.ecuries,self.circuits)
                    print(booster)

                case 2:
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid choice.")


menu = Menu()
