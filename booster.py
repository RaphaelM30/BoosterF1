import json, random


class Booster:
    """Class to create a booster containing cards from JSON files."""

    def __init__(self, card_number=5, *files):
        """Create a booster from one or several JSON files.

        Args:
            card_number (int): Number of cards in the booster.
            *files (str): Paths to the JSON files containing the cards.
        """
        self.cards = []
        self.booster_card = []

        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.cards.extend(data)

        self.choice_random_card(card_number)

    def choice_random_card(self, number):
        """Choose random cards from the available cards."""
        self.booster_card = random.sample(self.cards, number)

    def __str__(self):
        """Return a better display of the cards."""
        result = ""

        for card in self.booster_card:
            result += "--------------------\n"

            for key, value in card.items():
                result += f"{key} : {value}\n"

        result += "--------------------"

        return result


booster = Booster(5, "card_data/circuit.json","card_data/ecuries.json","card_data/team_principal.json","card_data/pilotes.json")
print(booster)
