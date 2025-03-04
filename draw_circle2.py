import pyxel

pyxel.init(100, 100, title="Exercise")
for i in range(5):
    pyxel.circ(10+i*20, 50, 10, 11)

pyxel.show()
