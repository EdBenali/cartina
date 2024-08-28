from constants import TRANSPARENT, WHITE
from PIL import Image, ImageDraw

CARD_WIDTH, CARD_HEIGHT = 256, 384


def create_blank_card():
    # Create a blank image
    img = Image.new('RGBA', (CARD_WIDTH, CARD_HEIGHT), color=TRANSPARENT)
    draw = ImageDraw.Draw(img)
    # Draw background
    ellipse_margin = CARD_WIDTH // 5
    ellipse = [(-ellipse_margin, -ellipse_margin),
               (CARD_WIDTH + ellipse_margin, CARD_HEIGHT + ellipse_margin)]
    draw.ellipse(xy=ellipse, fill=WHITE)
    return draw, img