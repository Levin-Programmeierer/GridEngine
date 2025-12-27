import engine
import pygame
grid = engine.grid(20, 20, 1, 30)
screen = grid.auto_screen()
pygame.display.set_caption("Engine Showcase")
clock = pygame.time.Clock()
grid.show_colors()

grid.change_state(3, 3, 2)
grid.change_state(3, 4, 4)
grid.change_state(3, 5, 1)
grid.change_state(3, 6, 3)

class yellow():
    def __init__(self):
        self.x = 3
        self.y = 4
        self.color = 4

yellow = yellow()

while True:
    clock.tick(20)
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        grid.move(yellow.x, yellow.y, (1, 0))
        if yellow.x < grid.width - 1:
            yellow.x += 1
    if keys[pygame.K_a]:
        grid.move(yellow.x, yellow.y, (-1, 0))
        if yellow.x > 0:
            yellow.x -= 1
    if keys[pygame.K_w]:
        grid.move(yellow.x, yellow.y, (0, -1))
        if yellow.y > 0:
            yellow.y -= 1
    if keys[pygame.K_s]:
        grid.move(yellow.x, yellow.y, (0, 1))
        if yellow.y < grid.height - 1:
            yellow.y += 1
    grid.render_grid(screen)
    grid.render_changes(screen)
    pygame.display.update()