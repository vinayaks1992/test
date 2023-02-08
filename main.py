import pygame
import random

# Initialize pygame
pygame.init()

# Set screen size and title
screen = pygame.display.set_mode((400, 708))
pygame.display.set_caption("Flappy Bird")

# Load the bird image
bird = pygame.image.load("bird.png")

# Define the bird's position and rect
bird_x = 150
bird_y = 350
bird_rect = pygame.Rect(bird_x, bird_y, 34, 24)

# Load the background image
background = pygame.image.load("background.png")

# Load the pipe image
pipe = pygame.image.load("pipe.png")

# Define the pipes' positions and rects
pipe_1_x = 400
pipe_1_y = 0
pipe_1_rect = pygame.Rect(pipe_1_x, pipe_1_y, 52, 320)

pipe_2_x = 400
pipe_2_y = 320 + 140
pipe_2_rect = pygame.Rect(pipe_2_x, pipe_2_y, 52, 320)

# Set the initial velocity of the bird
bird_velocity = 0

# Set the initial gravity
gravity = 1

# Set the gap size between pipes
gap_size = 140

# Set the initial score to 0
score = 0

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the bird's velocity and position
    bird_velocity += gravity
    bird_y += bird_velocity

    # Check for collision with the top or bottom of the screen
    if bird_y < 0 or bird_y + 24 > 708:
        running = False

    # Check for collision with the pipes
    if (bird_rect.colliderect(pipe_1_rect) or
        bird_rect.colliderect(pipe_2_rect)):
        running = False

    # Update the bird rect
    bird_rect.y = bird_y

    # Update the pipes' positions
    pipe_1_x -= 2
    pipe_2_x -= 2

    # Check if the pipes are off the screen
    if pipe_1_x + 52 < 0:
        pipe_1_x = 400
        pipe_1_y = random.randint(0, 368) - 368

    if pipe_2_x + 52 < 0:
        pipe_2_x = 400
        pipe_2_y = random.randint(0, 368) + gap_size

    # Update the pipes' rects
    pipe_1_rect.x = pipe_1_x
    pipe_1_rect.y = pipe_1_y
    pipe_2_rect.x = pipe_2_x
    pipe_2_rect.y = pipe_2_y

    # Check for a point scored
    if pipe_1_x + 52 < bird_x and pipe_1_x + 52 > bird_x - 2:
        score += 1