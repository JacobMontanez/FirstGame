import pygame

#important pygame stuff
pygame.init()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption('My First Game')
clock = pygame.time.Clock()
#background
bg = pygame.image.load('Space.jpg')


#classes
class player(object):
    def __init__(self, color, x, y, w, h, hpC):
        self.x = x
        self.color = color
        self.y = y
        self.w = w
        self.h = h
        self.vel = 5
        self.Left = False
        self.Right = False
        self.hp = 100
        self.visible = True
        self.hpC = hpC
        self.vel = 10
    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, (75, 75, 75), (self.hpC - 3, 17, 200 + 6, 26))
        pygame.draw.rect(screen, (255, 0, 0), (self.hpC, 20, 200, 20))
        if self.visible:
            pygame.draw.rect(screen, (0, 255, 0), (self.hpC, 20, 200 - ((100 - self.hp) * 2), 20))
            
    
    def hit(self):
        if self.hp > 0:
            self.hp -=5
        else:
            self.visible = False

class projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 18 * facing
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


print("UP = W/Up arrow")
print("Down = S/Down arrow")
print("Left = A/Left arrow")
print("Right = D/Right arrow")
print("Shoot = Space/L")
name1 = str(input())
name2 = str(input())

#important functions
def draw():
    screen.blit(bg, (0,0))
    player1.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    
    text = font.render(name1, 1, (255,255,255))
    text2 = font.render(name2, 1, (255,255,255))
    if player1.visible:
        screen.blit(text, (player1.x +2,player1.y - 15))
    if player2.visible:
        screen.blit(text2, (player2.x +2,player2.y - 15))
    screen.blit(text, (250, 25))
    screen.blit(text2, (500, 25))
    
    won()
    
    for bullet in bullets:
        if player2.visible:
            bullet.draw(screen)
    for bullet in bullets2:
        if player1.visible:
            bullet.draw(screen)
    clock.tick(60)
    pygame.display.update()

def won():
    if not player2.visible:
        screen.blit(wintexta, (300, 200))
    if not player1.visible:
        screen.blit(wintextb, (300, 200))

    
font = pygame.font.SysFont('comicsnas', 20, True)
win = pygame.font.SysFont('comicsans', 60, True)
running = True
bullets = []
bullets2 = []
player1 = player((0,0,255), 100, 225, 50, 20, 20)
player2 = player((255,0,0), 700, 225, 50, 20, 580)
firerate = 0
firerate2 = 0


#mainloop start
while running:
    if firerate > 0:
        firerate += 1
    if firerate > 12:
        firerate = 0

    if firerate2 > 0:
        firerate2 += 1
    if firerate2 > 12:
        firerate2 = 0
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for bullet in bullets:
        if player1.visible:
            if bullet.y - bullet.radius < player2.y + player2.h and bullet.y + bullet.radius > player2.y:
                if bullet.x + bullet.radius > player2.x and bullet.x - bullet.radius < player2.w + player2.x:
                    player2.hit()
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 900 and bullet.x > -10:
                bullet.x += bullet.vel

    for bullet in bullets2:
        if player2.visible:
            if bullet.y - bullet.radius < player1.y + player1.h and bullet.y + bullet.radius > player1.y:
                if bullet.x + bullet.radius > player1.x and bullet.x - bullet.radius < player1.w + player1.x:
                    player1.hit()
                    bullets2.pop(bullets2.index(bullet))
            if bullet.x < 900 and bullet.x > -10:
                bullet.x += bullet.vel
            
    keys = pygame.key.get_pressed()
                         
    if keys[pygame.K_SPACE] and firerate == 0:
        if player1.Left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 1000:
            bullets.append(projectile(round(player1.x + player1.w//2), round(player1.y + player1.h//2), 6, (255,255,0), facing))
        firerate = 1
                
    
    if keys[pygame.K_l] and firerate2 == 0:
        if player2.Left == False and player2.Right == False:
            facing = -1
        elif player2.Left:
            facing = -1
        else:
            facing = 1
        if len(bullets2) < 1000:
            bullets2.append(projectile(round(player2.x + player2.w//2), round(player2.y + player2.h//2), 6, (255,255,0), facing))
            firerate2 = 1
                
    if keys[pygame.K_w] and player1.y > 5:
        player1.y -= player1.vel
    if keys[pygame.K_s] and player1.y < 430:
        player1.y += player1.vel
    if keys[pygame.K_a] and player1.x > 5:
        player1.x -= player1.vel
        player1.Left = True
        player1.Right = False
    elif keys[pygame.K_d]and player1.x < 760:
        player1.x += player1.vel
        player1.Left = False
        player1.Right = True


    if keys[pygame.K_UP] and player2.y > 5:
        player2.y -= player2.vel
    if keys[pygame.K_DOWN] and player2.y < 430:
        player2.y += player2.vel
    if keys[pygame.K_LEFT] and player2.x > 5:
        player2.x -= player2.vel
        player2.Left = True
        player2.Right = False
    elif keys[pygame.K_RIGHT] and player2.x < 760:
        player2.x += player2.vel
        player2.Left = False
        player2.Right = True
    
    draw()
#mainloop end
    
pygame.quit()
quit()
