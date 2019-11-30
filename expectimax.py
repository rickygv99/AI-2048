import copy
from collections import Counter
from simulator import Simulator

def expectimax(simulator, grid, depth, isPlayer):
    if simulator.isGameOver(grid):
        return ("s", -float("inf"))

    if depth == 0:
        return (None, simulator.getScore(grid))

    if isPlayer:
        maxScore = -float("inf")
        maxAction = "s"
        for action in ["s", "a", "d", "w"]:
            gameOver, grid = simulator.slide(grid, action)
            a, score = expectimax(simulator, grid, depth, False)
            if score > maxScore:
                maxScore = score
                maxAction = action
        return (maxAction, maxScore)
    else:
        totalScore = 0
        totalActions = 0
        for i in range(simulator.size):
            for j in range(simulator.size):
                if grid[i][j] != None:
                    continue
                totalActions += 2
                new_grid = copy.deepcopy(grid)
                new_grid[i][j] = 2
                action, score = expectimax(simulator, new_grid, depth - 1, True)
                if score != -float("inf"):
                    totalScore += score
                new_grid[i][j] = 4
                action, score = expectimax(simulator, new_grid, depth - 1, True)
                if score != -float("inf"):
                    totalScore += score
        if totalActions == 0:
            totalActions = 1
        expected_value = totalScore / totalActions
        return (None, expected_value)

if __name__ == "__main__":
    scores = []
    highestTiles = []
    numTrials = 1
    action_order = ["s", "a", "d", "w"]
    for i in range(numTrials):
        simulator = Simulator()
        gameOver = False
        while gameOver == False:
            old_grid = copy.deepcopy(simulator.grid)
            action, score = expectimax(simulator, simulator.grid, 3, True)
            gameOver, grid = simulator.makeAction(action, simulator.grid, output=False)
            simulator.grid = grid
            new_grid = simulator.grid
            if old_grid == new_grid:
                for action in action_order:
                    old_grid = copy.deepcopy(simulator.grid)
                    gameOver, grid = simulator.makeAction(action, simulator.grid, output=False)
                    simulator.grid = grid
                    if gameOver:
                        break
                    new_grid = simulator.grid
                    if old_grid != new_grid:
                        break
            print(simulator.grid)
        scores.append(simulator.getScore(simulator.grid))
        highestTiles.append(simulator.getHighestTile(simulator.grid))
    averageScore = sum(scores) / numTrials
    highestScore = max(scores)
    frequencyHighestTiles = dict(Counter(highestTiles))
    print("Average score: " + str(averageScore))
    print("Highest score: " + str(highestScore))
    print("Highest tiles: " + str(frequencyHighestTiles))
