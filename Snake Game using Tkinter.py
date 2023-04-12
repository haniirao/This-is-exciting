"""
import tkinter as tk
import random

# Set up the game window
window = tk.Tk()
window.title("Snake Game")
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Set up the game board
board_size = 20
board = canvas.create_rectangle(0, 0, 400, 400, fill="white")
snake = [(board_size*10, board_size*10)]
direction = "Right"
food = None

# Draw the initial snake
def draw_snake():
    canvas.delete("snake")
    for segment in snake:
        x, y = segment
        canvas.create_rectangle(x, y, x+board_size, y+board_size, fill="green", tags="snake")

# Move the snake
def move():
    global direction, food
    x, y = snake[0]
    if direction == "Right":
        x += board_size
    elif direction == "Left":
        x -= board_size
    elif direction == "Up":
        y -= board_size
    elif direction == "Down":
        y += board_size
    # Check for collision with the walls
    if x >= 400 or x < 0 or y >= 400 or y < 0:
        game_over()
        return
    # Check for collision with the food
    if food and (x, y) == food:
        snake.append(snake[-1])
        food = None
        draw_food()
    # Check for collision with itself
    if (x, y) in snake[1:]:
        game_over()
        return
    # Move the snake
    snake.insert(0, (x, y))
    snake.pop()
    draw_snake()
    window.after(100, move)

# Draw the food
def draw_food():
    global food
    if not food:
        x = random.randint(0, 19) * board_size
        y = random.randint(0, 19) * board_size
        food = (x, y)
        canvas.create_oval(x, y, x+board_size, y+board_size, fill="red", tags="food")

# Game over
def game_over():
    canvas.create_text(200, 200, text="Game Over", font=("Arial", 20))
    window.unbind("<Key>")
    window.after_cancel(move_id)

# Handle keyboard input
def handle_key(event):
    global direction
    if event.keysym == "Right" and direction != "Left":
        direction = "Right"
    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"
    elif event.keysym == "Up" and direction != "Down":
        direction = "Up"
    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"

# Start the game
window.bind("<Key>", handle_key)
draw_snake()
draw_food()
move_id = window.after(100, move)
window.mainloop()
"""
################################################################################################################

# Program in Python to create a Snake Game

from tkinter import *
import random

# Initialising Dimensions of Game
WIDTH = 500
HEIGHT = 500
SPEED = 200
SPACE_SIZE = 20
BODY_SIZE = 2
SNAKE = "#00FF00"
FOOD = "#FFFFFF"
BACKGROUND = "#000000"

# Class to design the snake
class Snake:

	def __init__(self):
		self.body_size = BODY_SIZE
		self.coordinates = []
		self.squares = []

		for i in range(0, BODY_SIZE):
			self.coordinates.append([0, 0])

		for x, y in self.coordinates:
			square = canvas.create_rectangle(
				x, y, x + SPACE_SIZE, y + SPACE_SIZE,
					fill=SNAKE, tag="snake")
			self.squares.append(square)

# Class to design the food
class Food:

	def __init__(self):

		x = random.randint(0,
				(WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
		y = random.randint(0,
				(HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

		self.coordinates = [x, y]

		canvas.create_oval(x, y, x + SPACE_SIZE, y +
						SPACE_SIZE, fill=FOOD, tag="food")

# Function to check the next move of snake
def next_turn(snake, food):

	x, y = snake.coordinates[0]

	if direction == "up":
		y -= SPACE_SIZE
	elif direction == "down":
		y += SPACE_SIZE
	elif direction == "left":
		x -= SPACE_SIZE
	elif direction == "right":
		x += SPACE_SIZE

	snake.coordinates.insert(0, (x, y))

	square = canvas.create_rectangle(
		x, y, x + SPACE_SIZE,
				y + SPACE_SIZE, fill=SNAKE)

	snake.squares.insert(0, square)

	if x == food.coordinates[0] and y == food.coordinates[1]:

		global score

		score += 1

		label.config(text="Points:{}".format(score))

		canvas.delete("food")

		food = Food()

	else:

		del snake.coordinates[-1]

		canvas.delete(snake.squares[-1])

		del snake.squares[-1]

	if check_collisions(snake):
		game_over()

	else:
		window.after(SPEED, next_turn, snake, food)

# Function to control direction of snake
def change_direction(new_direction):

	global direction

	if new_direction == 'left':
		if direction != 'right':
			direction = new_direction
	elif new_direction == 'right':
		if direction != 'left':
			direction = new_direction
	elif new_direction == 'up':
		if direction != 'down':
			direction = new_direction
	elif new_direction == 'down':
		if direction != 'up':
			direction = new_direction

# function to check snake's collision and position
def check_collisions(snake):

	x, y = snake.coordinates[0]

	if x < 0 or x >= WIDTH:
		return True
	elif y < 0 or y >= HEIGHT:
		return True

	for body_part in snake.coordinates[1:]:
		if x == body_part[0] and y == body_part[1]:
			return True

	return False

# Function to control everything
def game_over():

	canvas.delete(ALL)
	canvas.create_text(canvas.winfo_width()/2,
					canvas.winfo_height()/2,
					font=('consolas', 70),
					text="GAME OVER", fill="red",
					tag="gameover")

# Giving title to the gaming window


window = Tk()
window.title("GFG Snake game ")


score = 0
direction = 'down'

# Display of Points Scored in Game

label = Label(window, text="Points:{}".format(score),
			font=('consolas', 20))
label.pack()

canvas = Canvas(window, bg=BACKGROUND,
				height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',
			lambda event: change_direction('left'))
window.bind('<Right>',
			lambda event: change_direction('right'))
window.bind('<Up>',
			lambda event: change_direction('up'))
window.bind('<Down>',
			lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
























