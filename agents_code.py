import world_code
import constants as const
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
        self.rect = pygame.Rect(self.x, self.y, const.SIZE_CELL, const.SIZE_CELL)

    def draw(self, surf):
        surf.fill(self.color, self.rect)


class Agent(Objects):
    def __init__(self, x, y, color, energy=200) -> None:
        super().__init__(x, y, color)
        self.energy = energy
        self.speed = 2
        self.points_evol = 1
        self.vision_area = 40

    def vision(self):
        self.what_see = {}
        start_x, end_x = self.x - self.vision_area, self.x + self.vision_area
        start_y, end_y = self.y - self.vision_area, self.y + self.vision_area
        if start_x < 0: start_x = 0
        if start_y < 0: start_y = 0
        if end_x > const.WIDTH - 1: end_x = const.WIDTH - 1
        if end_y > const.HEIGHT - 1: end_y = const.HEIGHT - 1
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if x == self.x and y == self.y:
                    continue
                cell_chek = world_code.world.cell(x, y)
                if cell_chek.object:
                    dx = x - self.x
                    dy = y - self.y
                    distance = math.sqrt(dx ** 2 + dy ** 2)
                    self.what_see[distance * -1] = cell_chek
        food = dict()
        for k, v in self.what_see.items():
            if v.col == const.GREEN:
                food[k] = v
        if food:
            self.move_to(dict(sorted(food.items(), reverse=True)))

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
            index = const.DIRECTIONS.index(direction[0])
            if index == 0: index = 8
            bypass = [-7, -9]
            random.shuffle(bypass)
            direction.extend((const.DIRECTIONS[index + b] for b in bypass))
            deadlock.update(direction)
            for d in direction:
                cell = world_code.world.cell(self.x + d[0],self.y + d[1])
                # print(cell.object)
                # print(cell.x, cell.y)
                if cell.col == const.GREEN:
                    print('eat')
                    self.eat(cell)
                    break
                elif cell.object is None:
                    self.move(d)
                    break

    def escape(self):
        return

    def move(self, d):
        self.cell.object = None
        self.cell.col = const.BLACK
        self.x += d[0]
        self.y += d[1]
        self.cell = world_code.world.cell(self.x, self.y)
        self.cell.col = self.color
        self.cell.object = self
        self.rect = pygame.Rect(self.x, self.y, const.SIZE_CELL, const.SIZE_CELL)
        self.energy -= self.speed / 10

    def eat(self, cell):
        cell.object = None
        cell.col = const.BLACK
        self.energy += 15
        del cell

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
    def __init__(self, x, y, color) -> None:
        color = const.GREEN
        super().__init__(x, y, color)

    def __del__(self):
        return


grass = []
agents = []


def create_agent(count):
    for _ in range(count):
        x, y = world_code.random_point()
        agents.append(Agent(x, y, const.BLUE))


def create_grass(count):
    for _ in range(count):
        x, y = world_code.random_point()
        grass.append(Grass(x, y, const.GREEN))

# agents.append(Agent(50, 40, const.BLUE))
# grass.append(Grass(60, 40, const.GREEN))
# a = agents[0].cell
# g = grass[0].cell
# ag = agents[0]
# gr = grass[0]
# print(a.x, a.y, a.position, ag.rect, ag.x, ag.y)
# print(g.x, g.y, g.position, gr.rect, gr.x, gr.y)
# cycle = 0
# while cycle < 11:
#     agents[0].vision()
#     cycle += 1

# create_grass(1)
# print(grass[0].cell.col)
# a = Agent(2, 3, const.BLUE)
# print(a)
