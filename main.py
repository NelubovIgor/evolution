import pygame
import agents_code
import world_code
import constants as cnst
import random
import time

# pygame setup 
pygame.init()
# дисплей
screen = pygame.display.set_mode((cnst.WIDTH, cnst.HEIGHT))
# время в игре
clock = pygame.time.Clock()

world_code.world

agents_code.create_agent(10)
agents_code.create_grass(1000)

surf_agents = pygame.Surface((cnst.WIDTH * cnst.SIZE_CELL, cnst.HEIGHT * cnst.SIZE_CELL), flags=pygame.SRCALPHA)

cycle = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    random.shuffle(agents_code.agents)
    for a in agents_code.agents:
        a.do()

    screen.fill(cnst.BLACK)
    surf_agents.fill(cnst.BLACK)

    for a in agents_code.agents:
        a.draw(surf_agents)

    for g in agents_code.grass:
        g.draw(surf_agents)

    screen.blit(surf_agents, (0, 0))

    pygame.display.flip()

    clock.tick(cnst.FPS)  # Лимит FPS
    cycle += 1
    # time.sleep(0.2)

pygame.quit()
