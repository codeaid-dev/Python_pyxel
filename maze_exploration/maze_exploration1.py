import pyxel

GAME_TITLE = "Maze Exploration"  # ゲームタイトル
WIDTH, HEIGHT = 168, 168

class App:
    def __init__(self):
        # Pyxelを初期化する
        pyxel.init(WIDTH, HEIGHT, title=GAME_TITLE)

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

    # アプリを更新する
    def update(self):
        # タイトル画面の時はRETURNキー(ENTERキー)の入力を待つ
        if self.is_title:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.is_title = False
                self.reset_game()

        if pyxel.btnp(pyxel.KEY_R):
            self.is_title = True

    # 迷路の壁を描画する
    def draw_maze(self):
        pyxel.cls(0)
        for y in range(self.mazeh):
            for x in range(self.mazew):
                if self.maze[y][x] == 1:
                    pyxel.blt(x*8,y*8,0,0,0,8,8,0)

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

App()
