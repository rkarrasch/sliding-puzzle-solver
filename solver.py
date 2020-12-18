import sys
import backend
import algorithms

maxIterations = 10000

def parseInput():
    
    startState = None
    endState = None

    startState = input('Starting state: ')
    endState = input('End state: ')

    startBoard = backend.Board(startState)
    endBoard = backend.Board(endState, boardId=-1)
    
    return startBoard, endBoard

def main():

    startState, goalState = parseInput()
    
    h = algorithms.createHueristic1Func(goalState)
    h2 = algorithms.createHueristic2Func(goalState)
    
    print( '\n\nBreadth First Search:\n\n' )
    algorithms.breadthFirstSearch(startState,goalState, h, maxIterations)

    print('\n\nA Star with Hueristic 1:\n\n')
    algorithms.aStarSearch(startState, goalState, h, maxIterations, 'h')

    print('\n\nA Star with Hueristic 2:\n\n')
    algorithms.aStarSearch(startState, goalState, h2, maxIterations, 'h2')

main()