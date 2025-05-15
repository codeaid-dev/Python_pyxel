import pyxel
import time

GAME_TITLE = "Maze Exploration"  # ゲームタイトル
WIDTH, HEIGHT = 168, 168

class Sprite:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 1
        self.status = True

class App:
    def __init__(self):
        # Pyxelを初期化する
        pyxel.init(WIDTH, HEIGHT, title=GAME_TITLE, fps=10)

        # リソースファイルを読み込む
        pyxel.load("resource.pyxres")

        # はじめはタイトル画面を表示する
        self.is_title = True

        # アプリの実行を開始する
        pyxel.run(self.update, self.draw)

    # ゲームをリセットする
    def reset_game(self):
        # 迷路を作成する
        self.mazew,self.mazeh = 21,21
        self.maze = [[0 for x in range(self.mazew)] for y in range(self.mazeh)]
        self.make_maze()
        self.set_goal()
        self.player = Sprite()
        self.start = time.time()

    # 迷路を作成する
    def make_maze(self):
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        #柱を建てて壁を作る
        for y in range(1,self.mazeh-1,2):
            for x in range(1,self.mazew-1,2):
                self.maze[y][x] = 1
                d = pyxel.rndi(0,2)
                if y == 1:
                    d = pyxel.rndi(0,3)
                self.maze[y+dy[d]][x+dx[d]] = 1

    # ゴールを設定する
    def set_goal(self):
        self.goal = False
        while True:
            self.goal_x = pyxel.rndi(0,self.mazew-1)
            self.goal_y = pyxel.rndi(0,self.mazeh-1)
            if self.maze[self.goal_y][self.goal_x] == 0:
                if self.goal_x != 0 and self.goal_y != 0:
                    break

    # 迷路の壁を描画する
    def draw_maze(self):
        pyxel.cls(0)
        for y in range(self.mazeh):
            for x in range(self.mazew):
                if self.maze[y][x] == 1:
                    pyxel.blt(x*8,y*8,0,0,0,8,8,0)
                if self.maze[y][x] == 0:
                    pyxel.circ(x*8+4,y*8+4,1,10)

    # プレイヤーを描画する
    def draw_player(self):
        if self.player.dir == 0 and self.player.status: # 左向き
            pyxel.blt(self.player.x*8,self.player.y*8,0,8,0,8,8,0)
        elif self.player.dir == 1 and self.player.status: # 右向き
            pyxel.blt(self.player.x*8,self.player.y*8,0,16,0,8,8,0)
        elif self.player.dir == 2 and self.player.status: # 上向き
            pyxel.blt(self.player.x*8,self.player.y*8,0,24,0,8,8,0)
        elif self.player.dir == 3 and self.player.status: # 下向き
            pyxel.blt(self.player.x*8,self.player.y*8,0,32,0,8,8,0)
        else: # 口を閉じている
            pyxel.blt(self.player.x*8,self.player.y*8,0,40,0,8,8,0)

    # ゴールを表示する
    def draw_goal(self):
        if self.goal:
            pyxel.circ(self.player.x*8+4, self.player.y*8+4, 4, 8)
            goal = "GOAL!!"
            x = (WIDTH/2) - (len(goal)*4/2)
            y = HEIGHT/2 - 5
            pyxel.text(x, y, goal, 3)
            passedtime = f"{self.passed:.0f} Seconds"
            x = (WIDTH/2) - (len(passedtime)*4/2)
            pyxel.text(x, y+6, passedtime, 3)

    # アプリを更新する
    def update(self):
        # タイトル画面の時はRETURNキー(ENTERキー)の入力を待つ
        if self.is_title:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.is_title = False
                self.reset_game()
        else:
            if not self.goal:
                x, y = self.player.x, self.player.y
                if pyxel.btn(pyxel.KEY_LEFT) and x-1 > -1 and (self.maze[y][x-1] == 0 or self.maze[y][x-1] == 2):
                    self.player.x -= 1
                    self.player.dir = 0
                    self.player.status = not self.player.status
                    if self.maze[y][x-1] == 0:
                        pyxel.play(0,0)
                        self.maze[y][x-1] = 2
                if pyxel.btn(pyxel.KEY_RIGHT) and x+1 < self.mazew and (self.maze[y][x+1] == 0 or self.maze[y][x+1] == 2):
                    self.player.x += 1
                    self.player.dir = 1
                    self.player.status = not self.player.status
                    if self.maze[y][x+1] == 0:
                        pyxel.play(0,0)
                        self.maze[y][x+1] = 2
                if pyxel.btn(pyxel.KEY_UP) and y-1 > -1 and (self.maze[y-1][x] == 0 or self.maze[y-1][x] == 2):
                    self.player.y -= 1
                    self.player.dir = 2
                    self.player.status = not self.player.status
                    if self.maze[y-1][x] == 0:
                        pyxel.play(0,0)
                        self.maze[y-1][x] = 2
                if pyxel.btn(pyxel.KEY_DOWN) and y+1 < self.mazeh and (self.maze[y+1][x] == 0 or self.maze[y+1][x] == 2):
                    self.player.y += 1
                    self.player.dir = 3
                    self.player.status = not self.player.status
                    if self.maze[y+1][x] == 0:
                        pyxel.play(0,0)
                        self.maze[y+1][x] = 2

                for masu in self.maze:
                    if 0 in masu:
                        break
                else:
                    self.goal = True
                    self.passed = time.time()-self.start

        if pyxel.btnp(pyxel.KEY_R):
            self.is_title = True

    # タイトルを描画する
    def draw_title(self):
        pyxel.cls(0)
        x = (WIDTH/2) - (len(GAME_TITLE)*4/2)
        y = HEIGHT/2 - 5
        for i in range(1, -1, -1):
            color = 10 if i == 0 else 8
            pyxel.text(x, y + i, GAME_TITLE, color)
        press = "- Press Enter Key -"
        x = (WIDTH/2) - (len(press)*4/2)
        pyxel.text(x, y+20, press, 3)

    # アプリを描画する
    def draw(self):
        # タイトル画面の時はタイトルを描画する
        if self.is_title:
            self.draw_title()
        else: # ゲーム画面を描画する
            self.draw_maze()
            self.draw_player()
            self.draw_goal()

App()
