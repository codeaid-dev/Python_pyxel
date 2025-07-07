import pyxel, random

GAME_TITLE = "Snake Game"
WIDTH, HEIGHT = 100, 100 #画面サイズ
W, H = 20, 20 #画面マス数

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title=GAME_TITLE, fps=5)
        pyxel.load("snake.pyxres")
        self.is_title = True
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.game_over = False
        self.snake = []
        self.head=(int(W/2),int(H/2))
        self.snake.append(self.head)
        for i in range(5):
            self.snake.insert(0, self.head)
        self.init_foods()
        self.key = 'Down'

    def init_foods(self):
        self.foods = []
        for i in range(10):
            while True:
                pos = (random.randint(0,W-1),random.randint(0,H-1))
                if not pos in self.foods and pos != self.head:
                    self.foods.append(pos)
                    break

    def eat(self):
        for food in list(self.foods):
            if self.head == food:
                self.foods.remove(food)
        if len(self.foods) == 0:
            self.init_foods()

    def update(self):
        # タイトル画面の時はRETURNキー(ENTERキー)の入力を待つ
        if self.is_title:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.is_title = False
                self.reset_game()
        elif not self.game_over:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.key = 'Left'
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.key = 'Right'
            if pyxel.btn(pyxel.KEY_UP):
                self.key = 'Up'
            if pyxel.btn(pyxel.KEY_DOWN):
                self.key = 'Down'
            if self.key == 'Left':
                self.head = (self.snake[0][0]-1, self.snake[0][1])
            if self.key == 'Right':
                self.head = (self.snake[0][0]+1, self.snake[0][1])
            if self.key == 'Up':
                self.head = (self.snake[0][0], self.snake[0][1]-1)
            if self.key == 'Down':
                self.head = (self.snake[0][0], self.snake[0][1]+1)
            if self.head in self.snake \
                or self.head[0]<0 \
                or self.head[0]>W-1 \
                or self.head[1]<0 \
                or self.head[1]>H-1:
                self.game_over = True
            self.snake.insert(0, self.head)

            if self.head in self.foods:
                self.eat()
            else:
                self.snake.pop()

        if pyxel.btnp(pyxel.KEY_R):
            self.is_title = True

    def draw_snake(self):
        pyxel.cls(0)
        yoko = WIDTH//W
        tate = HEIGHT//H
        for body in self.snake:
            pyxel.rect(body[0]*yoko,
                       body[1]*tate,
                       yoko,
                       tate,
                       7)

    def draw_foods(self):
        yoko = WIDTH//W
        tate = HEIGHT//H
        for food in self.foods:
            pyxel.blt(food[0]*yoko,
                      food[1]*tate,
                      0, 0, 0, yoko, tate, 0)

    def draw_game_over(self):
        over = "GAME OVER"
        x = WIDTH / 2 - (len(over)*4 / 2)
        y = HEIGHT / 2 - 5
        pyxel.text(x, y, over, 2)

    def draw_title(self): #タイトルを描画する
        pyxel.cls(0)
        x = WIDTH / 2 - (len(GAME_TITLE)*4 / 2)
        y = HEIGHT / 2 - 5
        for i in range(1, -1, -1):
            color = 10 if i == 0 else 8
            pyxel.text(x, y + i, GAME_TITLE, color)
        press = "- Press Enter Key -"
        x = WIDTH / 2 - (len(press)*4 / 2)
        pyxel.text(x, y+20, press, 3)

    def draw(self):
        if self.is_title: #タイトルを描画する
            self.draw_title()
        else: #ゲーム画面を描画する
            self.draw_snake()
            self.draw_foods()
            if self.game_over:
                self.draw_game_over()

App()
