import constants as const
import random


class World:
    def __init__(self) -> None:

        self.cells = []  # 921600

        for pos in range(const.HEIGHT * const.WIDTH):
            x = pos % const.HEIGHT
            y = pos // const.HEIGHT
            self.cells.append(Cell(pos, x, y))

    def cell(self, x, y):
        return self.cells[y * const.HEIGHT + x]


class Cell:
    def __init__(self, position, x, y, object=None, col=const.BLACK) -> None:
        self.position = position
        self.x = x
        self.y = y
        self.object = object
        self.col = col


def random_point():
    while True:
        cell = random.choice(world.cells)
        if cell.object is None:
            return cell.x, cell.y


world = World()

# print(world.cells)
# w = World(const.WIDTH * const.HEIGHT)        
# print(w.cell(2, 3).object)

# pos = 42
# width = 40
# height = 30
# scale1 = width * height
# print(pos % width, pos // height)
# print(1 * width + 2)


