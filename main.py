from pygame import*

window = display.set_mode((700,500))
back = (102, 59, 203)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_p] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

player_l = Player('racket.png', 20, 200, 50, 100, 5)
player_r = Player('racket.png', 600, 200, 50, 100, 5)

ball = GameSprite('ball.png', 200, 200, 40, 40, 5)

game = True
finish = False

speed_x = 3
speed_y = 3

font.init()
font1 = font.SysFont('Arial', 40)
lose1 = font1.render('левый лох', True, (225, 225, 225))
lose2 = font1.render('правый лох', True, (225, 225, 225))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        player_l.reset()
        player_r.reset()
        ball.reset()
       
        player_l.update_l()
        player_r.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1

        if ball.rect.y > 440 or ball.rect.y < 5:
            speed_y *= -1
        
        if ball.rect.x < 5:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > 640:
            finish = True
            window.blit(lose2, (200,200))

    display.update()
    time.delay(40)