import turtle
import random
import time

# ----------------------------
# ПОЛЕ
# ----------------------------
WIDTH, HEIGHT = 600, 400

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Red Riding Hood Mission")

# герой
hero = turtle.Turtle()
hero.shape("circle")
hero.color("red")
hero.penup()

# старт и цель
start = (-250, 0)
goal = (250, 0)

hero.goto(start)

# препятствия
obstacles = []

# скорость (студенты будут менять)
vx = 2
vy = 2

# режим
going_forward = True

# ----------------------------
# ФУНКЦИИ
# ----------------------------

def spawn_obstacle():
    x = random.randint(-280, 280)
    y = random.randint(-180, 180)
    obstacles.append((x, y))

def draw_obstacles():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.penup()
    for ox, oy in obstacles:
        drawer.goto(ox, oy)
        drawer.dot(15, "green")

def check_collision():
    for ox, oy in obstacles:
        if abs(hero.xcor() - ox) < 10 and abs(hero.ycor() - oy) < 10:
            return True
    return False

# ----------------------------
# УПРАВЛЕНИЕ
# ----------------------------

def up():
    hero.sety(hero.ycor() + vy)

def down():
    hero.sety(hero.ycor() - vy)

def left():
    hero.setx(hero.xcor() - vx)

def right():
    hero.setx(hero.xcor() + vx)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# ----------------------------
# ОСНОВНОЙ ЦИКЛ
# ----------------------------

start_time = time.time()

while True:

    # фаза 2: на обратном пути начинается хаос
    if not going_forward:
        if random.random() < 0.05 + (vx + vy)/20:
            spawn_obstacle()

    # проверка достижения цели
    if going_forward and abs(hero.xcor() - goal[0]) < 10:
        print("Reached B! RETURN!")
        going_forward = False

    # проверка возвращения
    if not going_forward and abs(hero.xcor() - start[0]) < 10:
        total_time = time.time() - start_time
        print("MISSION COMPLETE!", total_time)
        break

    # столкновение
    if check_collision():
        print("GAME OVER")
        break

    draw_obstacles()
    time.sleep(0.02)

turtle.done()

