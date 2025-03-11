import pyxel

pyxel.init(160, 120, title="Exercise")

circles = []
NUM_CIRCLES = 10

class Circle:
    pass

class App:
    def __init__(self):
        for _ in range(NUM_CIRCLES):
            c = Circle()
            c.radius = 5
            c.x = pyxel.rndi(c.radius,
                        pyxel.width-c.radius)
            c.y = pyxel.rndi(c.radius,
                        pyxel.height-c.radius)
            c.dx = pyxel.rndi(2, 3)
            c.dy = pyxel.rndi(2, 3)
            c.color = pyxel.rndi(2, 15)
            circles.append(c)
        pyxel.run(self.update, self.draw)

    def update(self):
        for c in circles:
            c.x += c.dx
            c.y += c.dy
            if c.x > pyxel.width-c.radius or c.x < c.radius:
                c.dx *= -1
            if c.y > pyxel.height-c.radius or c.y < c.radius:
                c.dy *= -1

    def draw(self):
        pyxel.cls(0)
        for c in circles:
            pyxel.circ(c.x,c.y,c.radius,c.color)

App()
