import pyxel

GAME_TITLE = "Flappy Rocket"  # ゲームタイトル

class FlappyRocket:
    def __init__(self):
        # Pyxelを初期化する
        pyxel.init(160, 120, title=GAME_TITLE)

        # リソースファイルを読み込む
        pyxel.load("flappy_rocket.pyxres")

        # ゲームをリセットする
        self.is_title = True
        self.reset_game()

        # アプリの実行を開始する
        pyxel.run(self.update, self.draw)

    # ゲームをリセットする
    def reset_game(self):
        # 得点を初期化する
        self.score = 0

        # 出現タイマーを初期化する
        self.timer = 0

        # 宇宙船を初期化する
        self.ship_x = (pyxel.width - 8) / 2  # X座標
        self.ship_y = pyxel.height / 4  # Y座標
        self.ship_vx = 0  # X方向の速度
        self.ship_vy = 0  # Y方向の速度
        self.ship_dir = 1  # 宇宙船の左右の向き(-1:左,1:右)
        self.is_jetting = False  # ジェット噴射中かどうか
        self.is_exploding = False  # 爆発中かどうか

        # マップの配置を初期化する
        self.survivors = []  # 宇宙飛行士の配置
        self.meteors = []  # 隕石の配置

    # アプリを更新する
    def update(self):
        # タイトル画面の時はRETURNキー(ENTERキー)の入力を待つ
        if self.is_title:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.is_title = False
                self.reset_game()

    # 空を描画する
    def draw_sky(self):
        num_grads = 4  # グラデーションの数
        grad_height = 6  # グラデーションの高さ
        grad_start_y = 0  # 描画開始位置

        pyxel.cls(0)
        for i in range(num_grads):
            pyxel.dither((num_grads-i) / num_grads)  # ディザリングを有効にする
            pyxel.rect(
                0,
                grad_start_y + i * grad_height,
                pyxel.width,
                grad_height,
                1,
            )
        pyxel.dither(1)  # ディザリングを無効にする

    # 宇宙船を描画する
    def draw_ship(self):
        pyxel.blt(
            self.ship_x,  # 描画位置のX座標
            self.ship_y,  # 描画位置のY座標
            0,  # 参照するイメージバンク番号
            0,  # 参照イメージの左上のX座標
            0,  # 参照イメージの左上のY座標
            8,  # 参照イメージの幅
            8,  # 参照イメージの高さ
            0,  # 色番号0を透明色として扱う
        )

    # スコアを描画する
    def draw_score(self):
        score = f"SCORE:{self.score}"
        for i in range(1, -1, -1):
            color = 7 if i == 0 else 0
            pyxel.text(3 + i, 3, score, color)

    # タイトルを描画する
    def draw_title(self):
        for i in range(1, -1, -1):
            color = 10 if i == 0 else 8
            pyxel.text(57, 50 + i, GAME_TITLE, color)
        pyxel.text(42, 70, "- Press Enter Key -", 3)

    # アプリを描画する
    def draw(self):
        # 画面を描画する
        self.draw_sky()
        self.draw_ship()
        self.draw_score()

        # タイトル画面の時はタイトルを描画する
        if self.is_title:
            self.draw_title()


FlappyRocket()
