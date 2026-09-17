class Pilote:
    def __init__(self, name: str, equipe: str, numero: str, victoires: str, poles:str, rarete:str) -> Pilote:
        """Class to create a pilote.

        Args:
            name (str): Name of the pilote.
            equipe (str): Team of the pilote.
            numero (str): Race number of the pilote.
            victoires (str): Number of victories of the pilote.
            poles (str): Number of pole positions of the pilote.
            rarete (str): Rarity of the pilote card.
        """
        self.name = name
        self.equipe = equipe
        self.numero = numero
        self.victoires = victoires
        self.poles = poles
        self.rarete = rarete

    def __str__(self):
        return f"{str(self.name)} - {str(self.equipe)} | #{str(self.numero)} | {str(self.victoires)} victoires | {str(self.poles)} poles | {str(self.rarete)}"

    def __repr__(self):
        return f"Pilote({repr(self.name)}, {repr(self.equipe)}, {repr(self.numero)}, {repr(self.victoires)}, {repr(self.poles)}, {repr(self.rarete)})"
