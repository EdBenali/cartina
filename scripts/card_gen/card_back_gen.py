from constants import RED
from scripts.card_utils import CARD_WIDTH, CARD_HEIGHT, create_blank_card

# Create blank card
draw, img = create_blank_card()


# Define card border
border_width = CARD_WIDTH // 10
draw.rectangle(
    [border_width, border_width, CARD_WIDTH - border_width, CARD_HEIGHT - border_width],
    outline=RED
)

# Create a simple pattern
pattern_color = RED
pattern_thickness = 2

# Draw horizontal lines
for y in range(border_width + border_width, CARD_HEIGHT - border_width, border_width):
    draw.line([(border_width, y), (CARD_WIDTH - border_width, y)], fill=pattern_color, width=pattern_thickness)

# Draw vertical lines
for x in range(border_width + border_width, CARD_WIDTH - border_width, border_width):
    draw.line([(x, border_width), (x, CARD_HEIGHT - border_width)], fill=pattern_color, width=pattern_thickness)

# Save the image
img.save('card_images/card_back.png')

# img.show()