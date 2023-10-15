import agents
import game

player = agents.GreedyModel()
average = 0
TEST_NUM = 500

for i in range(TEST_NUM):
    average += game.runNoRender(player)

average /= TEST_NUM

print("Average score:", average)