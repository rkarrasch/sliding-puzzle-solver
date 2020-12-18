showBoard = True

def displayFinal(searchType, iters, nodesAddedtoOpen, nodesAddedtoClose, cost):
    print(f'{searchType} Stats:')
    print(f'Iterations:\t{iters}\n# of Nodes Added to Open List:\t{nodesAddedtoOpen}')
    print(f'# of Nodes Added to Closed List:\t{nodesAddedtoClose}\nTotal Cost:\t{cost}')

def displayState(boardId, parentId, cost, hVal, board=None):
    fN = hVal + cost
    print(f'<id={boardId}\t\tparent={parentId}\t\tg(n)=\t{cost}\th(n)={hVal}\tf(n)={fN}>')
    if showBoard:
        print(str(board))


def breadthFirstSearch(startState, endState, hueristicFunc, maxIterations):
    
    i = 0
    cost = 0
    openList = [(0, startState)] #queue
    nAddOpen = 1
    closedList = {} #hash table
    nAddClosed = 0
    expandedNode = startState
    
    
    while expandedNode.getHash() != endState.getHash():
        
        i+=1
        
        if i >= maxIterations:
            print('Maximum number of iterations reached')
            break

        # Expand Node
        currentCost,expandedNode = openList.pop()
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
                
                #If statements determine the cost of moving the tile based on number
                if  17 > tileVal > 6:
                    openList.insert(0, (currentCost + 3, board))
                
                elif tileVal > 16:
                    openList.insert(0, (currentCost + 15, board))
                
                else:
                    openList.insert(0, (currentCost + 1, board))
                nAddOpen += 1

            closedList[startState.getHash()] = startState
            nAddClosed += 1
        
        displayState(expandedNode.boardId, expandedNode.parentId, currentCost, hVal, expandedNode)
    
    displayFinal('Breadth First Search', i, nAddOpen, nAddClosed, cost)
