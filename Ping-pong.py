from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.recy.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.recy.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


back = (200,255,255)
win_width = 600
win_height = 800
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket_1 = Player('racket.png', 30, 200, 150, 50, 5)
racket_r = Player('racket.png', 520, 200, 150, 50, 5)
ball = GameSprite('Tennis_ball.png', 200, 200, 50, 50, 5)

font_label = font.Font(None, 40)
lose_1 = font_label.render("PLAYER ONE LOSE!",True,(255,50,50))
lose_2 = font_lbel.render("PLAYER TWO LOSE!",True,(50,50,225))

speed_x = 3
speed_y = 3
