import pygame
import agents_code
import world_code
import constants as const
import random
import time

# pygame setup 
pygame.init()
# дисплей
screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
# время в игре
clock = pygame.time.Clock()

world_code.world

agents_code.create_agent(10)
agents_code.create_grass(1000)

# agents_code.agents.append(agents_code.Agent(50, 40, const.BLUE))
# agents_code.grass.append(agents_code.Grass(58, 40, const.GREEN))

surf_agents = pygame.Surface((const.WIDTH * const.SIZE_CELL, const.HEIGHT * const.SIZE_CELL), flags=pygame.SRCALPHA)

cycle = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    random.shuffle(agents_code.agents)
    for a in agents_code.agents:
        a.vision()
        # print(a.cell.x, a.x)

    screen.fill(const.BLACK)
    surf_agents.fill(const.BLACK)

    for a in agents_code.agents:
        a.draw(surf_agents)

    for g in agents_code.grass:
        g.draw(surf_agents)

    screen.blit(surf_agents, (0, 0))

    pygame.display.flip()

    clock.tick(const.FPS)  # Лимит FPS
    cycle += 1
    # time.sleep(0.2)
    
pygame.quit()
