# Cup problem

```python
import sys

line = []
with sys.stdin as data:
    line = data.read().split('\n')

loop = int(line[0])

cupSize = (40, 24, 110)
goal = 65

allState = []
waterAmount = []

def findState(state, water):
    if (state in allState):
        if water >= waterAmount[allState.index(state)]:
            return
        else:
            waterAmount[allState.index(state)] = water
    else:
        allState.append(state)
        waterAmount.append(water)

    a,b,c = state

    if a > 0:
        if (cupSize[1] - b) > a:
            findState((0, b+a, c), water+a)
        else:
            findState((a-(cupSize[1]-b), cupSize[1], c), water+(cupSize[1]-b))

        if (cupSize[2] - c) > a:
            findState((0, b, c+a), water+a)
        else:
            findState((a-(cupSize[2]-c), b, cupSize[2]), water+(cupSize[2]-c))

    
    if b > 0:
        if (cupSize[0] - a) > b:
            findState((a+b, 0, c), water+b)
        else:
            findState((cupSize[0], b-(cupSize[0]-a), c), water+(cupSize[0]-a))

        if (cupSize[2] - c) > b:
            findState((a, 0, c+b), water+b)
        else:
            findState((a, b-(cupSize[2]-c), cupSize[2]), water+(cupSize[2]-c))

    if c > 0:
        if (cupSize[0] - a) > c:
            findState((a+c, b, 0), water+c)
        else:
            findState((cupSize[0], b, c-(cupSize[0]-a)), water+(cupSize[0]-a))

        if (cupSize[1] - b) > c:
            findState((a, b+c, 0), water+c)
        else:
            findState((a, cupSize[1], c-(cupSize[1]-b)), water+(cupSize[1]-b))

for i in range(1,loop+1):
    number = line[i].split(' ')
    cupSize = tuple(map(int,(number[0], number[1], number[2])))
    goal = int(number[-1])

    allState = []
    waterAmount = []

    findState((0, 0, cupSize[2]), 0)

    listOfGoal = []
    small = (0,0)

    for allState, waterAmount in zip(allState, waterAmount):
        a,b,c = allState
        if a == goal or b == goal or c == goal:
            listOfGoal.append((a,b,c,waterAmount))
        
        if a < goal:
            if a > small[0] or (a == small[0] and waterAmount < small[-1]):
                small = (a,waterAmount)
        if b < goal:
            if b > small[0] or (b == small[0] and waterAmount < small[-1]):
                small = (b,waterAmount)
        if c < goal:
            if c > small[0] or (c == small[0] and waterAmount < small[-1]):
                small = (c,waterAmount)

    if len(listOfGoal) > 0:
        min = listOfGoal[0]
        for g in listOfGoal:
            if g[-1] < min[-1]:
                min = g
        print(min[-1],goal)
    else:
        print(small[1],small[0])
```
