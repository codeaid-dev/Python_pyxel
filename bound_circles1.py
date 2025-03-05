import pyxel

pyxel.init(160, 120, title="Exercise")

x = [20, 50, 80, 110, 140]
y = [20, 40, 10, 30, 50]
dy = [0] * 5
gravity = 0.1
colors = [6, 5, 10, 3, 2]

while True:
    pyxel.cls(0)
    for i in range(5):
        y[i] += dy[i]
        dy[i] += gravity
        if y[i] >= pyxel.height - 10:
            y[i] = pyxel.height - 10
            dy[i] *= -0.96
        pyxel.circ(x[i],y[i],10,colors[i])
    pyxel.flip()
