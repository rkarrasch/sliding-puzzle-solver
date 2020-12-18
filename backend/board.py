import random
import string

# Debug Variable
UseStrIds = False

ROWS = 6
COLS = 3
SIZE = ROWS * COLS

def toCartesianCoords(index):
    return index % COLS, index // COLS

def fromCartesianCoords(coords):
    x,y = coords
    return y * COLS + x

class Board():
    def __init__(self, boardState, boardId='root', parentId=None):
        self.state, emptyTileIndex = _calculateState(boardState)
        self.emptyTile = toCartesianCoords(emptyTileIndex)
        self.parentId = parentId
        
        if boardId == 'root' and not UseStrIds:
            self.boardId=0
        else:
            self.boardId = boardId
        self.boardCost = 0
        
    
    def getHash(self):
        return str(self.state)

    #Returns hueristic result
    def calculateMoves(self, hueristic):
        return hueristic(self.state)
    
    
    #Returns possible moves on the board in the format (tileMoved, newState, (moveX, moveY))
    #tileMoved is the number of the move coordinate
    #newState is the board of the result
    #(moveX,moveY) are the tile coordinates of the tile that moved on the current board
    def possibleMoves(self):
        
        
        # Move left, right, down, up
        tileX, tileY = self.emptyTile
        moves = [
            (tileX + 1, tileY),
            (tileX - 1, tileY),
            (tileX, tileY + 1),
            (tileX, tileY - 1)
        ]

        #Makes sure the move is valid
        validMoves = [(x, y) for x,y in moves if x >= 0 and x < ROWS and y >= 0 and y < COLS]

        finalResult = []
        
        # Represents tileMove as (tileMoved, newState, move)
        for move in validMoves:
        
            tileMoved = self.state[fromCartesianCoords(move)]
            newState = self.state.copy()

            # swaps states
            newState[fromCartesianCoords(self.emptyTile)] = tileMoved
            newState[fromCartesianCoords(move)] = None

            #Creates the new board
            newBoard = Board(newState, _generateBoardId(self.boardId), self.boardId)

            finalResult.append((tileMoved, newBoard, move))
        
        return finalResult

    def __str__(self):
        result = f'Board Id:\t{self.boardId}\n'
        
        # Prints board as grid
        for i in range(len(self.state)):

            if (i % COLS) == 0:
                if i > 0:
                    result += '\n'
                result += str(self.state[i])
            
            else:
                result += '\t'
                result += str(self.state[i])

        return result

def _generateBoardId(parentId):
    #unique identifiers
    if UseStrIds:
        choices = string.ascii_lowercase +'0123456789'
        return parentId + '-' + random.choice(choices)
    
    return parentId * 100 + random.randint(0,99)

#Function that returns the state of the board
#Can be passed the state as a list or as a string i.e. [1 2 3 4 . . . 17]
#the list/string given must be equal to the board size
def _calculateState(boardState):
    
    if type(boardState) == str:
        
        if boardState[0] != '[' or boardState [-1] != ']':
            raise ValueError('Format invalid. Expected square brackets at the start and end of each state')
        values = [int(v) for v in boardState[1:-1].split(" ") if v != '']

        if len(values) != SIZE:
            raise ValueError(f'Format Invalid, the board expected {SIZE} tiles. It recieved {len(values)}.\n The values parsed were {values}')
        
        if values.index(0) < 0:
            raise ValueError('No empty tile found')
        
        indexEmpty = values.index(0)
        values[indexEmpty] = None
        return values, indexEmpty

    elif type(boardState) == list:
        # Assumes it has already been parsed
        indexEmpty = boardState.index(None)

        if len(boardState) != 18:
            raise ValueError(f'Format incorrect, the board expects {SIZE} tiles. Its recieved {len(boardState)}.\n The values parsed were {boardState}')

        if indexEmpty < 0:
            raise ValueError('No empty tile found')
        
        return boardState, indexEmpty
    
    else:
        raise ValueError('Invalid type for Board State. It must be either a list or a string')
