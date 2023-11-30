import pygame
import math
import random

pygame.init()

class Antbot:
    def __init__(self, X, Y, angle, food):
        self.X = X
        self.Y = Y
        self.angle = angle
        self.food = food
        self.flagF = 0
        self.flagH = 0
        self.angF = random.uniform(0, 2 * math.pi)
        self.angH = random.uniform(0, 2 * math.pi)
        self.disF = 100
        self.disH = 100

    def step(self):
        self.disF += 0.1
        self.disH += 0.1

        self.angle += random.uniform(-0.05, 0.05)

        if self.X < 10 or self.X > width - 10 or self.Y < 10 or self.Y > height - 10:
            self.angle += math.pi

        self.X += math.sin(self.angle)
        self.Y += math.cos(self.angle)

        cl = screen.get_at((int(self.X), int(self.Y)))

        if cl == (255, 255, 0):  # Yellow
            self.food = 1
            self.disF = 0
            self.flagF = 1
            self.angle = self.angH

        if cl == (0, 255, 255):  # Cyan
            self.food = 0
            self.flagH = 1
            self.disH = 0
            self.angle = self.angF

        if self.flagF > 0:
            self.CryF()
            self.flagF = 0
            if self.food == 0:
                self.angle = self.angF

        if self.flagH > 0:
            self.CryH()
            self.flagH = 0
            if self.food == 1:
                self.angle = self.angH

    def render(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.X), int(self.Y)), 2)

    def setAngleF(self, x, y, d):
        an = math.acos((y - self.Y) / d)
        self.angF = an if x > self.X else 2 * math.pi - an

    def setAngleH(self, x, y, d):
        an = math.acos((y - self.Y) / d)
        self.angH = an if x > self.X else 2 * math.pi - an

    def CryF(self):
        for i in range(count):
            if ants[i].disF > self.disF:
                xz, yz = ants[i].X, ants[i].Y
                if self.X - dst < xz < self.X + dst and self.Y - dst < yz < self.Y + dst:
                    d = math.dist((self.X, self.Y), (xz, yz))
                    if d <= dst:
                        ants[i].setAngleF(self.X, self.Y, d)
                        ants[i].flagF = 1
                        ants[i].disF = self.disF
                        pygame.draw.line(screen, (255, 255, 153), (self.X, self.Y), (xz, yz), 1)

    def CryH(self):
        for i in range(count):
            if ants[i].disH > self.disH:
                xz, yz = ants[i].X, ants[i].Y
                if self.X - dst < xz < self.X + dst and self.Y - dst < yz < self.Y + dst:
                    d = math.dist((self.X, self.Y), (xz, yz))
                    if d <= dst:
                        ants[i].setAngleH(self.X, self.Y, d)
                        ants[i].flagH = 1
                        ants[i].disH = self.disH
                        pygame.draw.line(screen, (153, 187, 255), (self.X, self.Y), (xz, yz), 1)


count = 500
dst = 30
ants = [Antbot(random.uniform(50, 850), random.uniform(50, 400), random.uniform(0, 2 * math.pi),
               1 if random.uniform(0, 10) > 5 else 0) for _ in range(count)]
print(ants)
width, height = 900, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Antbots")

showAnt = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            showAnt *= -1

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (300, 300), 25)
    pygame.draw.circle(screen, (0, 255, 255), (width - 300, height - 300), 25)
    pygame.draw.circle(screen, (255, 255, 0), (100, 100), 25)

    for ant in ants:
        ant.step()

    if showAnt == 1:
        for ant in ants:
            ant.render()

    pygame.display.flip()
