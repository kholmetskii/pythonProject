import pygame
import math
import random

pygame.init()

# Функция для создания муравья с начальными параметрами
def create_ant(X, Y):
    return {
        'X': X,
        'Y': Y,
        'angle': random.uniform(0, 2 * math.pi),
        'food': 1 if random.uniform(0, 10) > 5 else 0,
        'flagF': 0,
        'flagH': 0,
        'angF': random.uniform(0, 2 * math.pi),
        'angH': random.uniform(0, 2 * math.pi),
        'disF': 100,
        'disH': 100
    }

# Функция для выполнения шага муравья
def step(ant):
    ant['disF'] += 0.1
    ant['disH'] += 0.1

    #ant['angle'] += random.uniform(-0.05, 0.05)

    if ant['X'] < 10 or ant['X'] > width - 10 or ant['Y'] < 10 or ant['Y'] > height - 10:
        ant['angle'] += math.pi

    ant['X'] += math.sin(ant['angle'])
    ant['Y'] += math.cos(ant['angle'])

    cl = screen.get_at((int(ant['X']), int(ant['Y'])))

    # Проверка цвета в текущей позиции для обработки еды
    if cl == (255, 255, 0):  # Yellow
        ant['food'] = 1
        ant['disF'] = 0
        ant['flagF'] = 1
        ant['angle'] = ant['angH']

    if cl == (0, 255, 255):  # Cyan
        ant['food'] = 0
        ant['flagH'] = 1
        ant['disH'] = 0
        ant['angle'] = ant['angF']

    # Обработка событий CryF и CryH
    if ant['flagF'] > 0:
        cry_F(ant)
        ant['flagF'] = 0
        if ant['food'] == 0:
            ant['angle'] = ant['angF']

    if ant['flagH'] > 0:
        cry_H(ant)
        ant['flagH'] = 0
        if ant['food'] == 1:
            ant['angle'] = ant['angH']

# Функция для отрисовки муравья
def render(ant):
    pygame.draw.circle(screen, (255, 255, 255), (int(ant['X']), int(ant['Y'])), 2)

# Функция для установки угла для CryF
def set_angle_F(ant, x, y, d):
    an = math.acos((y - ant['Y']) / d)
    ant['angF'] = an if x > ant['X'] else 2 * math.pi - an

# Функция для установки угла для CryH
def set_angle_H(ant, x, y, d):
    an = math.acos((y - ant['Y']) / d)
    ant['angH'] = an if x > ant['X'] else 2 * math.pi - an

# Функция для выполнения CryF
def cry_F(ant):
    for i in range(count):
        if ants[i]['disF'] > ant['disF']:
            xz, yz = ants[i]['X'], ants[i]['Y']
            d = math.dist((ant['X'], ant['Y']), (xz, yz))
            if d <= dst:
                set_angle_F(ants[i], ant['X'], ant['Y'], d)
                ants[i]['flagF'] = 1
                ants[i]['disF'] = ant['disF']
                pygame.draw.line(screen, (255, 255, 153), (ant['X'], ant['Y']), (xz, yz), 1)

# Функция для выполнения CryH
def cry_H(ant):
    for i in range(count):
        if ants[i]['disH'] > ant['disH']:
            xz, yz = ants[i]['X'], ants[i]['Y']
            d = math.dist((ant['X'], ant['Y']), (xz, yz))
            if d <= dst:
                set_angle_H(ants[i], ant['X'], ant['Y'], d)
                ants[i]['flagH'] = 1
                ants[i]['disH'] = ant['disH']
                pygame.draw.line(screen, (153, 187, 255), (ant['X'], ant['Y']), (xz, yz), 1)

# Инициализация параметров
count = 800
dst = 35
ants = [create_ant(random.uniform(50, 1300), random.uniform(50, 600)) for _ in range(count)]
width, height = 1400, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Antbots")

showAnt = 1

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            showAnt *= -1

    # Очистка экрана
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (300, 300), 25)
    pygame.draw.circle(screen, (0, 255, 255), (width - 300, height - 300), 25)

    # Выполнение шага для каждого муравья
    for ant in ants:
        step(ant)

    # Отрисовка муравьев, если флаг установлен в 1
    if showAnt == 1:
        for ant in ants:
            render(ant)
    # Обновление экрана
    pygame.display.flip()

