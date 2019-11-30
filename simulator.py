"""
Author: Ricky Grannis-Vu
"""

import random
import copy
import math

class Simulator:

    def __init__(self, size=4):
        self.size = size
        self.grid = self.createEmptyGrid()
        self.grid = self.generateRandomTile(self.grid)
        self.grid = self.generateRandomTile(self.grid)

    def createEmptyGrid(self):
        grid = []
        for i in range(self.size):
            grid.append([])
            for j in range(self.size):
                grid[i].append(None)
        return grid

    def generateRandomTile(self, grid):
        grid_copy = copy.deepcopy(grid)
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if grid_copy[x][y] == None:
                grid_copy[x][y] = random.choice([2, 4])
                return grid_copy

    def isGameOver(self, grid):
        for i in range(self.size):
            for j in range(self.size):
                if grid[i][j] == None:
                    return False
                if i != 0 and grid[i][j] == grid[i - 1][j]:
                    return False
                if i != self.size - 1 and grid[i][j] == grid[i + 1][j]:
                    return False
                if j != 0 and grid[i][j] == grid[i][j - 1]:
                    return False
                if j != self.size - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
        return True

    def getScore(self, grid):
        score = 0
        for i in range(self.size):
            for j in range(self.size):
                if grid[i][j] == None:
                    continue
                power = math.log(grid[i][j], 2)
                score += (power - 1) * 2**power
        return score

    def getHighestTile(self, grid):
        highestTile = None
        for i in range(self.size):
            for j in range(self.size):
                if highestTile == None or grid[i][j] > highestTile:
                    highestTile = grid[i][j]
        return highestTile

    def slide(self, grid_copy, action):
        if action == "w":
            isModified, grid_copy = self.slideUp(grid_copy)
        elif action == "s":
            isModified, grid_copy = self.slideDown(grid_copy)
        elif action == "a":
            isModified, grid_copy = self.slideLeft(grid_copy)
        elif action == "d":
            isModified, grid_copy = self.slideRight(grid_copy)
        return (isModified, grid_copy)

    def slideUp(self, g):
        grid = copy.deepcopy(g)
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size):
            for j in range(self.size):
                for row in range(i - 1, -1, -1):
                    if grid[row + 1][j] == None:
                        break
                    if grid[row][j] == None:
                        grid[row][j] = grid[row + 1][j]
                        grid[row + 1][j] = None
                        didAction = True
                    elif modified[row + 1][j] == None and grid[row][j] == grid[row + 1][j]:
                        grid[row][j] = 2 * grid[row + 1][j]
                        grid[row + 1][j] = None
                        modified[row][j] = 1
                        didAction = True
        return (didAction, grid)


    def slideDown(self, g):
        grid = copy.deepcopy(g)
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size - 1, -1, -1):
            for j in range(self.size):
                for row in range(i + 1, self.size):
                    if grid[row - 1][j] == None:
                        break
                    if grid[row][j] == None:
                        grid[row][j] = grid[row - 1][j]
                        grid[row - 1][j] = None
                        didAction = True
                    elif modified[row - 1][j] == None and grid[row][j] == grid[row - 1][j]:
                        grid[row][j] = 2 * grid[row - 1][j]
                        grid[row - 1][j] = None
                        modified[row][j] = 1
                        didAction = True
        return (didAction, grid)

    def slideRight(self, g):
        grid = copy.deepcopy(g)
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size):
            for j in range(self.size - 1, -1, -1):
                for col in range(j + 1, self.size):
                    if grid[i][col - 1] == None:
                        break
                    if grid[i][col] == None:
                        grid[i][col] = grid[i][col - 1]
                        grid[i][col - 1] = None
                        didAction = True
                    elif modified[i][col - 1] == None and grid[i][col] == grid[i][col - 1]:
                        grid[i][col] = 2 * grid[i][col - 1]
                        grid[i][col - 1] = None
                        modified[i][col] = 1
                        didAction = True
        return (didAction, grid)

    def slideLeft(self, g):
        grid = copy.deepcopy(g)
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size):
            for j in range(self.size):
                for col in range(j - 1, -1, -1):
                    if grid[i][col + 1] == None:
                        break
                    if grid[i][col] == None:
                        grid[i][col] = grid[i][col + 1]
                        grid[i][col + 1] = None
                        didAction = True
                    elif modified[i][col + 1] == None and grid[i][col] == grid[i][col + 1]:
                        grid[i][col] = 2 * grid[i][col + 1]
                        grid[i][col + 1] = None
                        modified[i][col] = 1
                        didAction = True
        return (didAction, grid)

    def printDisplay(self):
        print("Score: " + str(self.getScore(self.grid)))
        for i in range(self.size + 1):
            for j in range(self.size + 1):
                if i == 0:
                    print(str(j).center(4), end = " ")
                elif j == 0:
                    print(str(i).center(4), end = " ")
                elif self.grid[i - 1][j - 1] == None:
                    print("".center(4), end = ' ')
                else:
                    print(str(self.grid[i - 1][j - 1]).center(4), end = ' ')
            print("")

    def reset(self):
        self.grid = self.createEmptyGrid()
        self.grid = self.generateRandomTile(grid)
        self.grid = self.generateRandomTile(grid)

    def makeAction(self, action, grid, output=True):
        grid_copy = copy.deepcopy(grid)
        isModified = False
        if action == "w":
            isModified, grid_copy = self.slideUp(grid_copy)
        elif action == "s":
            isModified, grid_copy = self.slideDown(grid_copy)
        elif action == "a":
            isModified, grid_copy = self.slideLeft(grid_copy)
        elif action == "d":
            isModified, grid_copy = self.slideRight(grid_copy)
        elif action == "r":
            self.reset()
        else:
            return (False, grid_copy)
        if isModified:
            grid_copy = self.generateRandomTile(grid_copy)
        gameOver = self.isGameOver(grid_copy)
        if output:
            self.printDisplay()
            if gameOver:
                print("GAME OVER!")
                print("Your final score is: " + str(self.getScore(grid_copy)))
                print("Your highest tile was: " + str(self.getHighestTile(grid_copy)))
        return (gameOver, grid_copy)

    def playAsHuman(self):
        self.printDisplay()
        while True:
            action = input("Enter keyboard input: ")
            if action == "e":
                break
            gameOver, grid = self.makeAction(action, self.grid)
            self.grid = grid
            if gameOver:
                break

if __name__ == "__main__":
    simulator = Simulator()
    simulator.playAsHuman()
