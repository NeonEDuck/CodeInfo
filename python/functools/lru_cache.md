# functools.lru_cache

## lru_cache
    - lru_cache will help you save the result of the function, so the next time you run it, it will just return the result it saved.

### This is a example without any cache, time required: 131.2590253s
```python
#!/usr/bin/env python3

import timeit

def fibonacci( n ):
    if n <= 2:
        return 1
    else:
        return fibonacci( n - 1 ) + fibonacci( n - 2 )


tic = timeit.default_timer() # timer start

for i in range( 41 ):
    print( f'fibonacci( {i} ) = {fibonacci( i )}' )

toc = timeit.default_timer() # timer end


print(f'Time required: {toc - tic}s')

# fibonacci( 1 ) = 1
# .
# .
# fibonacci( 40 ) = 102334155
# Time required: 131.2590253s
```

### This is a example with self wrote cache system, time required: 0.008355999999999999s
```python
#!/usr/bin/env python3

import timeit

fibonacci_cache = {}

def fibonacci( n ):

    if n in fibonacci_cache.keys():
        return fibonacci_cache[n]

    value = 0
    if n <= 2:
        value = 1
    else:    
        value = fibonacci( n - 1 ) + fibonacci( n - 2 )
    
    fibonacci_cache[n] = value

    return value

tic = timeit.default_timer() # timer start

for i in range( 41 ):
    print( f'fibonacci( {i} ) = {fibonacci( i )}' )

toc = timeit.default_timer() # timer end


print(f'Time required: {toc - tic}s')

# fibonacci( 1 ) = 1
# .
# .
# fibonacci( 40 ) = 102334155
# Time required: 0.008355999999999999s
```

### This is a example with lru_cache, time required: 0.008177199999999996s
```python
#!/usr/bin/env python3

from functools import lru_cache
import timeit

@lru_cache( maxsize=256 )
def fibonacci( n ):
    if n <= 2:
        return 1
    else:
        return fibonacci( n - 1 ) + fibonacci( n - 2 )


tic = timeit.default_timer() # timer start

for i in range( 41 ):
    print( f'fibonacci( {i} ) = {fibonacci( i )}' )

toc = timeit.default_timer() # timer end


print(f'Time required: {toc - tic}s')
```