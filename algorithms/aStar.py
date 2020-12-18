showBoard = True

def displayFinal(searchType, iters, nodesAddedtoOpen, nodesAddedtoClose, cost):
    print(f'{searchType} Stats:')
    print(f'Iterations:\t{iters}\n# of Nodes Added to Open List:\t{nodesAddedtoOpen}')
    print(f'# of Nodes Added to Closed List:\t{nodesAddedtoClose}\nTotal Cost:\t{cost}')

def displayState(boardId, parentId, cost, hVal, priority=None, board=None):
    fN = hVal + cost
    print(f'<id={boardId}\t\tparent={parentId}\t\tg(n)=\t{cost}\th(n)={hVal}\tf(n)={fN}\tPriority={priority}>')
    if showBoard:
        print(str(board))

class priorityQueue():
    def __init__(self, startValues=None):

        self.queue = {}

        if startValues:
            for priority,val in startValues:
                self.insert(priority, val)

    def insert(self, priority, value):
        if priority in self.queue.keys():
            self.queue[priority].insert(0, value)
        else:
            self.queue[priority] = [value]
    
    def pop(self):

        nextKey = min(self.queue.keys())
        value = self.queue[nextKey].pop()

        # deletes key if its empty
        if len(self.queue[nextKey]) == 0:
            del self.queue[nextKey]
        
        return nextKey, value

def aStarSearch(startState, endState, hueristicFunc, maxIterations, hFunction="h"):
    
    i = 0
    cost = 0
    openList = priorityQueue(startValues=[(0, startState)])
    nAddOpen = 1
    closedList = {}
    nAddClosed = 0
    expandedNode = startState

    while hueristicFunc(expandedNode) > 0:
        i+=1
        if i >= maxIterations:
            print('Maximum number of iterations reached')
            break
        
        # Expand Node
        _, expandedNode = openList.pop()
        currentCost = expandedNode.boardCost
        hVal = hueristicFunc(expandedNode)
        
        # Checks if board reaches goal state
        if hVal == 0:
            print('\n\nGoal Reached!!!\n\n')
            cost = currentCost
            
        else:
            # Find Childrens
            nextMove = expandedNode.possibleMoves()
            for tileVal, board, _ in nextMove:
                
                # Skip over states already visited
                if board.getHash() in closedList.keys():
                    continue
                newH = hueristicFunc(board)

                #If statements determine the cost of moving the tile based on number
                if  17 > tileVal > 6:
                    board.boardCost = currentCost + 3
                    openList.insert(board.boardCost + newH, board)

                
                elif tileVal > 16:
                    board.boardCost = currentCost + 15
                    openList.insert(board.boardCost + newH, board)

                else:
                    board.boardCost = currentCost + 1
                    openList.insert(board.boardCost + newH, board)

                nAddOpen += 1
            
            closedList[startState.getHash()] = startState
            nAddClosed += 1

        displayState(expandedNode.boardId, expandedNode.parentId, currentCost, hVal, currentCost, expandedNode)

    displayFinal(f'A* using {hFunction}', i, nAddOpen, nAddClosed, cost)

