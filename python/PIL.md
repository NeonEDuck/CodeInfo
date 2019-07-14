# PIL
###### python -m pip install pillow

## Image
### open( str=path )
```python
#!/usr/bin/env python3

from PIL import Image
path = 'example.png'
img = Image.open(path)
```
### size
```python
#!/usr/bin/env python3

from PIL import Image
path = 'example.png'
img = Image.open(path)
print(img.size)

# output:
# (150, 150)
```

### new( str=mode, tuple=size )
```python
#!/usr/bin/env python3

from PIL import Image
img = Image.new('RGB', (150, 150))
print(img.mode)
print(img.size)

# output:
# RGB
# (150, 150)
```

### load()
```python
#!/usr/bin/env python3

from PIL import Image
path = 'example.png'
img = Image.open(path)
data = img.load()
w, h = img.size

for x in range(w):
    for y in range(h):
        print(data[x,y])

# output:
# (255, 255, 255)
# (255, 255, 255)
# (255, 255, 255)
# (255, 255, 255)
# (255, 255, 255)
# ...
```

### save(str=path)
```python
#!/usr/bin/env python3

from PIL import Image
import math
w, h = 150, 150
img = Image.new('RGB', (w, h))
data = img.load()

for x in range(w):
    for y in range(h):
        c = int(math.pow(( x + y ) / ( w + h - 1 ), 2) * 255)
        color = (c, c, c)
        data[x,y] = color

img.save('output.png')
```