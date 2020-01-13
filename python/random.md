# random

### random()
```python
#!/usr/bin/env python3

from random import random

print( random() ) # ( 0.0 ~ 1.0 )

# output:
# 0.07575896917149338
```

### randint( start, end )
```python
#!/usr/bin/env python3

from random import randint

print( randint(1, 50) ) # ( 1 ~ 50 )

# output:
# 17
```

### randrange( start, end [, interval] )
```python
#!/usr/bin/env python3

from random import randrange

print( randrange( 0, 101, 2 ) ) # ( 0 ~ 100 ) even

# output:
# 64
```

### uniform( start, end )
```python
#!/usr/bin/env python3

from random import uniform

print( uniform( 0, 50 ) ) # ( 0.0 ~ 50.0 ) 

# output:
# 34.2310553547616458
```

### choice( sample )
```python
#!/usr/bin/env python3

from random import choice

print( choice( 'ABC' ) )
print( choice( [ 'rock', 'paper', 'scissors' ] ) )

# output:
# B
# rock
```

### sample( pool, number )
```python
#!/usr/bin/env python3

from random import sample
import string

AtoJPool = 'ABCDEFGHIJ'
letterDigitPool = string.ascii_letters + string.digits
JtoAPool = ['j','i','h','g','f','e','d','c','b','a']

print( sample( AtoJPool, 3 ) )

ran_str1 = ''.join( sample( letterDigitPool, 8 ) )
print( ran_str1 )

ran_str2 = ''.join( sample( JtoAPool, 5 ) )
print( ran_str2 )

# output:
# ['E', 'J', 'G']
# dY1ohWjb
# bedif
```

### shuffle( iterable )
```python
#!/usr/bin/env python3

from random import shuffle

numList = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
shuffle( numList )
print( numList )

# output:
# [4, 2, 7, 9, 0, 1, 8, 5, 6, 3]
```