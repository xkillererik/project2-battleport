import pygame
pygame.init()

class Menu:
    def __init__(self):
        self.X = game.Width / 3
        self.Y = 20
        self.Buttoncolor = (150,150,150)
        self.Buttoncolor2 = (220,220,220)
        self.Textcolor = (30,30,30)
        self.Fontsize = 40

        self.Buttons = [\
        (self.X, self.Y, "Start", "game"),\
        (self.X, self.Y + self.Fontsize*1.5, "Instructions", "instructions"),\
        (self.X, self.Y + self.Fontsize*3, "Players", "playerlist"),\
        (self.X, self.Y + self.Fontsize*4.5, "Exit", "exit")]

    def draw(self):
        for button in self.Buttons:
            if pygame.mouse.get_pos()[0] > button[0]\
            and pygame.mouse.get_pos()[0] < button[0] * 2\
            and pygame.mouse.get_pos()[1] > button[1]\
            and pygame.mouse.get_pos()[1] < button[1] + self.Fontsize:
                if pygame.mouse.get_pressed()[0]:
                    game.Level = button[3]
                pygame.draw.rect(game.Display, self.Buttoncolor2, (button[0], button[1], button[0], self.Fontsize))
            else:
                pygame.draw.rect(game.Display, self.Buttoncolor, (button[0], button[1], button[0], self.Fontsize))
            text(button[2], self.Textcolor, self.Fontsize, button[0], button[1])

class Menubar:
    def __init__(self):
        self.Width = game.Width
        self.Height = game.Height * 0.03
        self.Barcolor = (50,50,50)
        self.Buttoncolor = (60,60,60)
        self.Buttoncolor2 = (100,100,100)
        self.Fontsize = int(self.Height)

        self.Buttons = [\
        (game.Width - 40, 0, 40, self.Height, "menu", game.Width, self.Height)]

    def draw(self):
        pygame.draw.rect(game.Display, self.Barcolor, (0, 0, self.Width, self.Height))

        for button in self.Buttons:
            if pygame.mouse.get_pos()[0] > button[0]\
            and pygame.mouse.get_pos()[0] < button[5]\
            and pygame.mouse.get_pos()[1] > button[1]\
            and pygame.mouse.get_pos()[1] < button[6]:
                if pygame.mouse.get_pressed()[0]:
                    game.Level = button[4]
                pygame.draw.rect(game.Display, self.Buttoncolor2, (button[0], button[1], button[2], button[3]))
            else:
                pygame.draw.rect(game.Display, self.Buttoncolor, (button[0], button[1], button[2], button[3]))
            text("Menu", (255,255,255), self.Fontsize, button[0] + button[2]/8, self.Height/4)
        
class Button:
    def __init__(self, x, y, x2, y2, color, colorhover, f):
        self.X = x
        self.Y = y
        self.X2 = x2
        self.Y2 = y2
        self.Color = color
        self.Color_hover = colorhover
        self.Click_function = f

    def Hover(self):
        if pygame.mouse.get_pos()[0] > self.X\
        and pygame.mouse.get_pos()[0] < self.X2\
        and pygame.mouse.get_pos()[1] > self.Y\
        and pygame.mouse.get_pos()[1] < self.Y2:
            return True
        else:
            return False

    def Click(self): return pygame.mouse.get_pressed()[0]
    def Clicked(self): self.Click_function()
        

    def Draw(self):
        if self.Hover():
            if self.Click(): self.Clicked()
            else: pygame.draw.rect(game.Display, self.Color_hover, (self.X, self.Y, self.X2 - self.X, self.Y2 - self.Y))
        else:
            pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.X2 - self.X, self.Y2 - self.Y))

class Game:
    def __init__(self):
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.Exit = False

        self.Width = 800
        self.Height = 600
        self.Display = pygame.display.set_mode((self.Width, self.Height))
        
        self.Level = "menu"

    def draw(self): self.Display.fill((0,0,0))
    def tick(self): self.clock.tick(self.FPS)
    def loop(self):
        while not self.Exit:
            if self.Level == "menu":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.Exit = True
                    self.draw()
                    menu.draw()
                    pygame.display.update()
                    self.tick()

            elif self.Level == "game":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.Exit = True
                    self.draw()
                    menubar.draw()
                    testbutton.Draw()
                    pygame.display.update()
                    self.tick()

            else: self.Exit = True

def text(text,textcolor,size,x,y):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, textcolor)
    game.Display.blit(screen_text, [x,y])

def test(): testbutton.Color = (100,100,100)

game = Game()
menu = Menu()
testbutton = Button(100, 100, 150, 150, (0,0,100), (100,0,0), test)
menubar = Menubar()

game.loop()

pygame.quit()
quit()