import json

class Pilote:
    def __init__(self, name: str, equipe: str, numero: int, victoires: int, poles:int, rarete:str) -> Pilote:
        """Class to create a pilote.

        Args:
            name (str): Name of the pilote.
            equipe (str): Team of the pilote.
            numero (int): Race number of the pilote.
            victoires (int): Number of victories of the pilote.
            poles (int): Number of pole positions of the pilote.
            rarete (str): Rarity of the pilote card.
        """
        self.name = name
        self.equipe = equipe
        self.numero = numero
        self.victoires = victoires
        self.poles = poles
        self.rarete = rarete

        assert isinstance(numero, int) > 0
        assert isinstance(victoires, int) >= 0
        assert isinstance(poles, int) >= 0

    def __str__(self):
        return f"{str(self.name)} - {str(self.equipe)} | #{str(self.numero)} | {str(self.victoires)} victoires | {str(self.poles)} poles | {str(self.rarete)}"

    def __repr__(self):
        return f"Pilote({repr(self.name)}, {repr(self.equipe)}, {repr(self.numero)}, {repr(self.victoires)}, {repr(self.poles)}, {repr(self.rarete)})"

    @staticmethod
    def create_instances():
        """Create all Pilote instances from the JSON file.

        Returns:
            list[Pilote]: List of all pilotes.
        """
        with open("card_data/pilotes.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        pilotes_list = []

        for pilote in data:
            pilotes_list.append(
                Pilote(
                    pilote["name"],
                    pilote["equipe"],
                    pilote["numero"],
                    pilote["victoires"],
                    pilote["poles"],
                    pilote["rarete"]
                )
            )

        return pilotes_list
