import agents
import game

player = agents.HeuristicModel()
average = 0
best = 0
TEST_NUM = 50

for i in range(TEST_NUM):
    score = game.runNoRender(player)
    average += score
    if score > best:
        best = score


average /= TEST_NUM

print("Average score:", average)
print("Best score:", best)