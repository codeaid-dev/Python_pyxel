import pyxel

pyxel.init(160, 120, title="Exercise")

x,y = 80,10
dy = 0
gravity = 0.1

while True:
    y += dy
    dy += gravity
    if y >= pyxel.height - 10:
        y = pyxel.height - 10
        dy *= -0.96
    pyxel.cls(0)
    pyxel.circ(x,y,10,10)
    pyxel.flip()
