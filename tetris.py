import pygame, random 
from random import randint

pygame.init()

S_WIDTH = 540
S_HEIGHT = 660
#gameboard is 20x10 (col by rows)
G_WIDTH = 300
G_HEIGHT = 600
P_SIZE = 30

top_left_x = 0
top_left_y = 2

# Each variable represents a tetris piece with the 1 represent 'blocks to be drawn'
S = [['.....',
      '..11.',
      '.11..',
      '.....',],
     ['.....',
      '..1..',
      '..11.',
      '...1.',
      '.....']]

Z = [['.....',
      '.....',
      '.11..',
      '..11.',
      '.....'],
     ['.....',
      '..1..',
      '.11..',
      '.1...',
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
        self.rotation = randint(0, len(self.shape)-1)

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
        self.next_piece()
        self.create_piece(self.next_p)
        self.hold()


    def next_piece(self):
        self.next_p = Piece()
        self.next_next = Piece()
        # self.piece_x, self.piece_y = 2,1 

    # Create a new piece: will be called everytime a piece gets locked
    def create_piece(self, piece):
        self.piece = piece
        # self.piece = Piece()
        self.piece_x, self.piece_y = 2, 1

    # Piece can no longer be move and therefore is now embedded into the grid
    def lock_piece(self):
        p = self.piece.rotation
        # if not self.check_collision(self.piece_x, self.piece_y):
        for y, row in enumerate(self.piece.shape[p]):
            for x, col in enumerate(row):
                if col == '1':
                    self.grid[y+self.piece_y][x+self.piece_x] = 1

        self.create_piece(self.next_next)
        self.next_piece()

    # Checking if block piece will not exit out the gamescreen or game zone (2, 3 represents left and right wall)
    def check_collision(self, dx, dy):
        p = self.piece.rotation
        for y, row in enumerate(self.piece.shape[p]):
            self.border_y = y + dy
            for x, block_val in enumerate(row):
                if block_val == '1':
                    self.border_x = x + dx
                    if self.border_x < 0:
                        return False
                    elif self.border_x > self.width-1: 
                        return False
                    elif self.border_y > self.height -1 :
                        return False
                    elif self.grid[self.border_y][self.border_x]:
                        return False                    
        return True

    # Check if the piece can move anymore in the x or y direction
    def valid_move(self, dx, dy):
        new_dx = self.piece_x + dx
        new_dy = self.piece_y + dy
        if self.check_collision(new_dx, new_dy):
            return True
        return False

    # Move the tetris piece
    def move_piece(self, dx, dy):
        if self.valid_move(dx, dy):
            self.piece_x += dx
            self.piece_y += dy
    
    # Make tetris piece fall a row after every interval; will have to check if move is valid or not: if not then lock the piece
    def falling_piece(self):
        if self.valid_move(dx=0, dy=1):
            self.move_piece(dx=0, dy=1)
        else:
            self.lock_piece()
            self.delete_lines()

    def hard_drop(self):
        while self.valid_move(dx=0, dy=1):
            self.move_piece(dx=0, dy=1)
        self.falling_piece()

    # delete lines by creating a list comprehension through the grid, if a row is all 1s then we will go through that row
    # and reverse it to get the row before it to make it drop
    def delete_lines(self):
        remove_row = [y for y, row in enumerate(self.grid) if all(row)]
        for y in remove_row:
            for _y in reversed(range(1, y+1)):
                self.grid[_y] = self.grid[_y-1]
        
    # Check if you can rotate piece through the the collisoin cases, if you can't then rotate counterclockwise
    def rotate_piece(self):
        self.piece.rotate("clockwise")
        check = self.check_collision(self.piece_x, self.piece_y)
        if check:
            pass 
        if not check:
            if self.border_x < 0:
                if self.valid_move(dx=1, dy=0):
                    self.move_piece(dx=1, dy=0)
                elif self.valid_move(dx=2, dy=0):
                    self.move_piece(dx=2, dy=0)
                else:
                    self.piece.rotate("counterclockwise")
            elif self.border_x > self.width-1:
                if self.valid_move(dx=-1, dy=0):
                    self.move_piece(dx=-1, dy=0)
                elif self.valid_move(dx=-2, dy=0):
                    self.move_piece(dx=-2, dy=0)
                else:
                    self.piece.rotate("counterclockwise")
            else:
                self.piece.rotate("counterclockwise")   

    # Used to check if player is holding a piece or not, if true then we will hold the piece and change the next and current piece
    def hold(self, check_hold=False):
        self.hold_piece = self.piece
        self.is_hold = check_hold

        self.create_piece(self.next_next)
        self.next_piece()    

        return self.is_hold
            
        
    #draw grid; parameter piece is the tetris piece, pos_x is starting x and pox_y is starting y
    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if col == 1:
                    pygame.draw.rect(self.gamescreen,
                                    self.piece.color,
                                    ((x * P_SIZE), (y * P_SIZE), P_SIZE, P_SIZE))

        for row in range(len(self.grid)-2):
            for col in range(len(self.grid[row])):
                pygame.draw.rect(self.gamescreen, 
                                (255,255,255), 
                                (top_left_x  * P_SIZE+ (col* P_SIZE), top_left_y  * P_SIZE+ (row * P_SIZE), P_SIZE, P_SIZE),
                                1)

        pygame.draw.rect(self.gamescreen, 
                        (255,0,0), 
                        (top_left_x * P_SIZE, top_left_y * P_SIZE, G_WIDTH, G_HEIGHT),
                        1)

    def draw_next(self, piece):
        p = piece.rotation
        for row in range(len(piece.shape[p])):
            for col in range(len(piece.shape[p][row])):
                if piece.shape[p][row][col] == '1':
                    pygame.draw.rect(self.gamescreen, 
                                    piece.color, 
                                    (((self.width + 340)) + col * P_SIZE, (row * P_SIZE) + 80, P_SIZE, P_SIZE))        


    def draw_piece(self, piece, pos_x, pos_y):
        p = piece.rotation
        for row in range(len(piece.shape[p])):
            for col in range(len(piece.shape[p][row])):
                if piece.shape[p][row][col] == '1':
                    pygame.draw.rect(self.gamescreen, 
                                    piece.color, 
                                    (pos_x * P_SIZE + (col* P_SIZE), pos_y * P_SIZE + (row * P_SIZE), P_SIZE, P_SIZE))

    def draw_hold_piece(self, piece):
        p = piece.rotation
        for row in range(len(piece.shape[p])):
            for col in range(len(piece.shape[p][row])):
                if piece.shape[p][row][col] == '1':
                    pygame.draw.rect(self.gamescreen, 
                                    piece.color, 
                                    (((self.width + 340)) + col * P_SIZE, (row * P_SIZE) + 240, P_SIZE, P_SIZE))         


    def draw_board(self):
        self.draw_next(self.next_next)
        self.draw_piece(self.piece, self.piece_x, self.piece_y)
        self.draw_grid()

    # if player is holding, then draw holding piece
    def draw_hold(self):
        if self.is_hold:
            self.draw_hold_piece(self.hold_piece)
    
    def gameover(self):
        return sum(self.grid[0]) > 0 or sum(self.grid[1]) > 0 or sum(self.grid[2]) > 0

   
class Tetris():
    DROP_EVENT = pygame.USEREVENT

    def __init__(self):
        self.window = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.gameboard = Gameboard(self.window)

    def main_menu(self):
        run = True
        while run:
            self.window.fill((0,0,0))
            font = pygame.font.SysFont('comicsans', 60)
            label = font.render('Press any button to start', 1, (255,255,255))
            self.window.blit(label, ((top_left_x + 4) * P_SIZE + G_WIDTH / 2 - (label.get_width() / 2), 300))            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.start()
        pygame.quit()

    def start(self):
        pygame.display.set_caption('Tetris Clone')
        running = True
        time = 750
        pygame.time.set_timer(Tetris.DROP_EVENT, time)

        while running:
            if self.gameboard.gameover():
                print("gameover")
                pygame.display.quit()
                quit()

            self.window.fill((0,0,0))
            font = pygame.font.SysFont('comicsans', 60)
            label = font.render('TETRIS', 1, (255,255,255))
            self.window.blit(label, (top_left_x * P_SIZE + G_WIDTH / 2 - (label.get_width() / 2), 10))

            font = pygame.font.SysFont('comicsans', 40)
            label = font.render('NEXT PIECE', 1, (255,255,255))
            self.window.blit(label, ((top_left_x + 9) * P_SIZE + G_WIDTH / 2 - (label.get_width() / 2), 80))

            font = pygame.font.SysFont('comicsans', 40)
            label = font.render('HOLD', 1, (255,255,255))
            self.window.blit(label, ((top_left_x + 9) * P_SIZE + G_WIDTH / 2 - (label.get_width() / 2), 240))

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
                        self.gameboard.hard_drop()
                    if event.key ==pygame.K_h:
                        self.gameboard.hold(check_hold=True)
                if event.type == Tetris.DROP_EVENT:
                    self.gameboard.falling_piece()                   

            self.gameboard.draw_board()
            self.gameboard.draw_hold()
            pygame.display.update()

    
if __name__ == '__main__':
    Tetris().main_menu()

    