import pygame
class grid:
    def __init__(self, height, width, border, size):
        self.size:int = size
        self.height:int = height
        self.width:int = width
        self.border:int = border
        self.content = [
            [[0 for i in range(self.width)] for k in range(self.height)]
        ]
        self.colors = ["Red", "Green", "Blue", "Yellow"]

    def change_state(self, x:int, y:int, state):
        if state < len(self.colors) + 2:
            self.content[0][y][x] = state

    def render_changes(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if not self.content[0][y][x] == 0:
                    pygame.draw.rect(screen, self.colors[self.content[0][y][x] - 1],(x * self.size + self.border, y * self.size + self.border, self.size - self.border * 2, self.size - self.border * 2))

    def render_grid(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (120, 120, 120),((x*self.size, y*self.size),(self.size, self.size)), self.border)

    def auto_screen(self):
        return pygame.display.set_mode((self.width * self.size, self.height * self.size))

    def move(self, x: int, y: int, offset: tuple[int, int]):
        dx, dy = offset
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            value = self.content[0][y][x]
            if value != 0:
                self.content[0][new_y][new_x] = value
                self.content[0][y][x] = 0

    def show_colors(self):
        print("Available colors: ")
        x = 1
        for color in self.colors:
            print(color, ": ", x)
            x+= 1