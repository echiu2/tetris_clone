import pygame, random 

pygame.init()

S_WIDTH = 540
S_HEIGHT = 720
#gameboard is 20x10 (col by rows)
G_WIDTH = 300
G_HEIGHT = 600
P_SIZE = 30

top_left_x = 4
top_left_y = 2

# Each variable represents a tetris piece with the 1 represent 'blocks to be drawn'
S = [['.....',
      '..11.',
      '.11..',
      '.....',
      '.....',],
     ['..1..',
      '..11.',
      '...1.',
      '.....'
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['.....',
      '..1..',
      '..1..',
      '..1..',
      '..1..'],
     ['.....',
      '.....',
      '1111.',
      '.....',
      '.....']]

O = [['.....',
      '.11..',
      '.11..',
      '.....',
      '.....']]

J = [['.....',
      '.1...',
      '.111.',
      '.....',
      '.....'],
     ['.....',
      '..11.',
      '..1..',
      '..1..',
      '.....'],
     ['.....',
      '.....',
      '.111.',
      '...1.',
      '.....'],
     ['.....',
      '..1..',
      '..1..',
      '.11..',
      '.....']]

L = [['.....',
      '...1.',
      '.111.',
      '.....',
      '.....'],
     ['.....',
      '..1..',
      '..1..',
      '..11.',
      '.....'],
     ['.....',
      '.....',
      '.111.',
      '.1...',
      '.....'],
     ['.....',
      '.11..',
      '..1..',
      '..1..',
      '.....']]

T = [['.....',
      '..1..',
      '.111.',
      '.....',
      '.....'],
     ['.....',
      '..1..',
      '..11.',
      '..1..',
      '.....'],
     ['.....',
      '.....',
      '.111.',
      '..1..',
      '.....'],
     ['.....',
      '..1..',
      '.11..',
      '..1..',
      '.....']]
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

    # rotate piece by dividing amount of rotation by 4 because you can only rotate 4 ways then add or subtract by 1 depending on direction
    def rotate(self, direction='clockwise'):
        if direction == 'clockwise':
            self.rotation = (self.rotation + 1) % len(self.shape)
        else:
            self.rotation = (self.rotation - 1) % len(self.shape)

#class representing within the tetris game
class Gameboard():
    # grid are the pieces currently inside the gameboard
    def __init__(self, gamescreen):
        self.gamescreen = gamescreen
        self.width = 10
        self.height = 22
        self.grid = []
        [self.grid.append([0] * self.width) for _ in range(self.height)]
        self.create_piece()

    def create_piece(self):
        self.piece = Piece()
        self.piece_x, self.piece_y = 6, 1

    # Checking if block piece will not exit out the gamescreen or game zone
    def check_collision(self, dx, dy):
        p = self.piece.rotation
        for y, row in enumerate(self.piece.shape[p]):
            border_y = y + dy
            print(border_y)
            for x, block_val in enumerate(row):
                if block_val == '1':
                    border_x = x + dx
                    if border_x < top_left_x:
                        return False
                    elif border_x > self.width + (top_left_x - 1):
                        return False
                    elif border_y > self.height -1 :
                        return False
                    elif self.grid[y][x]:
                        return False                    
        return True

    def move_piece(self, dx, dy):
        new_dx = self.piece_x + dx
        new_dy = self.piece_y + dy
        if self.check_collision(new_dx, new_dy):
            self.piece_x = new_dx
            self.piece_y = new_dy

    def rotate_piece(self):
        self.piece.rotate("clockwise")
        check = self.check_collision(self.piece_x, self.piece_y)
        if check:
            pass 

    def lock_piece(self):
        p = self.piece.rotation
        # if not self.check_collision(self.piece_x, self.piece_y):
        for y, row in enumerate(self.piece.shape[p]):
            for x, col in enumerate(row):
                if col == '1':
                    self.grid[y+self.piece_y][x+self.piece_x] = 1
        
        print(self.grid)
        self.create_piece()

    #draw grid; parameter piece is the tetris piece, pos_x is starting x and pox_y is starting y
    def draw_grid(self):
        # for y, row in enumerate(self.grid):
        #     for x, col in enumerate(row):
        #         if col == '1':
        #             pygame.draw_rect(self.gamescreen,
        #                             (128,128,128),
        #                             (top_left_x * P_SIZE + (col* P_SIZE), top_left_y * P_SIZE + (row * P_SIZE), P_SIZE, P_SIZE),
        #                             1)
        #         else:
        #             pygame.draw.rect(self.gamescreen, 
        #                             (255,0,0), 
        #                             (top_left_x * P_SIZE, top_left_y * P_SIZE, G_WIDTH, G_HEIGHT),
        #                             1)
        #         pygame.draw.rect(self.gamescreen, 
        #                 (255,0,0), 
        #                 (top_left_x * P_SIZE, top_left_y * P_SIZE, G_WIDTH, G_HEIGHT),
        #                 1)
        for row in range(len(self.grid)-2):
            for col in range(len(self.grid[row])):
                pygame.draw.rect(self.gamescreen, 
                                (255,255,255), 
                                (top_left_x * P_SIZE + (col* P_SIZE), top_left_y * P_SIZE + (row * P_SIZE), P_SIZE, P_SIZE),
                                1)

        pygame.draw.rect(self.gamescreen, 
                        (255,0,0), 
                        (top_left_x * P_SIZE, top_left_y * P_SIZE, G_WIDTH, G_HEIGHT),
                        1)

    # def get_pos(self):

    def draw_piece(self, piece, pos_x, pos_y):
        p = piece.rotation
        for row in range(len(piece.shape[p])):
            for col in range(len(piece.shape[p][row])):
                if piece.shape[p][row][col] == '1':
                    pygame.draw.rect(self.gamescreen, 
                                    piece.color, 
                                    (pos_x * P_SIZE + (col* P_SIZE), pos_y * P_SIZE + (row * P_SIZE), P_SIZE, P_SIZE))


    def draw_board(self):
        self.draw_piece(self.piece, self.piece_x, self.piece_y)
        self.draw_grid()
    
    def gameover(self):
        if sum(self.grid[0]) > 0 or sum(self.grid[1]) > 0:
            print("hi")
   
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
            self.window.blit(label, (top_left_x * P_SIZE + G_WIDTH / 2 - (label.get_width() / 2), 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:         
                    running = False
                    pygame.display.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.gameboard.rotate_piece()
                    if event.key ==pygame.K_DOWN:
                        self.gameboard.move_piece(dx=0, dy=1)
                    if event.key ==pygame.K_LEFT:
                        self.gameboard.move_piece(dx=-1, dy=0)
                    if event.key ==pygame.K_RIGHT:
                        self.gameboard.move_piece(dx=1, dy=0)
                    if event.key ==pygame.K_SPACE:
                        self.gameboard.lock_piece()                      

            self.gameboard.draw_board()
            pygame.display.update()

    
if __name__ == '__main__':
    Tetris().start()

    