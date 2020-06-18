import pygame, random 

pygame.init()

S_WIDTH = 720
S_HEIGHT = 900
#gameboard is 20x10 (col by rows)
G_WIDTH = 400
G_HEIGHT = 800
P_SIZE = 30

coord_x = 30
coord_y = 60

# Each variable represents a tetris piece with the 1 represent 'blocks to be drawn'
I = [
    ['11110','00000', '00000','00000','00000']
    # [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]     
]
O = [
    ['11000','11000','00000','00000','00000']
]
T = [
    ['01000','11100','00000','00000','00000']
    # [[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
    # [[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0]],
    # [[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
]
S = [
    ['00000','11000','01100','00000','00000']
    # [[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
]
Z = [
    ['11000','01100','00000','00000','00000']
    # [[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0]]
]
J = [
    ['10000','11100','00000','00000','00000']
    # [[0,0,0,0,0],[0,1,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]],
    # [[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]],
    # [[0,0,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]
]
L = [
    ['10000','11100','00000','00000','00000']
    # [[0,0,0,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]],
    # [[0,0,0,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,0,0]],
    # [[0,0,0,0,0],[0,1,1,1,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
]
# Class representing tetris pieces
class Piece():
    # List of shapes in type string
    SHAPES = [I, O, T, S, Z, J, L]

    #dictionary key of shapes with color values for index 0 and shape values for index 1
    SHAPES_INFO = [
        (0, 255, 0),
        (255, 0, 0), 
        (0, 255, 255), 
        (255, 255, 0), 
        (255, 165, 0),
        (0, 0, 255), 
        (128, 0, 128)
    ]

    def __init__(self, shape=None):
        # if there is no current shape in play, choose a random one to be in a play
        if not shape:
            self.shape = random.choice(Piece.SHAPES)
        else:
            self.shape = shape
        self.color = Piece.SHAPES_INFO[Piece.SHAPES.index(self.shape)]
        self.rotation = 0
        self.coord_x = 120
        self.coord_y = 0

    # rotate piece by dividing amount of rotation by 4 because you can only rotate 4 ways then add or subtract by 1 depending on direction
    def rotate(self, direction='clockwise'):
        if direction == 'clockwise':
            self.rotation = (self.rotation % 4) + 1
        else:
            self.rotation = (self.rotation % 4) - 1

#class representing within the tetris game
class Gameboard():
    # grid are the pieces currently inside the gameboard
    def __init__(self,gamescreen):
        self.gamescreen = gamescreen
        self.width = 10
        self.height = 22
        self.grid = []
        self.piece = Piece()
        
        [self.grid.append([0] * self.width) for _ in range(self.height)]

    # create a block piece in the game and get its starting coordinates at the first row and third column 
    def draw_piece(self):
        self.shape = self.piece.shape
        self.color = self.piece.color
        self.coord_x = self.piece.coord_x
        self.coord_y = self.piece.coord_y
        for row in range(len(self.shape[0])):
            for col in range(len(self.shape[0][row])):
                if self.shape[0][row][col] == '1':
                    pygame.draw.rect(self.gamescreen, 
                                    self.color, 
                                    (self.coord_x + (col* P_SIZE), self.coord_y + (row * P_SIZE), P_SIZE, P_SIZE))       

    #draw board and its screen
    def draw_board(self):
        for row in range(2, len(self.grid)):
            for col in range(len(self.grid[row])):
                pygame.draw.rect(self.gamescreen, 
                                (255,255,255), 
                                (coord_x + (col* P_SIZE), coord_y + (row * P_SIZE), P_SIZE, P_SIZE),
                                1)

    def move_piece(self):
        self.coord_x += 40
        self.coord_y += 40
        self.piece.color = (0,0,0)
        

class Tetris():

    def __init__(self):
        self.window = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.gameboard = Gameboard(self.window)

    def run(self):
        pygame.display.set_caption('Tetris Clone')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:         
                    running = False
                    pygame.display.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_DOWN:
                        self.gameboard.move_piece()

            self.window.fill((0,0,0))
            self.gameboard.draw_board()
            self.gameboard.draw_piece()
            pygame.display.update()

    
if __name__ == '__main__':
    Tetris().run()
    z = Piece()
    print(z.coord_x)
    

    