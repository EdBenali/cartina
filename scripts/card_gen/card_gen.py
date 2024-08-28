from PIL import Image, ImageDraw, ImageFont

from enums import Rank, Suit, Suits, Ranks, RankGroup
from scripts.card_utils import CARD_WIDTH, CARD_HEIGHT, create_blank_card

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


def generate_card_image(suit: Suit, rank: Rank, show_image: bool = False):
    draw, img = create_blank_card()

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

    if show_image:
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


def _draw_suit(suit: Suit, draw: ImageDraw, rank: Rank, ):
    # Draw the suit symbol
    draw_suit_func = DRAW_SUIT_FUNCS[suit.value]

    # Aces
    if rank.group == RankGroup.Ace:
        draw_suit_func(
            symbol_pos=CARD_CENTRE,
            symbol_size=SYMBOL_SIZE,
            colour=suit.colour,
            draw=draw)
    elif rank.group == RankGroup.Face:
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
    else:
        raise ValueError(f"Unkown rank group passed to _draw_suit: "
                         f"{RankGroup.Ace.value}")


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
            symbol_pos[0] + symbol_size // 10,
            symbol_pos[1] + symbol_size // 2 +
            (symbol_size // 10) * 4],
        fill=colour
    )


def _draw_diamonds(symbol_pos: tuple,
                   symbol_size: int,
                   colour: tuple,
                   draw: ImageDraw):
    diamond = [
        (symbol_pos[0], symbol_pos[1] - symbol_size // 1.6),  # Top
        (symbol_pos[0] + symbol_size // 2, symbol_pos[1]),  # Right
        (symbol_pos[0], symbol_pos[1] + symbol_size // 1.6),  # Bottom
        (symbol_pos[0] - symbol_size // 2, symbol_pos[1])  # Left
    ]
    draw.polygon(xy=diamond, fill=colour)


def _draw_hearts(symbol_pos: tuple,
                 symbol_size: int,
                 colour: tuple,
                 draw: ImageDraw):
    triangle = [
        (symbol_pos[0], symbol_pos[1] + symbol_size // 2),  # Bottom
        (symbol_pos[0] + symbol_size // 2,
         symbol_pos[1] - symbol_size // 2),
        # Top left
        (symbol_pos[0] + symbol_size // 2,
         symbol_pos[1] - symbol_size // 2),
        (symbol_pos[0] - symbol_size // 2,
         symbol_pos[1] - symbol_size // 2)
        # Top right
    ]
    draw.polygon(xy=triangle, fill=colour)

    # Draw left slice
    l_slice = [
        (symbol_pos[0] - symbol_size // 2, symbol_pos[1] - symbol_size +
         symbol_size // 4),
        (symbol_pos[0], symbol_pos[1] - symbol_size // 4)]
    draw.pieslice(
        xy=l_slice,
        start=180,
        end=360,
        fill=colour)

    # Draw right slice
    r_slice = [(symbol_pos[0], symbol_pos[1] - symbol_size + symbol_size // 4),
               (symbol_pos[0] + symbol_size // 2,
                symbol_pos[1] - symbol_size // 4)]
    draw.pieslice(
        xy=r_slice,
        start=180,
        end=360,
        fill=colour)


def _draw_clubs(symbol_pos: tuple,
                symbol_size: int,
                colour: tuple,
                draw: ImageDraw):
    circle_coords = [
        (symbol_pos[0], symbol_pos[1] - symbol_size // 4),  # Top
        (symbol_pos[0] - symbol_size // 4,
         symbol_pos[1] + symbol_size // 4),  # Bottom left
        (symbol_pos[0] + symbol_size // 4,
         symbol_pos[1] + symbol_size // 4)  # Bottom right
    ]

    for xy in circle_coords:
        draw.circle(xy=xy,
                    radius=symbol_size // 4,
                    fill=colour)

    draw.polygon(xy=circle_coords, fill=colour)

    # Draw the spade tail
    draw.rectangle(
        xy=[
            (symbol_pos[0] - symbol_size // 15, symbol_pos[1]),
            (symbol_pos[0] + symbol_size // 15,
            symbol_pos[1] + symbol_size // 2 + symbol_size // 10)
        ],
        fill=colour
    )


DRAW_SUIT_FUNCS = {
    Suits.Spades.value.value: _draw_spades,
    Suits.Diamonds.value.value: _draw_diamonds,
    Suits.Hearts.value.value: _draw_hearts,
    Suits.Clubs.value.value: _draw_clubs
}

if __name__ == "__main__":
    for r in Ranks:
        for s in Suits:
            generate_card_image(s.value, r.value)
