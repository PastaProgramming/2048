import agents
import game

agent = agents.BFSModel(4)
totalScore = 0
best = 0
winCount = 0
TEST_NUM = 50

for i in range(TEST_NUM):
    print("Game", i+1, end="\t")
    score, won = game.runNoRender(agent)
    print("score =",score)
    totalScore += score
    if won:
        winCount += 1
    if score > best:
        best = score

average = totalScore / TEST_NUM
winPercent = winCount / TEST_NUM

print("Average score:", average)
print("Best score:", best)
print("Win percentage:", winPercent * 100)