import textwrap
from PIL import Image, ImageDraw, ImageFont
import requests

URL = "https://api.quotable.io/random"


def gen_quote():
    response = requests.get(URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    generated_quote = quote + "  " + '"' + author + '"'
    return generated_quote


print('done')

# Open the image
image_path = "images/image.png"
image = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Choose a font and size
font_path = "fonts/Arial_Bold.ttf"
font_size = 25
font = ImageFont.truetype(font_path, font_size)

# Specify the text and position
text = gen_quote()
position = (80, 140)

# Choose the color (R, G, B)
text_color = (255, 255, 255)

wrapped_text = textwrap.fill(text, 39)
lines = wrapped_text.split('/n')

# Add text to the image
for i, line in enumerate(lines):
    draw.multiline_text((position[0], position[1] + i * font_size), line, font=font, fill=text_color)
# Save the modified image
output_path = "images/output.png"
image.save(output_path)


# Display the image (optional)
image.show()
print('done!!!')
