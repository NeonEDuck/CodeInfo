# itertools

### combinations( array, subsetLen )

```python
#!/usr/bin/env python3

from itertools import combinations
array = [ 1, 2, 3 ]
for subset in combinations( array, len( array ) - 1 ):
    print( subset )
    
#output:
#(1, 2)
#(1, 3)
#(2, 3)
```

### permutations( array, subsetLen )

```python
#!/usr/bin/env python3

from itertools import permutations
array = [ 1, 2, 3 ]
for subset in permutations( array, len( array ) - 1 ):
    print( subset )
    
#output:
#(1, 2)
#(1, 3)
#(2, 1)
#(2, 3)
#(3, 1)
#(3, 2)
```
