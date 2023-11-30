import pygame
import math
import random


pygame.init()


class Ant:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.angle = random.uniform(0, 2 * math.pi)
        self.food = True if random.uniform(0, 2) > 1 else False
        self.yellow_flag = False
        self.blue_flag = False
        self.yellow_ang = random.uniform(0, 2 * math.pi)
        self.blue_ang = random.uniform(0, 2 * math.pi)
        self.yellow_dis_counter = 100
        self.blue_dis_counter = 100

    def step(self):

        self.yellow_dis_counter += 0.1
        self.blue_dis_counter += 0.1

        #self.angle += random.uniform(-0.001, 0.001)

        if self.X < 10:
            self.X = 10
            self.angle += math.pi
        elif self.X > width - 10:
            self.X = width - 10
            self.angle += math.pi
        if self.Y < 10:
            self.Y = 10
            self.angle += math.pi
        elif self.Y > height - 10:
            self.Y = height - 10
            self.angle += math.pi

        self.X += math.sin(self.angle)
        self.Y += math.cos(self.angle)

        cl = screen.get_at((int(self.X), int(self.Y)))

        if cl == (255, 255, 0):
            self.food = True
            self.yellow_dis_counter = 0
            self.yellow_flag = True
            self.angle = self.blue_ang

        if cl == (0, 255, 255):
            self.food = False
            self.blue_dis_counter = 0
            self.blue_flag = True
            self.angle = self.yellow_ang

        if self.yellow_flag:
            self.yellow_cry()
            self.yellow_flag = False
            if not self.food:
                self.angle = self.yellow_ang

        if self.blue_flag:
            self.blue_cry()
            self.blue_flag = False
            if self.food:
                self.angle = self.blue_ang

    def render(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.X), int(self.Y)), 2)

    def set_yellow_ang(self, x, y, d):
        an = math.acos((y - self.Y) / d)
        self.yellow_ang = an if x > self.X else 2 * math.pi - an

    def set_blue_ang(self, x, y, d):
        an = math.acos((y - self.Y) / d)
        self.blue_ang = an if x > self.X else 2 * math.pi - an

    def yellow_cry(self):
        for i in range(count):
            if ants[i].yellow_dis_counter > self.yellow_dis_counter:
                x, y = ants[i].X, ants[i].Y
                d = math.dist((self.X, self.Y), (x, y))
                if d <= dst:
                    ants[i].set_yellow_ang(self.X, self.Y, d)
                    ants[i].yellow_flag = True
                    ants[i].yellow_dis_counter = self.yellow_dis_counter
                    pygame.draw.line(screen, (255, 255, 153), (self.X, self.Y), (x, y), 1)

    def blue_cry(self):
        for i in range(count):
            if ants[i].blue_dis_counter > self.blue_dis_counter:
                x, y = ants[i].X, ants[i].Y
                d = math.dist((self.X, self.Y), (x, y))
                if d <= dst:
                    ants[i].set_blue_ang(self.X, self.Y, d)
                    ants[i].blue_flag = True
                    ants[i].blue_dis_counter = self.blue_dis_counter
                    pygame.draw.line(screen, (153, 187, 255), (self.X, self.Y), (x, y), 1)


count = 700
dst = 30
ants = [Ant(random.uniform(50, 950), random.uniform(50, 550)) for _ in range(count)]
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ants')
showAnt = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            showAnt *= -1
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (200, 200), 25)
    pygame.draw.circle(screen, (0, 255, 255), (width - 200, height - 100), 25)
    for ant in ants:
        ant.step()
    if showAnt == 1:
        for ant in ants:
            ant.render()
    pygame.display.flip()
