import pygame, random 

pygame.init()

S_WIDTH = 540
S_HEIGHT = 720
#gameboard is 20x10 (col by rows)
G_WIDTH = 300
G_HEIGHT = 600
P_SIZE = 30

top_left_x = 120
top_left_y = 60

# Each variable represents a tetris piece with the 1 represent 'blocks to be drawn'
I = [
    ['1111','0000', '0000','0000']
]
O = [
    ['1100','1100','0000','0000']
]
T = [
    ['0100','11100','0000','0000']
]
S = [
    ['1100','0110','0000','0000']
]
Z = [
    ['1100','0110','0000','0000']
]
J = [
    ['1000','1110','0000','0000']
]
L = [
    ['1000','1110','0000','0000']
]
# Class representing tetris pieces
class Piece():
    # List of shapes in type string
    SHAPES = [I, O, T, S, Z, J, L]

    #dictionary key of shapes with color values for index 0 and shape values for index 1
    SHAPES_COLOR = [(0, 255, 0),(255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0),(0, 0, 255), (128, 0, 128)]

    def __init__(self, shape=None):
        # if there is no current shape in play, choose a random one to be in a play
        if not shape:
            self.shape = random.choice(Piece.SHAPES)
        else:
            self.shape = shape
        self.color = Piece.SHAPES_COLOR[Piece.SHAPES.index(self.shape)]
        self.rotation = 0
        #Starting position of tetris piece, 4 from x axis and 4 from y axis (120x120) in block size
        self.x = 4
        self.y = 4

    # rotate piece by dividing amount of rotation by 4 because you can only rotate 4 ways then add or subtract by 1 depending on direction
    def rotate(self, direction='clockwise'):
        if direction == 'clockwise':
            self.rotation = (self.rotation % 4) + 1
        else:
            self.rotation = (self.rotation % 4) - 1

    def get_pos(self):
        print(self.x, self.y)

#class representing within the tetris game
class Gameboard():
    # grid are the pieces currently inside the gameboard
    def __init__(self,gamescreen):
        self.gamescreen = gamescreen
        self.width = 10
        self.height = 22
        self.grid = []
        [self.grid.append([0] * self.width) for _ in range(self.height)]
        self.piece = Piece() 

    #draw board and its screen
    def draw_board(self):
        for row in range(2, len(self.grid)):
            for col in range(len(self.grid[row])):
                # if int(self.grid[row][col]) == 1:
                #     pygame.draw.rect(self.gamescreen, 
                #                 self.piece.color, 
                #                 (self.piece.x * P_SIZE, self.piece.y * P_SIZE, P_SIZE, P_SIZE),
                #                 1)

                pygame.draw.rect(self.gamescreen, 
                                (255,255,255), 
                                (top_left_x + (col* P_SIZE), top_left_y + (row * P_SIZE), P_SIZE, P_SIZE),
                                1)

        pygame.draw.rect(self.gamescreen, 
                        (255,0,0), 
                        (top_left_x, top_left_y + 60, G_WIDTH, G_HEIGHT),
                        1)

    # create a block piece in the game and get its starting coordinates at the first row and third column 
    def draw_piece(self, piece, coord_x, coord_y):
        color = piece.color
        piece_x = coord_x
        piece_y = coord_y
        for row in range(len(piece.shape[0])):
            for col in range(len(piece.shape[0][row])):
                if piece.shape[0][row][col] == '1':
                    x = pygame.draw.rect(self.gamescreen, 
                                    color, 
                                    (piece_x * P_SIZE + (col* P_SIZE) + 90, piece_y * P_SIZE + (row * P_SIZE), P_SIZE, P_SIZE))
        
    # Checking if block piece will not exit out the gamescreen or game zone
    def check_collision(self, dx, dy):
        for y, row in enumerate(self.piece.shape[0]):
            border_y = y + dy
            for x, block_val in enumerate(row):
                if int(block_val) == 1:
                    border_x = x + dx
                    if border_x <= 0:
                        return False
                    elif border_x > self.width:
                        return False
                    elif border_y - 1 > self.height:
                        return False
                    elif self.grid[y][x]:
                        return False
                        
        return True

    # check if you can move tetris piece, if so then move it or if it reaches the end then make a new tetris piece
    def move_piece(self, dx, dy):
        new_dx = self.piece.x + dx
        new_dy = self.piece.y + dy
        if self.check_collision(new_dx, new_dy):
            self.piece.x = new_dx
            self.piece.y = new_dy
            if self.piece.y == self.height:
                print('check')
                for y, row in enumerate(self.piece.shape[0]):
                    for x, block_val in enumerate(row):
                            self.grid[self.piece.y-1][self.piece.x] = block_val

                self.piece = Piece()

    # Draw gameboard and tetris piece
    def draw_blocks(self):
        self.draw_piece(self.piece, self.piece.x, self.piece.y)
        self.draw_board()

          
class Tetris():
    def __init__(self):
        self.window = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.gameboard = Gameboard(self.window)

    def start(self):
        pygame.display.set_caption('Tetris Clone')
        running = True
        while running:
            self.window.fill((0,0,0))
            font = pygame.font.SysFont('comicsans', 60)
            label = font.render('TETRIS', 1, (255,255,255))
            self.window.blit(label, (top_left_x + G_WIDTH / 2 - (label.get_width() / 2), 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:         
                    running = False
                    pygame.display.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_DOWN:
                        self.gameboard.move_piece(dx=0, dy=1)
                    if event.key ==pygame.K_LEFT:
                        self.gameboard.move_piece(dx=-1, dy=0)
                    if event.key ==pygame.K_RIGHT:
                        self.gameboard.move_piece(dx=1, dy=0)

            self.gameboard.draw_blocks()
            pygame.display.update()

    
if __name__ == '__main__':
    Tetris().start()

    