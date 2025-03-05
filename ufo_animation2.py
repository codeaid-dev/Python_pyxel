import pyxel

def draw_ufo(x, y, body_color, window_color):
    pyxel.elli(x, y, 11, 5, body_color)
    for i in range(4):
        pyxel.pset(x+2+i*2, y+2, window_color)

pyxel.init(100, 100, title="Exercise")

ufo_x = [pyxel.rndi(0,95) for _ in range(10)]
ufo_y = [pyxel.rndi(0,95) for _ in range(10)]

while True:
    pyxel.cls(1)
    for i in range(len(ufo_x)):
        draw_ufo(ufo_x[i], ufo_y[i], 7, 8)
        ufo_x[i] += 1
        if ufo_x[i] >= pyxel.width:
            ufo_x[i] = -11
    pyxel.flip()
