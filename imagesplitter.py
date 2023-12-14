# Google generated code from search term "split large image into tiles python"

import numpy as np
from PIL import Image

def split_image(image, tile_size):
  """Splits an image into tiles of a given size.

  Args:
    image: A PIL Image object.
    tile_size: The size of the tiles, in pixels.

  Returns:
    A list of PIL Image objects, each containing a tile of the original image.
  """

  image_width, image_height = image.size
  num_tiles_x = int(np.ceil(image_width / tile_size))
  num_tiles_y = int(np.ceil(image_height / tile_size))

  tiles = []
  for i in range(num_tiles_x):
    for j in range(num_tiles_y):
      tile = image.crop((i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size))
      tiles.append(tile)

  return tiles


# # Example usage:

# image = Image.open("large_image.jpg")
# tiles = split_image(image, 256)

# for i, tile in enumerate(tiles):
#   tile.save(f"tile_{i}.jpg")