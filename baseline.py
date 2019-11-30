import copy
from collections import Counter
from simulator import Simulator

if __name__ == "__main__":
    scores = []
    highestTiles = []
    numTrials = 1000
    action_order = ["s", "a", "d", "w"]
    for i in range(numTrials):
        simulator = Simulator()
        gameOver = False
        while gameOver == False:
            for action in action_order:
                old_grid = copy.deepcopy(simulator.grid)
                gameOver, grid = simulator.makeAction(action, simulator.grid, output=False)
                simulator.grid = grid
                if gameOver:
                    break
                new_grid = simulator.grid
                if old_grid != new_grid:
                    break
        scores.append(simulator.getScore(simulator.grid))
        highestTiles.append(simulator.getHighestTile(simulator.grid))
    averageScore = sum(scores) / numTrials
    highestScore = max(scores)
    frequencyHighestTiles = dict(Counter(highestTiles))
    print("Average score: " + str(averageScore))
    print("Highest score: " + str(highestScore))
    print("Highest tiles: " + str(frequencyHighestTiles))
