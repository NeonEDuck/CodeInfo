# str

## translate
###### String's character swap
```python
line = 'ATTCAG'
line = line.translate(string.maketrans('ATCG', 'TAGC'))
# A ==> T
# T ==> A
# C ==> G
# G ==> C
# TAAGTC
```

## rjust(width[, fillchar=' '])
```python
print('abc'.rjust(10, '0'))
print('12345'.rjust(10, 'a'))
print('12345'.rjust(3, '.'))
# 0000000abc
# aaaaa12345
# 12345
```

## rsplit([sep=None][, maxsplit])
```python
print('abc,ddee,oks'.rsplit(','))
print('abc,ddee,oks'.rsplit(',',1))
# ['abc', 'ddee', 'oks']
# ['abc,ddee', 'oks']
```