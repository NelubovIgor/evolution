import pygame
import agents_code
import world_code
import constants as cnst
import random
import pg_textblocks
import time

# pygame setup
pygame.init()
# дисплей
screen = pygame.display.set_mode((cnst.WIDTH, cnst.HEIGHT))
# время в игре
clock = pygame.time.Clock()

world_code.world
cycle = 0
agents_code.create_agent(10)
agents_code.create_grass(100, cycle)

surf_agents = pygame.Surface((cnst.WIDTH * cnst.SIZE_CELL, cnst.HEIGHT * cnst.SIZE_CELL), flags=pygame.SRCALPHA)


running = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cycle % 50 == 0:
        agents_code.create_grass(100, cycle)
        random.shuffle(agents_code.grass)
        for g in agents_code.grass:
            g.age(cycle)

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
    text_1 = ['fps: {}'.format(round(clock.get_fps(), 1)),
              'bots: {}'.format(len(agents_code.agents)),
              'trees {}'.format(len(agents_code.grass))]

    pg_textblocks.display_text(screen, text_1, 5, 5)
    pygame.display.flip()

    clock.tick(cnst.FPS)  # Лимит FPS
    cycle += 1
    # time.sleep(0.2)


pygame.quit()


def time_check():
    return


def test_without_animation():
    global cycle
    while True:
        point = cycle % 30 == 0
        if point:
            start = time.time()
        if cycle % 50 == 0:
            agents_code.create_grass(100, cycle)
            random.shuffle(agents_code.grass)
            for g in agents_code.grass:
                g.age(cycle)

        random.shuffle(agents_code.agents)
        for a in agents_code.agents:
            a.do()
        if point:
            end = time.time()
            speed = round(end - start, 3)
            print(f'скорость кода: {speed}, цикл: {cycle}')
        if cycle == 300:
            break
        cycle += 1


# test_without_animation()
