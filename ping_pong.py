from pygame import *

#классы
class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed):
    super().__init__()
    self.image = transform.scale(image.load(player_image), (65, 65))
    self.speed = player_speed
    self.rect  = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y
  def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_s] and self.rect.y < H - 100:
      self.rect.y += self.speed

  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_DOWN] and self.rect.y < H - 100:
      self.rect.y += self.speed

#окно игры
W = 700
H = 500
window = display.set_mode((W, H))
display.set_caption("Пинг понг")
back = (146, 153, 222)
window.fill(back)

#игровой таймер
clock = time.Clock()
FPS = 60

#спрайты
raket1 = Player('racket.png', 10, H // 2, 25, 100, 10)
raket2 = Player('racket.png', W - 35, H // 2, 25, 100, 10)
ball = GameSprite('ball.png', W//2, H//2, 50, 50, 0)

#текст
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose1 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

#игровой цикл
game = True
finish = False
while game:
    for e in event.get():
      if e.type == QUIT:
        game = False

      if finish != True:
        window.fill(BACKGROUND)

      if ball.rect.y > H-50 or ball.rect.y < 0:
        speed_y *= -1

      if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        if ball.rect.centery < racket1.rect.left or ball.rect.centery > racket1.rect.left:
          speed_y *= -1
        if ball.rect.centery < racket2.rect.left or ball.rect.centery > racket2.rect.left:
          speed_y *= -1

    display.update()
    clock.tick(FPS)


