"""
Author: Ricky Grannis-Vu
"""

import random

class Simulator:

    def __init__(self, size=4):
        self.score = 0
        self.size = size
        self.grid = self.createEmptyGrid()
        self.generateRandomTile()
        self.generateRandomTile()

    def createEmptyGrid(self):
        grid = []
        for i in range(self.size):
            grid.append([])
            for j in range(self.size):
                grid[i].append(None)
        return grid

    def generateRandomTile(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.grid[x][y] == None:
                self.grid[x][y] = random.choice([2, 4])
                break

    def isGameOver(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == None:
                    return False
                if i != 0 and self.grid[i][j] == self.grid[i - 1][j]:
                    return False
                if i != self.size - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
                if j != 0 and self.grid[i][j] == self.grid[i][j - 1]:
                    return False
                if j != self.size - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
        return True

    def getHighestTile(self):
        highestTile = None
        for i in range(self.size):
            for j in range(self.size):
                if highestTile == None or self.grid[i][j] > highestTile:
                    highestTile = self.grid[i][j]
        return highestTile

    def slideUp(self):
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size):
            for j in range(self.size):
                for row in range(i - 1, -1, -1):
                    if self.grid[row + 1][j] == None:
                        break
                    if self.grid[row][j] == None:
                        self.grid[row][j] = self.grid[row + 1][j]
                        self.grid[row + 1][j] = None
                        didAction = True
                    elif modified[row + 1][j] == None and self.grid[row][j] == self.grid[row + 1][j]:
                        self.grid[row][j] = 2 * self.grid[row + 1][j]
                        self.grid[row + 1][j] = None
                        modified[row][j] = 1
                        self.score += self.grid[row][j]
                        didAction = True
        return didAction


    def slideDown(self):
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size - 1, -1, -1):
            for j in range(self.size):
                for row in range(i + 1, self.size):
                    if self.grid[row - 1][j] == None:
                        break
                    if self.grid[row][j] == None:
                        self.grid[row][j] = self.grid[row - 1][j]
                        self.grid[row - 1][j] = None
                        didAction = True
                    elif modified[row - 1][j] == None and self.grid[row][j] == self.grid[row - 1][j]:
                        self.grid[row][j] = 2 * self.grid[row - 1][j]
                        self.grid[row - 1][j] = None
                        modified[row][j] = 1
                        self.score += self.grid[row][j]
                        didAction = True
        return didAction

    def slideRight(self):
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size):
            for j in range(self.size - 1, -1, -1):
                for col in range(j + 1, self.size):
                    if self.grid[i][col - 1] == None:
                        break
                    if self.grid[i][col] == None:
                        self.grid[i][col] = self.grid[i][col - 1]
                        self.grid[i][col - 1] = None
                        didAction = True
                    elif modified[i][col - 1] == None and self.grid[i][col] == self.grid[i][col - 1]:
                        self.grid[i][col] = 2 * self.grid[i][col - 1]
                        self.grid[i][col - 1] = None
                        modified[i][col] = 1
                        self.score += self.grid[i][col]
                        didAction = True
        return didAction

    def slideLeft(self):
        modified = self.createEmptyGrid()
        didAction = False
        for i in range(self.size):
            for j in range(self.size):
                for col in range(j - 1, -1, -1):
                    if self.grid[i][col + 1] == None:
                        break
                    if self.grid[i][col] == None:
                        self.grid[i][col] = self.grid[i][col + 1]
                        self.grid[i][col + 1] = None
                        didAction = True
                    elif modified[i][col + 1] == None and self.grid[i][col] == self.grid[i][col + 1]:
                        self.grid[i][col] = 2 * self.grid[i][col + 1]
                        self.grid[i][col + 1] = None
                        modified[i][col] = 1
                        self.score += self.grid[i][col]
                        didAction = True
        return didAction

    def printDisplay(self):
        print("Score: " + str(self.score))
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
        self.score = 0
        self.grid = self.createEmptyGrid()
        self.generateRandomTile()
        self.generateRandomTile()

    def play(self):
        self.printDisplay()
        while True:
            i = input("Enter keyboard input: ")
            isModified = False
            if i == "w":
                isModified = self.slideUp()
            elif i == "s":
                isModified = self.slideDown()
            elif i == "a":
                isModified = self.slideLeft()
            elif i == "d":
                isModified = self.slideRight()
            elif i == "r":
                self.reset()
            elif i == "e":
                break
            else:
                continue
            if isModified:
                self.generateRandomTile()
            self.printDisplay()
            if self.isGameOver():
                print("GAME OVER!")
                print("Your final score is: " + str(self.score))
                print("Your highest tile was: " + str(self.getHighestTile()))
                break

if __name__ == "__main__":
    simulator = Simulator()
    simulator.play()
