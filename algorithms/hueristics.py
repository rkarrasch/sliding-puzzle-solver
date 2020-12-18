from backend.board import toCartesianCoords

#First hueristic function for the homework, implementing it now as a way to know when the goal has been reached for breadth first search
def createHueristic1Func(goalBoard):

    goalState = goalBoard.state
    
    #Returns tiles that are out of place
    def h(board):
        state = board.state
        tilesOutOfPlace = 0
        for i in range(len(goalState)):
            if state[i] != goalState[i]:
                tilesOutOfPlace += 1
        return tilesOutOfPlace
        
    return h

#Hueristic for homework part 3
def createHueristic2Func(goalBoard):

    goalState = goalBoard.state
    
    def h(board):
        
        moveSum = 0
        currentState = board.state
        
        for i in range(len(currentState)):
            
            tileCoords = toCartesianCoords(i)
            tileVal = currentState[i]

            goalCoords = toCartesianCoords(goalState.index(tileVal))
            
            x = abs(tileCoords[0] - goalCoords[0])
            y = abs(tileCoords[1] - goalCoords[1])
            
            moveSum += (x + y)
        
        return moveSum
    
    return h