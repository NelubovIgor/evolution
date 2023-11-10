from pygame import init, SRCALPHA, Color, draw, font, Surface
import constants as cnst

init()

f_arial = font.Font('arial.ttf', 11)


def display_text(surf, text, x, y):

    max_w = 0
    for line in text:
        str_w = f_arial.render(line, False, cnst.WHITE).get_width()
        if str_w > max_w:
            max_w = str_w

    w = max_w - 1 + 10

    strings = len(text)
    h = strings * 12 - 4 + 10
    s = Surface((w, h), flags=SRCALPHA)
    s.fill(Color(0, 0, 0, 127))

    delay = 0
    for line in text:
        s.blit(f_arial.render(line, False, cnst.WHITE), (5, delay - 2 + 5))
        delay += 12

    draw.rect(s, cnst.GRAY_DARK, (0, 0, w, h), 1)

    surf.blit(s, (x, y))
