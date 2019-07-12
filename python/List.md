# from x to the end
```python
line = '0123456789'
print(line[3:])
# 3456789
```

# from the start to x
```python
line = '0123456789'
print(line[:3])
# 012
```

# x count from the back
```python
line = '0123456789'
print(line[-3:])
print(line[:-3])
# 789
# 0123456
```

# even
```python
line = '0123456789'
print(line[::2])
# 02468
```

# odd
```python
line = '0123456789'
print(line[1::2])
# 13579
```

# backward
```python
line = '0123456789'
print(line[::-1])
# 9876543210
```

# |s
```python
line = '0123456789'
print(line[3:6])
print(line[6:3:-1])
# 345
# 654

#        |3 4 5|6
#   0 1 2 3 4 5 6 7 8 9

#        |6 5 4|3
#   9 8 7 6 5 4 3 2 1 0
```
