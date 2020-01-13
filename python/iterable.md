# interable
## Map

- When you want to apply a function to every elements in a iterable

### This is a example without `map`
```python
#!/usr/bin/env python3

def square(x):
	return x ** 2

list = [ 0, 1, 2, 3, 4 ]
newList = []

for i in list:
	newList.append( square( i ) )
print(newList)

# output:
# [ 0, 1, 4, 9, 16 ]
```

### Now if you do it with `map`
```python
#!/usr/bin/env python3

def square(x):
	return x ** 2

list = [ 0, 1, 2, 3, 4 ]
newList = list( map( square, list ) )

print( newList )

# output:
# [ 0, 1, 4, 9, 16 ]
```

#
## Enumerate

- When you want to loop though a iterable with `for x in y` but still want index

### This is a example without `enumerate`
```python
#!/usr/bin/env python3

fruits = [ 'apple', 'banana', 'pineapple', 'coconut' ]

i = 0
for fruit in fruits:
    print( f'{i} {fruit}' )
    i += 1
# output:
# 0 apple
# 1 banana
# 2 pineapple
# 3 coconut
```

### Now if you do it with `enumerate`
```python
#!/usr/bin/env python3

for i, fruit in enumerate( fruits ):
    print( f'{i} {fruit}' )
# output:
# 0 apple
# 1 banana
# 2 pineapple
# 3 coconut
```

### You can even specify a start
```python
#!/usr/bin/env python3

for i, fruit in enumerate( fruits, start=1 ):
    print( f'{i} {fruit}' )
# output:
# 1 apple
# 2 banana
# 3 pineapple
# 4 coconut
```