import random
import time
import turtle

DELAY = 0.1
SCORE = 0
HIGH_SCORE = 0

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("blue4")
screen.setup(width=600, height=600)
screen.tracer(0)  # chat g helps with tracers

deathmessagechoice = random.randint(1, 3)
applemessagechoice = random.randint(1,3)

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write("Score: {}  High Score: {}".format(SCORE, HIGH_SCORE),
          align="center",
          font=("Courier", 10, "normal"))

# Border walls
border = turtle.Turtle()
border.shape("square")
border.color("black")
border.shapesize(stretch_wid=29, stretch_len=29)
border.penup()
border.goto(0, 0)

#messages
messages = ["Got another apple!", "You won't make it past 10!", "Thats a new high score!"]
deathmessages = ["l bozo", "Better luck next time!", "get gud"]
# Snake
snake = [turtle.Turtle()]
for segment in snake:
  segment.shape("square")
  segment.color("green")
  segment.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-13, 13) * 20, random.randint(-13, 13) * 20)


# Functions
def go_up():
  if snake[0].heading() != 270:
    snake[0].setheading(90)


def go_down():
  if snake[0].heading() != 90:
    snake[0].setheading(270)


def go_left():
  if snake[0].heading() != 0:
    snake[0].setheading(180)


def go_right():
  if snake[0].heading() != 180:
    snake[0].setheading(0)


def move():
  for i in range(len(snake) - 1, 0, -1):
    x = snake[i - 1].xcor()
    y = snake[i - 1].ycor()
    snake[i].goto(x, y)
  snake[0].forward(20)  #chat g helped with the movement range


def check_collision():
  if (snake[0].distance(food) < 20):
    food.goto(random.randint(-13, 13) * 20, random.randint(-13, 13) * 20)
    new_segment = turtle.Turtle()
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    snake.append(new_segment)
    global SCORE, HIGH_SCORE
    SCORE += 1
    if SCORE > HIGH_SCORE:
      HIGH_SCORE = SCORE
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(SCORE, HIGH_SCORE),
              align="center",
              font=("Courier", 10, "normal"))
    if applemessagechoice == 1:
      print(messages[0])
    if applemessagechoice == 2:
      print(messages[1])
    if applemessagechoice == 3:
      print(messages[2])

   # replit ai helped make if statment better
  if (snake[0].xcor() > 290 or snake[0].xcor() < -290 or snake[0].ycor() > 290
      or snake[0].ycor() < -290):
    return True

  return any(segment.distance(snake[0]) < 20 for segment in snake[1:])


# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Main game loop
while True:
  screen.update()
  move()
  if check_collision():
    time.sleep(1)
    snake[0].goto(0, 0)
    for segment in snake:
      segment.goto(1000, 1000)  #chat g helped with segment
    if deathmessagechoice == 1:
      print(deathmessages[0])
    if deathmessagechoice == 2:
      print(deathmessages[1])
    if deathmessagechoice == 3:
      print(deathmessages[2])
    snake.clear()
    new_head = turtle.Turtle()
    new_head.shape("square")
    new_head.color("green")
    new_head.penup()
    snake.append(new_head)
    SCORE = 0
    print(deathmessages[0])
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(SCORE, HIGH_SCORE),
              align="center",
              font=("Courier", 10, "normal"))
    time.sleep(DELAY)
  time.sleep(DELAY)