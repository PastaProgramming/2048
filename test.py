import agents
import game

player = agents.BFSModel(5)
average = 0
TEST_NUM = 50

for i in range(TEST_NUM):
    average += game.runNoRender(player)

average /= TEST_NUM

print("Average score:", average)