import pygame, random 

S_WIDTH = 720
S_HEIGHT = 1080
#gameboard is 20x10 (col by rows)
G_WIDTH = 400
G_HEIGHT = 800
P_SIZE = 40

# Class representing tetris pieces
class Piece():

    I = [
        [[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]     
    ]

    O = [
        [[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    ]

    T = [
        [[0,0,1,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    ]

    S = [
        [[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    ]

    Z = [
        [[0,0,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0]]
    ]

    J = [
        [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,1,0,0,0],[0,1,1,1],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]
    ]

    L = [
        [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,1,1,1,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    ]

    # List of shapes in type string
    SHAPES = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']

    #dictionary key of shapes with color values for index 0 and shape values for index 1
    SHAPES_INFO = {
        'I': [(0, 255, 0), I],
        'O': [(255, 0, 0), O], 
        'T': [(0, 255, 255), T], 
        'S': [(255, 255, 0), S], 
        'Z': [(255, 165, 0), Z],
        'J': [(0, 0, 255), J], 
        'L': [(128, 0, 128), L]
    }

    def __init__(self, shape, color, size, rotation):
        if not shape:
            self.shape = random.choice(Piece.SHAPES)
        else:
            self.shape = shape
        self.color = Piece.SHAPES_INFO[self.shape][0]
        self.size = size
        self.rotation = 0

    def rotate(self, direction='clockwise'):
        if direction == 'clockwise':
            self.rotation = (self.rotation % 4) + 1
        else:
            self.rotation = (self.rotaiton % 4) - 1

class Gameboard():

    # contents are the pieces currently inside the gameboard
    def __init__(self, gamescreen):
        self.gamescreen = gamescreen
        self.width = width
        self.height = height
        self.content = content



# if __name__ == '__main__':
#     x = Piece(None, None, 0)
#     y = Gameboard(G_WIDTH, G_HEIGHT, [])
#     print(x.color)
#     print(y.width)
    

    