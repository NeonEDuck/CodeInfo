# random

### random()
```python
#!/usr/bin/env python3

import random

print(random.random())

# output:
# 0.07575896917149338
```

### randint( int=start, int=end )
```python
#!/usr/bin/env python3

import random

print(random.randint(1, 50)) #(1~50)

# output:
# 17
```

### randrange( int=start, int=end, int=interval)
```python
#!/usr/bin/env python3

import random

print(random.randrange(0, 101, 2)) #(0~100) even

# output:
# 64
```

### uniform( int=start, int=end )
```python
#!/usr/bin/env python3

import random

print(random.uniform(0, 50)) #(0~50) 

# output:
# 34.2310553547616458
```

### choice( str=sample )
```python
#!/usr/bin/env python3

import random

print(random.choice('ABC'))
print(random.choice(['rock', 'paper', 'scissors']))

# output:
# B
# rock
```

### sample( str=sample )
```python
#!/usr/bin/env python3

import random
import string

print(random.sample('ABCDEFGHIJ', 3))
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)
ran_str2 = ''.join(random.sample(['j','i','h','g','f','e','d','c','b','a'], 5))
print(ran_str2)

# output:
# ['E', 'J', 'G']
# dY1ohWjb
# bedif
```

### shuffle( list=target )
```python
#!/usr/bin/env python3

import random

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(numList)
print(numList)

# output:
# [4, 2, 7, 9, 0, 1, 8, 5, 6, 3]
```