from components.card import Card


class Hand:
    def __init__(self, screen):
        self.__cards = []
        self.__pos = (screen.get_width() // 2, screen.get_height() // 1.2)
        self.__rel_positions = []

    @property
    def cards(self):
        return self.__cards

    @property
    def hand_size(self):
        return len(self.__cards)

    def add_card(self, card: Card):
        self.__cards.append(card)
        self.__rel_positions.append(self.hand_size/2)
        self.__rel_positions = [p - 0.5 for p in self.__rel_positions]
        self.adjust_card_pos()

    def remove_card(self, card: Card):
        for i, c in enumerate(self.__cards):
            if c == card:
                self.__cards.pop(i)
        self.__rel_positions.pop()
        self.__rel_positions = [p + 0.5 for p in self.__rel_positions]
        self.adjust_card_pos()

    def adjust_card_pos(self):
        for i, c in enumerate(self.__cards):
            c.update_position((self.__pos[0] + self.__rel_positions[i] *
                                  c.rect.width, #//2
                             self.__pos[1]))