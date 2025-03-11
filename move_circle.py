import pyxel

pyxel.init(160, 120, title="Exercise")

circle = None

class Circle:
    pass

class App:
    def __init__(self):
        global circle
        c = Circle()
        c.x = pyxel.width/2
        c.y = pyxel.height/2
        c.dx, c.dy = 2, 3
        c.color = 10
        c.radius = 5
        circle = c
        pyxel.run(self.update, self.draw)

    def update(self):
        circle.x += circle.dx
        circle.y += circle.dy
        if circle.x > pyxel.width-circle.radius or circle.x < circle.radius:
            circle.dx *= -1
        if circle.y > pyxel.height-circle.radius or circle.y < circle.radius:
            circle.dy *= -1

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(circle.x,circle.y,circle.radius,circle.color)

App()
