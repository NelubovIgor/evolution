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
    def __init__(self, x, y, color=cnst.BLUE, energy=150) -> None:
        super().__init__(x, y, color)
        self.energy = energy
        self.speed = 2
        self.points_evol = 10
        self.vision_area = 2

    def do(self):
        food, cell, path = self.touch()
        if self.energy < 200 and food:
            random.shuffle(food)
            self.eat(food[0])
        elif self.energy > 200:
            self.reproduction()
        elif path:
            self.vision(path)

    def touch(self):
        cells = world_code.world.cell_around(self.x, self.y, 1)
        feel_food = [c for c in cells if c.col == cnst.GREEN]
        feel_cell = [c for c in cells if c.col == cnst.BLUE]
        clear_path = [c for c in cells if c.object is None]
        # feel_enemy = [c for c in cells if c.col == cnst.RED]
        return feel_food, feel_cell, clear_path

    def vision(self, path):
        cells = world_code.world.cell_around(self.x, self.y, self.vision_area)
        see_food = {}
        see_cell = {}
        # see_enemy = {}
        for c in cells:
            dx = c.x - self.x
            dy = c.y - self.y
            print(path) # написать код для определения доступности направления к объекту
            print(dx, dy)
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if c.col == cnst.GREEN:
                see_food[distance * -1] = c
            elif c.col == cnst.BLUE:
                see_cell[distance * -1] = c

    def move_to(self, targets):
        res = list(targets.values())[0]
        # print(res.x, res.y, self.x, self.y)
        deadlock = set()
        for k, v in targets.items():
            if len(deadlock) == 8:
                break
            x = self.x - v.x
            y = self.y - v.y
            dir_x = -int(x / abs(x)) if x != 0 else 0
            dir_y = -int(y / abs(y)) if y != 0 else 0
            direction = [(dir_x, dir_y)]
            # print(direction, k)
            if direction[0] in deadlock:
                continue
            index = cnst.DIRECTIONS.index(direction[0])
            if index == 0: index = 8
            bypass = [-7, -9]
            random.shuffle(bypass)
            direction.extend((cnst.DIRECTIONS[index + b] for b in bypass))
            deadlock.update(direction)
            for d in direction:
                cell = world_code.world.cell(self.x + d[0],self.y + d[1])
                # print(cell.object)
                # print(cell.x, cell.y)
                if cell.col == cnst.GREEN:
                    print('eat')
                    self.eat(cell)
                    break
                elif cell.object is None:
                    self.move(d)
                    break

    # def move_to(self, targets):
    #     res = list(targets.values())[0]
    #     # print(res.x, res.y, self.x, self.y)
    #     deadlock = set()
    #     for k, v in targets.items():
    #         if len(deadlock) == 8:
    #             break
    #         x = self.x - v.x
    #         y = self.y - v.y
    #         dir_x = -int(x / abs(x)) if x != 0 else 0
    #         dir_y = -int(y / abs(y)) if y != 0 else 0
    #         direction = [(dir_x, dir_y)]
    #         # print(direction, k)
    #         if direction[0] in deadlock:
    #             continue
    #         index = cnst.DIRECTIONS.index(direction[0])
    #         if index == 0: index = 8
    #         bypass = [-7, -9]
    #         random.shuffle(bypass)
    #         direction.extend((cnst.DIRECTIONS[index + b] for b in bypass))
    #         deadlock.update(direction)
    #         for d in direction:
    #             cell = world_code.world.cell(self.x + d[0],self.y + d[1])
    #             # print(cell.object)
    #             # print(cell.x, cell.y)
    #             if cell.col == cnst.GREEN:
    #                 print('eat')
    #                 self.eat(cell)
    #                 break
    #             elif cell.object is None:
    #                 self.move(d)
    #                 break

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
        self.energy -= self.speed / 10

    def eat(self, cell):
        grass.remove(cell.object)
        cell.object = None
        cell.col = cnst.BLACK
        self.energy += 15

    def age(self):
        age_now = time.time() - self.birth
        if age_now > 5 and self.speed == 1:
            self.speed += 1
        elif age_now > 10 and self.speed == 2:
            self.speed += 1
        elif age_now > 15:
            self.kill()
            agents.remove(self)

    def reproduction(self):
        if self.energy > 100:
            self.energy -= 50
            agents.append(Agent(self.rect.center))


class Grass(Objects):
    def __init__(self, x, y, color=cnst.GREEN) -> None:
        color = cnst.GREEN
        super().__init__(x, y, color)


grass = []
agents = []


def create_agent(count):
    for _ in range(count):
        x, y = world_code.random_point()
        agents.append(Agent(x, y, cnst.BLUE))


def create_grass(count):
    for _ in range(count):
        x, y = world_code.random_point()
        grass.append(Grass(x, y, cnst.GREEN))


world_code.world


agents.append(Agent(0, 0))
agents.append(Agent(1, 0))
grass.append(Grass(0, 2))


a1 = agents[0]
a2 = agents[1]

# g1 = grass[0]
# print(grass)
# print(g1.cell.object)
a1.do()
print('do')
# print(grass[0])
print(a1.energy)

# cycle = 0
# while cycle < 11:
#     agents[0].vision()
#     cycle += 1

# create_grass(1)
# print(grass[0].cell.col)
# a = Agent(2, 3, const.BLUE)
# print(a)





# def vision(self):
#     self.what_see = {}
#     start_x, end_x = self.x - self.vision_area, self.x + self.vision_area
#     start_y, end_y = self.y - self.vision_area, self.y + self.vision_area
#     if start_x < 0: start_x = 0
#     if start_y < 0: start_y = 0
#     if end_x > const.WIDTH - 1: end_x = const.WIDTH - 1
#     if end_y > const.HEIGHT - 1: end_y = const.HEIGHT - 1
#     for x in range(start_x, end_x + 1):
#         for y in range(start_y, end_y + 1):
#             if x == self.x and y == self.y:
#                 continue
#             cell_chek = world_code.world.cell(x, y)
#             if cell_chek.object:
#                 dx = x - self.x
#                 dy = y - self.y
#                 distance = math.sqrt(dx ** 2 + dy ** 2)
#                 self.what_see[distance * -1] = cell_chek
#     food = dict()
#     for k, v in self.what_see.items():
#         if v.col == const.GREEN:
#             food[k] = v
#     if food:
#         self.move_to(dict(sorted(food.items(), reverse=True)))
