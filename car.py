from PIL import Image


class Car:
    def __init__(self, picture, tile_size):
        side_length = len(picture[0]) * tile_size

        result = Image.new("RGB", (side_length, side_length))

        self.x = 0
        self.y = 0
        self.side_length = None
        self.tiles_per_side = None
        self.result = result
        self.tile_size = tile_size

        self.add_picture(picture)

    def add_picture(self, picture):
        for row in picture:
            self.add_row(row)

    def add_row(self, list_of_colors):
        tiles_per_side = len(list_of_colors)
        side_length = len(list_of_colors) * self.tile_size

        if self.tiles_per_side is None:
            self.tiles_per_side = tiles_per_side

        if self.side_length is None:
            self.side_length = side_length

        if self.tiles_per_side != tiles_per_side:
            raise Exception("Rows have different numbers of colors!")

        if self.side_length != side_length:
            raise Exception("Rows have different numbers of colors!")

        for color in list_of_colors:
            self.add_tile_to_row(color)

        self.y = self.y + 1
        self.x = 0

    def add_tile_to_row(self, color):
        tile = Image.new('RGB', (self.tile_size, self.tile_size), color=color)
        self.result.paste(tile, (self.x * self.tile_size, self.y * self.tile_size))

        self.x = self.x + 1
