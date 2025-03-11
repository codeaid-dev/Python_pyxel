import pyxel

pyxel.init(160, 120, title="Exercise")

gravity = 0.1
NUM_CIRCLES = 10
circles = []

class Circle:
    pass

class App:
    def __init__(self):
        for i in range(NUM_CIRCLES):
            c = Circle()
            c.x = pyxel.rndi(10,pyxel.width-10)
            c.y = pyxel.rndi(10, 50)
            c.dy = pyxel.rndf(0.1, 1.0)
            c.color = pyxel.rndi(2,15)
            circles.append(c)

        pyxel.run(self.update, self.draw)

    def update(self):
        for c in circles:
            c.y += c.dy
            c.dy += gravity
            if c.y >= pyxel.height - 10:
                c.y = pyxel.height - 10
                c.dy *= -0.96

    def draw(self):
        pyxel.cls(0)
        for c in circles:
            pyxel.circ(c.x,c.y,10,c.color)

App()
