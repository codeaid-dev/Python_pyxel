import pyxel

pyxel.init(160, 120, title="Exercise")

x = []
y = []
dy = []
gravity = 0.1
colors = []
NUM_CIRCLES = 10

for i in range(NUM_CIRCLES):
    x.append(pyxel.rndi(10,pyxel.width-10))
    y.append(pyxel.rndi(10, 50))
    dy.append(pyxel.rndf(0.1, 1.0))
    colors.append(pyxel.rndi(2,15))

def update():
    for i in range(NUM_CIRCLES):
        y[i] += dy[i]
        dy[i] += gravity
        if y[i] >= pyxel.height - 10:
            y[i] = pyxel.height - 10
            dy[i] *= -0.96

def draw():
    pyxel.cls(0)
    for i in range(NUM_CIRCLES):
        pyxel.circ(x[i],y[i],10,colors[i])

pyxel.run(update, draw)
