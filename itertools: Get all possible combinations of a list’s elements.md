### itertools.combinations(list(), int)

```python
import itertools

array = [1, 2, 3]
for subset in itertools.combinations(array, len(array)-1):
    print(subset)
    
#output:
#(1, 2)
#(1, 3)
#(2, 3)
```

### itertools.permutations(list(), int)

```python
import itertools

array = [1, 2, 3]
for subset in itertools.permutations(array, len(array)-1):
    print(subset)
    
#output:
#(1, 2)
#(1, 3)
#(2, 1)
#(2, 3)
#(3, 1)
#(3, 2)
```
