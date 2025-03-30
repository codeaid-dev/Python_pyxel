import pyxel

GAME_TITLE = "Flappy Rocket"  # ゲームタイトル

SHIP_ACCEL_X = 0.06  # 宇宙船の左右方向の加速度
SHIP_ACCEL_UP = 0.04  # 宇宙船の上方向の加速度
SHIP_ACCEL_DOWN = 0.02  # 宇宙船の下方向の加速度
MAX_SHIP_SPEED = 0.8  # 宇宙船の最大速度

SPRITE_SPAWN_INTERVAL = 150  # スプライトの出現間隔(150フレーム＝5秒)

class Sprite:
    def __init__(self):
        self.dx = -pyxel.rndf(0.1,2.0)

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

        # スプライトの配置を初期化する
        self.items = []  # アイテムの配置
        self.meteors = []  # 隕石の配置

    # スプライトの位置を画面左端の縦方向(Y軸)にランダムな位置にする
    def generate_pos(self, sprite):
        sprite.x = pyxel.width
        sprite.y = pyxel.rndi(0, pyxel.height-8)

    # アイテムを追加する
    def add_item(self):
        sprite = Sprite()
        self.generate_pos(sprite)
        self.items.append(sprite)

    # 隕石を追加する
    def add_meteor(self):
        sprite = Sprite()
        self.generate_pos(sprite)
        self.meteors.append(sprite)

    # 宇宙船を更新する
    def update_ship(self):
        # 宇宙船の速度を更新する
        if pyxel.btn(pyxel.KEY_UP):  # 上矢印キーが押されている時
            self.is_jetting = True
            self.ship_vy = max(self.ship_vy - SHIP_ACCEL_UP, -MAX_SHIP_SPEED)
            pyxel.play(0, 0)  # チャンネル0で効果音0(ジェット音)を再生する
        else:  # スペースキーが押されていない時
            self.is_jetting = False
            self.ship_vy = min(self.ship_vy + SHIP_ACCEL_DOWN, MAX_SHIP_SPEED)

        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_RIGHT): # 左右矢印キーが押されている時
            if pyxel.btn(pyxel.KEY_LEFT):
                self.ship_dir = -1
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.ship_dir = 1
            self.ship_vx = max(
                min(self.ship_vx + self.ship_dir * SHIP_ACCEL_X, 1), -MAX_SHIP_SPEED
            )

        # 宇宙船の位置を更新する
        self.ship_x += self.ship_vx
        self.ship_y += self.ship_vy

        # 画面端に到達したら跳ね返す
        if self.ship_x < 0:  # 画面左端を越えた時
            self.ship_x = 0
            self.ship_vx = abs(self.ship_vx)
            pyxel.play(0, 1)  # チャンネル0で効果音1(跳ね返り音)を再生する

        max_ship_x = pyxel.width - 8
        if self.ship_x > max_ship_x:  # 画面右端を越えた時
            self.ship_x = max_ship_x
            self.ship_vx = -abs(self.ship_vx)
            pyxel.play(0, 1)

        if self.ship_y < 0:  # 画面上端を越えた時
            self.ship_y = 0
            self.ship_vy = abs(self.ship_vy)
            pyxel.play(0, 1)

        max_ship_y = pyxel.height - 8
        if self.ship_y > max_ship_y:  # 画面下端を越えた時
            self.ship_y = max_ship_y
            self.ship_vy = -abs(self.ship_vy)
            pyxel.play(0, 1)

    def update_sprites(self):
        for s in self.items:
            s.x += s.dx
            if s.x < -8:
                s.x = pyxel.width
        for s in self.meteors:
            s.x += s.dx
            if s.x < -8:
                s.x = pyxel.width

    # スプライト(アイテム/隕石)を追加する
    def add_sprites(self):
        # 一定時間ごとにスプライトを追加する
        if self.timer == 0:
            self.add_item()
            self.add_meteor()
            self.timer = SPRITE_SPAWN_INTERVAL
        else:
            self.timer -= 1

    # アプリを更新する
    def update(self):
        # タイトル画面の時はRETURNキー(ENTERキー)の入力を待つ
        if self.is_title:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.is_title = False
                self.reset_game()
            return  # タイトル画面では他の更新処理は行わない

        # ゲームを更新する
        self.update_ship()
        self.add_sprites()
        self.update_sprites()

    # 空を描画する
    def draw_sky(self):
        num_grads = 4  # グラデーションの数
        grad_height = 6  # グラデーションの高さ
        #grad_start_y = pyxel.height - grad_height * num_grads  # 描画開始位置
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
        # ジェット噴射の表示位置をずらす量を計算する
        offset_y = (pyxel.frame_count % 3 + 2) if self.is_jetting else 0

        # 下方向のジェット噴射を描画する
        pyxel.blt(
            self.ship_x, # 描画位置のX座標
            self.ship_y + 3 + offset_y, # 描画位置のY座標
            0, # 参照するイメージバンク番号
            0, # 参照イメージの左上のX座標
            8, # 参照イメージの左上のY座標
            8, # 参照イメージの幅
            8, # 参照イメージの高さ
            0, # 色番号0を透明色として扱う
        )

        # 宇宙船を描画する
        pyxel.blt(self.ship_x, self.ship_y, 0, 0, 0, 8, 8, 0)

    # アイテムを描画する
    def draw_items(self):
        for s in self.items:
            pyxel.blt(s.x, s.y, 0, 8, 0, 8, 8, 0)

    # 隕石を描画する
    def draw_meteors(self):
        for s in self.meteors:
            pyxel.blt(s.x, s.y, 0, 16, 0, 8, 8, 0)

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
        self.draw_items()
        self.draw_meteors()
        self.draw_score()

        # タイトル画面の時はタイトルを描画する
        if self.is_title:
            self.draw_title()


FlappyRocket()
