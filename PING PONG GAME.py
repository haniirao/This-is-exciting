
###PING PONG GAME

import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game window
pygame.display.set_caption("Pong")

# Set up the game clock
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the paddles
paddle_width = 10
paddle_height = 80
paddle_speed = 6
left_paddle = pygame.Rect(50, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Define the ball
ball_width = 20
ball_speed = 4
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_width // 2
ball_direction_x = random.choice([-1, 1])
ball_direction_y = random.choice([-1, 1])
ball = pygame.Rect(ball_x, ball_y, ball_width, ball_width)

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.y > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.y < screen_height - paddle_height:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.y > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.y < screen_height - paddle_height:
        right_paddle.y += paddle_speed
    
    # Move the ball
    ball.x += ball_direction_x * ball_speed
    ball.y += ball_direction_y * ball_speed
    
    # Check for collisions with the paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_direction_x *= -1
        ball_speed += 1
    
    # Check for collisions with the top and bottom walls
    if ball.y < 0 or ball.y > screen_height - ball_width:
        ball_direction_y *= -1
    
    # Check for a score
    if ball.x < 0:
        print("Right player scores!")
        ball.x = ball_x
        ball.y = ball_y
        ball_speed = 5
        ball_direction_x = 1
        ball_direction_y = 1
    if ball.x > screen_width:
        print("Left player scores!")
        ball.x = ball_x
        ball.y = ball_y
        ball_speed = 5
        ball_direction_x = -1
        ball_direction_y = -1
    
    # Fill the screen with white
    screen.fill(white)
    
    # Draw the paddles
    pygame.draw.rect(screen, black, left_paddle)
    pygame.draw.rect(screen, black, right_paddle)
    
    # Draw the ball
    pygame.draw.ellipse(screen, black, ball)

    # Update the screen
    pygame.display.update()
    
    # Set the game clock
    clock.tick(60)

# Quit Pygame
pygame.quit()





