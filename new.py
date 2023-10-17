import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 800
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WHITE = (255, 165, 0)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2-Player Vertical Pong Game")

# Initialize paddles and ball
player1_paddle = pygame.Rect(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WIDTH - 20, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Score variables
player1_score = 0
player2_score = 0
max_score = 5  # Adjust as needed for your win condition

# Font for displaying scores
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.move_ip(0, PADDLE_SPEED)
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.move_ip(0, PADDLE_SPEED)

    # Update the ball
    ball.move_ip(BALL_SPEED_X, BALL_SPEED_Y)

    # Ball bouncing
    if ball.top < 0 or ball.bottom > HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        BALL_SPEED_X = -BALL_SPEED_X

    if ball.left < 0:
        # Player 2 scores a point
        player2_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)

    if ball.right > WIDTH:
        # Player 1 scores a point
        player1_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)

    # Check for win
    if player1_score >= max_score or player2_score >= max_score:
        if player1_score > player2_score:
            winner_text = font.render("Player 1 Wins!", True, WHITE)
        else:
            winner_text = font.render("Player 2 Wins!", True, WHITE)
        screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_text = font.render(f"Player 1: {player1_score} | Player 2: {player2_score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    # Delay to control game speed
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
