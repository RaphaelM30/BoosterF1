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
        result = "\n========== F1 BOOSTER ==========\n"

        for i, card in enumerate(self.booster_card, 1):
            result += f"{i}. {card}\n"

        result += "================================"

        return result
