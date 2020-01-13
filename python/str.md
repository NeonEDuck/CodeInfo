# str

## translate( table )
```python
#!/usr/bin/env python3

line = 'ATTCAG'
line = line.translate( string.maketrans('ATCG', 'TAGC') )

# String's character swap
# A ==> T
# T ==> A
# C ==> G
# G ==> C
# TAAGTC
```

## rjust( width [, fillchar=' '] )
```python
#!/usr/bin/env python3

print( 'abc'.rjust(10, '0') )
print( '12345'.rjust(10, 'a') )
print( '12345'.rjust(3, '.') )

# 0000000abc
# aaaaa12345
# 12345
```

## split( [sep=None] [, maxsplit] ) / rsplit( [sep=None] [, maxsplit] )
```python
#!/usr/bin/env python3

print( 'abc,ddee,oks'.split( ',' ) )
print( 'abc,ddee,oks'.split( ',', maxsplit = 1 ) )
print( 'abc,ddee,oks'.rsplit( ',', maxsplit = 1 ) )

# [ 'abc', 'ddee', 'oks' ]
# [ 'abc', 'ddee,oks' ]
# [ 'abc,ddee', 'oks' ]
```

## isdigit()
```python
#!/usr/bin/env python3

print( 'abcdef'.isdigit() )
print( 'abc123'.isdigit() )
print( '123456'.isdigit() )
print( 'a1b2c3'[1::2].isdigit() )

# false
# false
# true
# true
```

## isalpha()
```python
#!/usr/bin/env python3

print( '123456'.isalpha() )
print( 'abc123'.isalpha() )
print( 'abcdef'.isalpha() )
print( 'a1b2c3'[::2].isalpha() )

# false
# false
# true
# true
```

## join()
```python
#!/usr/bin/env python3

intList = [ 0, 1, 2, 3, 4 ]
newStr = ''.join( intList )
print( newStr )

newStr = ' '.join( intList )
print( newStr )

newStr = '-'.join( intList )
print( newStr )

# 01234
# 0 1 2 3 4
# 0-1-2-3-4
```