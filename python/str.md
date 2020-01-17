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

## ljust( width [, fillchar=' '] ) / rjust( width [, fillchar=' '] )
```python
#!/usr/bin/env python3

print( 'abc'.ljust(10, '0') )
print( '12345'.ljust(10, 'a') )
print( '12345'.ljust(3, '.') )
print( 'abc'.rjust(10, '0') )

# abc0000000
# 12345aaaaa
# 12345
# 0000000abc
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

## strip( [chars] ) / lstrip( [chars] ) / rstrip( [chars] )
```python
#!/usr/bin/env python3

print( '_*(123***123__(**('.strip('*(_') )
print( '_*(123***123__(**('.lstrip('*(_') )
print( '_*(123***123__(**('.rstrip('*(_') )
print( '  abcdefgh        '.strip() )

# 123***123
# 123***123__(**(
# _*(123***123
# abcdefgh
```

## upper() / lower() / swapcase()
```python
#!/usr/bin/env python3

print( 'abc_ABC'.upper() )
print( 'abc_ABC'.lower() )
print( 'abc_ABC'.swapcase() )

# ABC_ABC
# abc_abc
# ABC_abc
```

## isdigit()
```python
#!/usr/bin/env python3

print( 'abcdef'.isdigit() )
print( 'abc123'.isdigit() )
print( '123456'.isdigit() )
print( 'a1b2c3'[1::2].isdigit() )

# False
# False
# True
# True
```

## isalpha()
```python
#!/usr/bin/env python3

print( '123456'.isalpha() )
print( 'abc123'.isalpha() )
print( 'abcdef'.isalpha() )
print( 'a1b2c3'[::2].isalpha() )

# False
# False
# True
# True
```

## istitle()
```python
#!/usr/bin/env python3

print( 'This Is A String'.istitle() )
print( 'This is a string'.istitle() )
print( 'THIS IS A STRING'.istitle() )

# True
# False
# False
```

## isascii()
```python
#!/usr/bin/env python3

print( '123456'.isascii() )
print( 'abcdef'.isascii() )
print( 'ÄÊÎÔÛÆ'.isascii() )

# True
# True
# False
```

## join()
```python
#!/usr/bin/env python3

intList = [ 0, 1, 2, 3, 4 ]

print( ''.join( intList ) )
print( ' '.join( intList ) )
print( '-'.join( intList ) )

# 01234
# 0 1 2 3 4
# 0-1-2-3-4
```