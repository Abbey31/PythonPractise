import cowsay
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Not numeric try again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range (2-10). Try again!')

def race(colors):
    cowsay = create_cows(colors)

    while True:
        for racer in cowsay:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[cowsay.index(racer)]
            


def create_cows(colors):
    cows = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = cows.cowsay()
        racer.color(color)
        racer.shape('cow')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH// 2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        cowsay.append(racer)

    return cowsay

def init_cows():
    screen = cowsay.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Cow Racing!')
            
racers = get_number_of_racers()
init_cows()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)


