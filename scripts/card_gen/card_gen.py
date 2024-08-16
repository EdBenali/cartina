from PIL import Image, ImageDraw, ImageFont

from constants import TRANSPARENT, WHITE
from enums import Rank, Suit, Suits, Ranks, RankGroup

CARD_WIDTH, CARD_HEIGHT = 256, 384
SYMBOL_SIZE = CARD_WIDTH // 2
CARD_CENTRE = (CARD_WIDTH // 2, CARD_HEIGHT // 2)

FONT_SIZE = 48  # Adjust for symbol size

SYMBOL_POSITIONS = {
    2: [
        (CARD_CENTRE[0], CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0], CARD_CENTRE[1] - SYMBOL_SIZE // 2)
    ],
    3: [
        (CARD_CENTRE[0], CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0], CARD_CENTRE[1]),
        (CARD_CENTRE[0], CARD_CENTRE[1] - SYMBOL_SIZE // 2)
    ],
    4: [
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2)
    ],
    5: [
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0], CARD_CENTRE[1]),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2)
    ],
    6: [
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1]),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1]),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2)
    ],
    7: [
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1]),
        (CARD_CENTRE[0], CARD_CENTRE[1] - SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1]),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2)
    ],
    8: [
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1]),
        (CARD_CENTRE[0], CARD_CENTRE[1] - SYMBOL_SIZE // 4),
        (CARD_CENTRE[0], CARD_CENTRE[1] + SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1]),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 2)
    ],
    9: [
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - (SYMBOL_SIZE //
         4) * 3),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + (SYMBOL_SIZE //
         4) * 3),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 4),
        (CARD_CENTRE[0], CARD_CENTRE[1]),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - (SYMBOL_SIZE //
         4) * 3),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + (SYMBOL_SIZE //
         4) * 3)
    ],
    10: [
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - (SYMBOL_SIZE //
         4) * 3),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + (SYMBOL_SIZE //
         4) * 3),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] + SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 4),
        (CARD_CENTRE[0], CARD_CENTRE[1] + SYMBOL_SIZE // 2),
        (CARD_CENTRE[0], CARD_CENTRE[1] - SYMBOL_SIZE // 2),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + SYMBOL_SIZE // 4),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] - (SYMBOL_SIZE //
         4) * 3),
        (CARD_CENTRE[0] - SYMBOL_SIZE // 2, CARD_CENTRE[1] + (SYMBOL_SIZE //
         4) * 3)
    ]
}


def generate_card_image(suit: Suit, rank: Rank):
    background_color = TRANSPARENT  # White background

    # Create a blank image
    img = Image.new('RGBA', (CARD_WIDTH, CARD_HEIGHT), color=background_color)
    draw = ImageDraw.Draw(img)

    # Draw background
    ellipse_margin = CARD_WIDTH // 5
    ellipse = [(-ellipse_margin, -ellipse_margin),
               (CARD_WIDTH + ellipse_margin, CARD_HEIGHT + ellipse_margin)]
    draw.ellipse(xy=ellipse, fill=WHITE)

    _draw_rank(rank=rank,
               draw=draw,
               colour=suit.colour)

    _draw_suit(suit=suit,
               draw=draw,
               rank=rank)

    # Resize to give a pixelated effect
    img = img.resize(
        (CARD_WIDTH // 2, CARD_HEIGHT // 2),
        Image.NEAREST
    ).resize((CARD_WIDTH, CARD_HEIGHT), Image.NEAREST)

    # Save the image
    img.save(f"card_images/{rank.symbol}_of_{suit.value}.png")

    # Show the image (optional)
    img.show()


def _draw_rank(rank: Rank, draw: ImageDraw, colour: tuple):
    # Font settings
    font = ImageFont.load_default(FONT_SIZE)

    # Drawing rank in the corners
    draw.text(
        xy=(CARD_CENTRE[0] - (SYMBOL_SIZE // 4) * 3,
            CARD_CENTRE[1] - (SYMBOL_SIZE // 4) * 5.5),
        text=rank.symbol,
        font=font,
        fill=colour)

    # Not using loop as I want to flip this upside down in future
    # alignment for if 10
    minor_align = 2 if rank.symbol != '10' else 1
    draw.text(
        xy=(CARD_CENTRE[0] + (SYMBOL_SIZE // 4) * minor_align,
            CARD_CENTRE[1] + (SYMBOL_SIZE // 4) * 4),
        text=rank.symbol,
        font=font,
        fill=colour)


def _draw_suit(suit: Suit, draw: ImageDraw, rank: Rank):
    # Draw the suit symbol
    draw_suit_func = DRAW_SUIT_FUNCS[suit.value]

    # Aces and Faces
    # TODO handle face gen
    if rank.group == RankGroup.Face:
        draw_suit_func(
            symbol_pos=CARD_CENTRE,
            symbol_size=SYMBOL_SIZE,
            colour=suit.colour,
            draw=draw)
    # Numbers
    elif rank.group == RankGroup.Number:
        rank_num = int(rank.symbol)
        symbol_positions = SYMBOL_POSITIONS[rank_num]

        for i in range(rank_num):
            draw_suit_func(
                symbol_pos=symbol_positions[i],
                symbol_size=SYMBOL_SIZE // 3,
                colour=suit.colour,
                draw=draw)



def _draw_spades(symbol_pos: tuple,
                 symbol_size: int,
                 colour: tuple,
                 draw: ImageDraw):

    triangle = [
        (symbol_pos[0], symbol_pos[1] - symbol_size // 2),  # Top
        (symbol_pos[0] - symbol_size // 2,
         symbol_pos[1] + symbol_size // 2),
        # Bottom left
        (symbol_pos[0] - symbol_size // 2,
         symbol_pos[1] + symbol_size // 2),
        (symbol_pos[0] + symbol_size // 2,
         symbol_pos[1] + symbol_size // 2)
        # Bottom right
    ]
    draw.polygon(xy=triangle, fill=colour)

    # Draw left slice
    l_slice = [
        (symbol_pos[0] - symbol_size // 2,
         symbol_pos[1] + symbol_size // 4),
        (symbol_pos[0],
         symbol_pos[1] + symbol_size // 4 + symbol_size // 2)]
    draw.pieslice(
        xy=l_slice,
        start=0,
        end=180,
        fill=colour)

    # Draw right slice
    r_slice = [(symbol_pos[0], symbol_pos[1] + symbol_size // 4),
               (symbol_pos[0] + symbol_size // 2,
                symbol_pos[1] + symbol_size // 4 + symbol_size // 2)]
    draw.pieslice(
        xy=r_slice,
        start=0,
        end=180,
        fill=colour)

    # Draw the spade tail
    draw.rectangle(
        xy=[symbol_pos[0] - symbol_size // 10, symbol_pos[1] + symbol_size // 2
            - symbol_size // 10,
         symbol_pos[0] + symbol_size // 10, symbol_pos[1] + symbol_size // 2 +
            (symbol_size // 10) * 4],
        fill=colour
    )

def _draw_diamonds():
    pass

def _draw_hearts():
    pass

def _draw_clubs():
    pass



DRAW_SUIT_FUNCS = {
    Suits.Spades.value.value: _draw_spades,
    Suits.Diamonds.value.value: _draw_diamonds,
    Suits.Hearts.value.value: _draw_hearts,
    Suits.Clubs.value.value: _draw_clubs
}



if __name__ == "__main__":
    for r in [
        Ranks.Ace,
        # Ranks.Two,
        # Ranks.Three, Ranks.Four, Ranks.Five, Ranks.Six,
        #       Ranks.Seven, Ranks.Eight, Ranks.Nine,
        #       Ranks.Ten
    ]:
        generate_card_image(Suits.Spades.value, r.value)
