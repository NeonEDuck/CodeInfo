# stdin

###### python *.py < files

```python
import sys

raw = ''
for line in sys.stdin:
    raw += line

data = raw.split('\n')
```
