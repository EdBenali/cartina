from PIL import Image, ImageDraw, ImageFont

from enums import Rank, Suit

BLACK = (0, 0, 0)
WHITE = (255,255,255)
WIDTH, HEIGHT = 256, 384

def generate_card_image(suit: Suit, rank: Rank):
    background_color = WHITE # White background

    # Create a blank image
    img = Image.new('RGB', (WIDTH, HEIGHT), color=background_color)
    draw = ImageDraw.Draw(img)

    # Font settings
    font_size = 32  # Adjust the size for the 'A'
    font = ImageFont.load_default(font_size)

    # Drawing 'A' at the corners
    text_positions = [(10, 10), (WIDTH - 30, HEIGHT - 40)]
    for pos in text_positions:
        draw.text(pos, rank.symbol, font=font, fill=suit.colour)

    _draw_suit(suit, draw)

    # Resize to give a pixelated effect
    img = img.resize(
        (int(WIDTH / 2), int(HEIGHT / 2)),
        Image.NEAREST
    ).resize((WIDTH, HEIGHT), Image.NEAREST)

    # Save the image
    img.save(f"card_images/{rank.symbol}_of_{suit.value}.png")

    # Show the image (optional)
    img.show()

def _draw_suit(suit: Suit, draw):
    # Draw the spade symbol (simple triangle shape)
    spade_size = 100
    spade_position = (WIDTH // 2, HEIGHT // 2)
    triangle = [
        (spade_position[0], spade_position[1] - spade_size // 2),  # Top
        (spade_position[0] - spade_size // 2,
         spade_position[1] + spade_size // 2),
        # Bottom left
        (spade_position[0] - spade_size // 2,
         spade_position[1] + spade_size // 2),
        (spade_position[0] + spade_size // 2,
         spade_position[1] + spade_size // 2)
        # Bottom right
    ]
    draw.polygon(triangle, fill=suit.colour)

    # Draw the spade tail
    draw.rectangle(
        [spade_position[0] - 10, spade_position[1] + spade_size // 2 - 10,
         spade_position[0] + 10, spade_position[1] + spade_size // 2 + 40],
        fill=suit.colour
    )
