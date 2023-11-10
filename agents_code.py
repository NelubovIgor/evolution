import world_code
import constants as cnst
import pygame
import math
import random


class Objects:
    def __init__(self, x, y, color) -> None:

        self.cell = world_code.world.cell(x, y)
        self.cell.object = self
        self.cell.col = color

        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, cnst.SIZE_CELL, cnst.SIZE_CELL)

    def draw(self, surf):
        surf.fill(self.color, self.rect)


class Agent(Objects):
    def __init__(self, x, y, color=cnst.BLUE, energy=50) -> None:
        super().__init__(x, y, color)
        self.energy = energy
        self.points_evol = 10
        self.vision_area = 40

    def do(self):
        self.energy -= 0.1
        self.age()
        food, cell, path = self.touch()
        if self.energy < 200 and food:
            random.shuffle(food)
            self.eat(food[0])
        elif self.energy > 200:
            self.reproduction()
        elif path:
            see_food, see_cell = self.vision()
            if self.energy > 20:
                self.move_to(path, see_food)

    def touch(self):
        cells = world_code.world.cell_around(self.x, self.y, 1)
        feel_food = (c for c in cells if c.col == cnst.GREEN)
        feel_cell = [c for c in cells if c.col == cnst.BLUE]
        clear_path = [c for c in cells if c.object is None]
        # feel_enemy = [c for c in cells if c.col == cnst.RED]
        return feel_food, feel_cell, clear_path

    def vision(self):
        cells = world_code.world.cell_around(self.x, self.y, self.vision_area)
        see_food = {}
        see_cell = {}
        # see_enemy = {}
        for c in cells:
            dx = c.x - self.x
            dy = c.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if c.col == cnst.GREEN:
                see_food[distance] = c
            elif c.col == cnst.BLUE:
                see_cell[distance] = c
        return see_food, see_cell

    def move_to(self, path, targets):
        open_path = [world_code.world.cell_to_cell(self, p) for p in path]
        to = ''
        for k, v in sorted(targets.items()):
            ind_dir = world_code.world.cell_to_cell(self, v)
            bypass = [-1, 1]
            random.shuffle(bypass)
            if ind_dir in open_path:
                to = ind_dir
                break
            elif ind_dir + bypass[0] in open_path:
                to = ind_dir + bypass[0]
                break
            elif ind_dir + bypass[1] in open_path:
                to = ind_dir + bypass[1]
                break
        if isinstance(to, int):
            self.move(cnst.DIRECTIONS[to])
        else:
            random.shuffle(open_path)
            self.move(cnst.DIRECTIONS[open_path[0]])

    def escape(self):
        return

    def move(self, d):
        self.cell.object = None
        self.cell.col = cnst.BLACK
        self.x += d[0]
        self.y += d[1]
        self.cell = world_code.world.cell(self.x, self.y)
        self.cell.col = self.color
        self.cell.object = self
        self.rect = pygame.Rect(self.x, self.y, cnst.SIZE_CELL, cnst.SIZE_CELL)
        self.energy -= 1

    def eat(self, cell):
        grass.remove(cell.object)
        cell.object = None
        cell.col = cnst.BLACK
        self.energy += 15

    def age(self):
        if self.energy <= 0:
            self.cell.object = None
            self.cell.col = cnst.BLACK
            agents.remove(self)

    def reproduction(self):
        near_cell = world_code.world.cell_around(self.x, self.y, 1)
        clear_path = [c for c in near_cell if c.object is None]
        if self.energy > 100 and clear_path:
            self.energy -= 50
            random.shuffle(clear_path)
            x, y = clear_path[0].x,  clear_path[0].y
            agents.append(Agent(x, y))


class Grass(Objects):
    def __init__(self, x, y, birth_cycle, color=cnst.GREEN) -> None:
        color = cnst.GREEN
        super().__init__(x, y, color)
        self.birth_cycle = birth_cycle

    def age(self, cycle):
        age = cycle - self.birth_cycle
        if age >= 2:
            res = self.reproduction(cycle)
            if res:
                self.birth_cycle = cycle

    def reproduction(self, cycle):
        near_cell = world_code.world.cell_around(self.x, self.y, 3)
        # print(near_cell)
        clear_path = [c for c in near_cell if c.object is None]
        # print(clear_path)
        if clear_path:
            random.shuffle(clear_path)
            x, y = clear_path[0].x,  clear_path[0].y
            grass.append(Grass(x, y, cycle))
            return True
        else:
            return False


grass = []
agents = []


def create_agent(count):
    for _ in range(count):
        x, y = world_code.random_point()
        agents.append(Agent(x, y))


def create_grass(count, cycle):
    for _ in range(count):
        x, y = world_code.random_point()
        grass.append(Grass(x, y, cycle))


def test(iteration):
    world_code.world

    agents.append(Agent(0, 0))
    agents.append(Agent(1, 0))
    grass.append(Grass(0, 2))
    grass.append(Grass(2, 2))

    a1 = agents[0]
    a2 = agents[1]

    # g1 = grass[0]
    # print(grass)
    # print(g1.cell.object)
    for _ in range(iteration):
        a1.do()
        print(a1.x, a1.y)
        print(a1.energy)

# test(0)

