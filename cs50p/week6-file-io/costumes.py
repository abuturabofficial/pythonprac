import sys
from PIL import Image

images = []

if len(sys.argv) <= 2:
    sys.exit("No enough command-line arguments")

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "constumes.gif", save_all=True, append_images=[images[1]],
    duration=200, loop=0
)
