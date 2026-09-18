import json

class Ecurie:
    def __init__(self,name: str,pays: str,moteur: str,pilotes: list,titres_constructeurs: int,identite: str,rarete:str)-> Ecurie:
        """Class to create a team.

        Args:
            name (str): Name of the team.
            pays (str): Country of the team.
            moteur (str): Engine manufacturer.
            pilotes (list): Drivers of the team.
            titres_constructeurs (int): Number of constructors' championships won.
            identite (str): Identity or nickname of the team.
            rarete (str): Rarity of the team card.
        """
        self.name = name
        self.pays = pays
        self.moteur = moteur
        self.pilotes = pilotes
        self.titres_constructeurs = titres_constructeurs
        self.identite = identite
        self.rarete = rarete

        assert isinstance(pilotes, list) and len(pilotes) > 0
        assert isinstance(titres_constructeurs, int) and titres_constructeurs >= 0

    def __str__(self):
        return f"{self.name} - {self.pays} | {self.moteur} | {self.pilotes} | {self.titres_constructeurs} titres | {self.rarete}"

    def __repr__(self):
        return f"Ecurie({repr(self.name)}, {repr(self.pays)}, {repr(self.moteur)}, {repr(self.pilotes)},{repr(self.titres_constructeurs)}, {repr(self.identite)}, {repr(self.rarete)})"

    @staticmethod
    def create_instances():
        """Create all Ecurie instances from the JSON file.

        Returns:
            list[Ecurie]: List of all teams.
        """
        with open("card_data/ecuries.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        ecuries_list = []

        for ecurie in data:
            ecuries_list.append(
                Ecurie(
                    ecurie["name"],
                    ecurie["pays"],
                    ecurie["moteur"],
                    ecurie["pilotes"],
                    ecurie["titres_constructeurs"],
                    ecurie["identite"],
                    ecurie["rarete"]
                )
            )

        return ecuries_list
