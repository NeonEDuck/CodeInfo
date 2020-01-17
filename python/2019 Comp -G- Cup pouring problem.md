# Cup pouring problem

### Problem G：倒水問題
- 有a, b, c三杯水，每杯水都有容量限制。前兩個杯子中初始時沒有水，第三個装滿水，倒法是一杯水到另一杯水倒到自己空或是別人滿為止。題目輸入為a, b, c, d，問是否可以倒出d公升的水，如果倒不出，則倒出一個最大的d'，使得d' <= d，並且在過程中要求總倒水量最少。
### **輸入說明:**  
- 第一列的數字*n*代表有幾筆資料要測試，2<=n<=30，之後每列為每組的測試資料，為四個數字。輸入為 a, b, c, d，( 1 <= a, b, c, d <= 200 )。倒水問題一般有三個杯子，容量分別為a, b, c，最初只有第3個杯子裝滿了c升水，其他兩個杯子為空，求要得到d公升的水，總共需要倒幾公升的水，則倒出一個最大的d'，使得d <= d。要避免重複拜訪。
### **輸出說明:**  
- 你的程式要對每一組測試資料，要求輸出最少的倒水量和目標水量(d或者d')
- 注意:本題的目標是倒的水量最少，而不是步數最少。實際上，水量最少時步数不一定最少，例如a=1, b=12, c=15, d=7，倒水量最少的方案是C->A, A->B重複7次，最後C裏有7升水。一共14步，總水量也是14。還有一種方法是C->B，然後B->A, A->C重複4次，最後C裏有7升水。一共只有10步，但總水量多達20。因此，需要改一下算法：不是每次取出步數最少的結點進行擴展，而是取出水量最少的節點進行擴展。

```python
import sys

raw = ''
for line in sys.stdin:
    raw += line

data = raw.split('\n')

loop = int(data[0])
cupSize = ( 0, 0, 0 )
goal = 0

def pourInto( acup, bcup, bcupSize ):
    """Pour acup into bcup"""
    bEmpty = bcupSize - bcup

    _a = max( 0, acup - bEmpty )
    _b = bcup + ( acup - _a )

    return ( _a, _b )

allState = {}
def findState( state, water ):
    """Loop though all the posible state and store it into allState"""

    # if the state have been repeated, return
    if state in allState.keys():
        if water < allState.get( state ):
            return
        else:
            allState[state] = water
    else:
        allState[state] = water

    a, b, c = state

    # pour the water and keep looping
    if a > 0:
        _a, _b = pourInto( a, b, cupSize[1] )
        findState( ( _a, _b, c ), water + ( a - _a ) )
        
        _a, _c = pourInto( a, c, cupSize[2] )
        findState( ( _a, b, _c ), water + ( a - _a ) )
    
    if b > 0:
        _b, _a = pourInto( b, a, cupSize[0] )
        findState( ( _a, _b, c ), water + ( b - _b ) )
        
        _b, _c = pourInto( b, c, cupSize[2] )
        findState( ( a, _b, _c ), water + ( b - _b ) )

    if c > 0:
        _c, _a = pourInto( c, a, cupSize[0] )
        findState( ( _a, b, _c ), water + ( c - _c ) )
        
        _c, _b = pourInto( c, b, cupSize[1] )
        findState( ( a, _b, _c ), water + ( c - _c ) )



for i in range( 1, loop + 1 ):
    nums = data[i].split( ' ' )

    cupSize = tuple( map( int, ( nums[0], nums[1], nums[2] ) ) )
    goal = int( nums[-1] )

    allState = {}
    
    findState( ( 0, 0, cupSize[2] ), 0 )
    listOfGoal = []
    small = ( 0, 0 )

    for state, waterAmount in allState.items():
        a, b, c = state
        
        for cup in ( a, b, c ):
            if cup == goal:
                listOfGoal.append( ( a, b, c, waterAmount ) )
            if cup < goal:
                if cup > small[0] or ( cup == small[0] and waterAmount < small[-1] ):
                    small = ( cup, waterAmount )


    
    if listOfGoal != []:
        minGoal = min( listOfGoal, key=lambda x: x[-1] )
        print( minGoal[-1], goal )
    else:
        print( small[1], small[0] )
```