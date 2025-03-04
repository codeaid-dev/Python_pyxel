import pyxel

def draw_ufo(x, y, body_color, window_color):
    pyxel.elli(x, y, 11, 5, body_color)
    for i in range(4):
        pyxel.pset(x+2+i*2, y+2, window_color)

pyxel.init(100, 100, title="Exercise")

ufo_x = 0

while True:
    pyxel.cls(1)
    draw_ufo(ufo_x, 50, 7, 8)
    pyxel.flip()
    ufo_x += 1
    if ufo_x >= pyxel.width:
        ufo_x = -11
