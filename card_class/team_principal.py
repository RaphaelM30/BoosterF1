class TeamPrincipal:
    def __init__(self, name: str, equipe: str, nationalite: str, role: str, depuis: int, profil: str, rarete: str) -> TeamPrincipal:
        """Class to create a team principal.

        Args:
            name (str): Name of the team principal.
            equipe (str): Team of the team principal.
            nationalite (str): Nationality of the team principal.
            role (str): Role of the team principal.
            depuis (int): Year since the team principal has this role.
            profil (str): Profile of the team principal.
            rarete (str): Rarity of the team principal card.
        """
        self.name = name
        self.equipe = equipe
        self.nationalite = nationalite
        self.role = role
        self.depuis = depuis
        self.profil = profil
        self.rarete = rarete

    def __str__(self):
        return f"{self.name} - {self.equipe} | {self.nationalite} | {self.role} | Depuis {self.depuis} | {self.rarete}"

    def __repr__(self):
        return f"TeamPrincipal({repr(self.name)}, {repr(self.equipe)}, {repr(self.nationalite)}, {repr(self.role)}, {repr(self.depuis)}, {repr(self.profil)}, {repr(self.rarete)})"
