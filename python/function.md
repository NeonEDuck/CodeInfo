# map
```python
	def square(x):
		return x ** 2
	list = [0, 1, 2, 3, 4]
	newList = list( map(square,list) )
	print(newList)
	
	# [0, 1, 4, 9, 16]
```

# join
```python
	intList = [0, 1, 2, 3, 4]
	newStr = ''.join(intList)
	print(newStr)
	
	newStr = ' '.join(intList)
	print(newStr)
	
	newStr = '-'.join(intList)
	print(newStr)
	
	# 014916
	# 0 1 4 9 16
	# 0-1-4-9-16
```
