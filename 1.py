import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario Bros 1-1")

# Define colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Mario attributes
mario_width = 40
mario_height = 60
mario_x = 50
mario_y = SCREEN_HEIGHT - mario_height - 20
mario_vel = 5
jumping = False
jump_count = 10

# Game loop
clock = pygame.time.Clock()

def draw_mario():
    pygame.draw.rect(screen, (255, 0, 0), (mario_x, mario_y, mario_width, mario_height))

def draw_level():
    # Draw sky
    screen.fill(BLUE)
    
    # Draw ground
    pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
    
    # Draw some platforms (simple representation)
    pygame.draw.rect(screen, BROWN, (150, SCREEN_HEIGHT - 100, 100, 20))  # platform 1
    pygame.draw.rect(screen, BROWN, (300, SCREEN_HEIGHT - 150, 100, 20))  # platform 2

def main():
    global mario_y, jumping, jump_count
    while True:
        screen.fill(WHITE)
        draw_level()
        draw_mario()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key press handling
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and mario_x > 0:
            mario_x -= mario_vel
        if keys[pygame.K_RIGHT] and mario_x < SCREEN_WIDTH - mario_width:
            mario_x += mario_vel

        # Jumping logic
        if not jumping:
            if keys[pygame.K_SPACE]:
                jumping = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                mario_y -= (jump_count ** 2) * 0.4 * neg
                jump_count -= 1
            else:
                jumping = False
                jump_count = 10

        # Limit frames per second
        clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()
