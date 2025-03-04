import pyxel

def draw_house(x, y):
    pyxel.tri(x, y, x-5, y+5, x+5, y+5, 8)
    pyxel.rect(x-3, y+6, 7, 7, 7)
    pyxel.circ(x, y+9, 2, 6)

pyxel.init(100, 100, title="Exercise")

#draw_house(50, 45)
for _ in range(10):
    x,y = pyxel.rndi(5,95),pyxel.rndi(0,88)
    draw_house(x,y)

pyxel.show()
