import constants as cnst
import random


class World:
    def __init__(self) -> None:

        self.cells = []  # 921600

        for pos in range(cnst.HEIGHT * cnst.WIDTH):
            x = pos % cnst.HEIGHT
            y = pos // cnst.HEIGHT
            self.cells.append(Cell(pos, x, y))

    def cell(self, x, y):
        return self.cells[y * cnst.HEIGHT + x]

    def cell_around(self, x, y, distance):
        cells = []
        start_x, end_x = x - distance, x + distance
        start_y, end_y = y - distance, y + distance
        if start_x < 0:
            start_x = 0
        if start_y < 0:
            start_y = 0
        if end_x > cnst.WIDTH - 1:
            end_x = cnst.WIDTH - 1
        if end_y > cnst.HEIGHT - 1:
            end_y = cnst.HEIGHT - 1
        for x_i in range(start_x, end_x + 1):
            for y_i in range(start_y, end_y + 1):
                if x == x_i and y == y_i:
                    pass
                # elif distance > 1:
                #     cell = self.cell(x_i, y_i)
                #     if cell.object is not None:
                #         cells.append(cell)
                else:
                    cells.append(self.cell(x_i, y_i))
        return cells

    def cell_to_cell(self, obj1, obj2):
        x = obj1.x - obj2.x
        y = obj1.y - obj2.y
        dir_x = -int(x / abs(x)) if x != 0 else 0
        dir_y = -int(y / abs(y)) if y != 0 else 0
        return cnst.DIRECTIONS.index((dir_x, dir_y))


class Cell:
    def __init__(self, position, x, y, object=None, col=cnst.BLACK) -> None:
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


