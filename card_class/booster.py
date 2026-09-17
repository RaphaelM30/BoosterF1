import json

class Booster:
    def __init__(self, *files):
        self.cards = []

        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.cards.extend(data)
