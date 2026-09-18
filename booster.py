import random


class Booster:
    """Class to create a booster containing cards."""

    def __init__(self, card_number: int, *cards_lists):
        """Create a booster.

        Args:
            card_number (int): Number of cards in the booster.
            *cards_lists (list): Lists containing the card instances.
        """
        assert card_number > 0
        assert len(cards_lists) > 0

        self.cards = []

        for cards_list in cards_lists:
            self.cards.extend(cards_list)

        self.choice_random_card(card_number)

    def choice_random_card(self, number: int):
        """Choose random cards from the available cards."""
        assert isinstance(number, int)
        assert number > 0
        assert number <= len(self.cards)

        self.booster_card = random.sample(self.cards, number)

    def __str__(self):
        """Return a better display of the cards."""
        result = ""

        for card in self.booster_card:
            result += "--------------------\n"
            result += str(card) + "\n"

        result += "--------------------"

        return result
