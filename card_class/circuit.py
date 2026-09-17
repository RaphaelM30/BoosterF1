class Circuit:
    def __init__(self, name: str, grand_prix: str, ville: str, pays: str,types: str, sprint: bool, caracteristique: str) -> Circuit:
        """Class to create a circuit.

        Args:
            name (str): Name of the circuit.
            grand_prix (str): Grand Prix hosted by the circuit.
            ville (str): City where the circuit is located.
            pays (str): Country where the circuit is located.
            type (str): Type of circuit.
            sprint (bool): Whether the circuit hosts a sprint.
            caracteristique (str): Main characteristic of the circuit.
        """
        self.name = name
        self.grand_prix = grand_prix
        self.ville = ville
        self.pays = pays
        self.type = types
        self.sprint = sprint
        self.caracteristique = caracteristique

    def __str__(self):
        return f"{self.name} - {self.grand_prix} | {self.ville} | {self.pays} | {self.type} | Sprint : {self.sprint}"

    def __repr__(self):
        return f"Circuit({repr(self.name)}, {repr(self.grand_prix)}, {repr(self.ville)}, {repr(self.pays)}, {repr(self.type)}, {repr(self.sprint)}, {repr(self.caracteristique)})"
