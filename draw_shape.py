import pyxel

pyxel.init(100, 100, title="Exercise")
pyxel.pset(10, 12, 7)
pyxel.pset(10, 36, 7)
pyxel.line(20, 5, 38, 45, 8)
pyxel.rect(40, 5, 18, 40, 9)
pyxel.rectb(60, 5, 18, 40, 10)
pyxel.circ(89, 25, 9, 11)

pyxel.circb(10, 75, 9, 12)
pyxel.elli(21, 55, 18, 40, 13)
pyxel.ellib(40, 55, 18,40, 14)
pyxel.tri(68, 55, 58, 95, 78, 95, 15)
pyxel.trib(89, 55, 79, 95, 99, 95, 16)

pyxel.show()
