# datetime

## datetime
### datetime( year, month, day, hour=0, minute=0, second=0, microsecond=0 )
```python
#!/usr/bin/env python3

from datetime import datetime
date = datetime( 2019, 2, 14, 10, 30, 25 )

print( date )
print( type( date ) )
    
# output:
# 2019-02-14 10:30:25
# <class 'datetime.datetime'>
```

### now()
```python
#!/usr/bin/env python3

from datetime import datetime
date = datetime.now()

print( date )
print( type( date ) )
    
# output:
# 2019-07-14 15:41:05.648136
# <class 'datetime.datetime'>
```

### strftime( format )
```python
#!/usr/bin/env python3

from datetime import datetime
dateStrFormat = '%Y-%m-%d %H:%M:%S'

date = datetime.now()
dateStr = date.strftime( dateStrFormat )

print( dateStr )
print( type( dateStr ) )
    
# output:
# 2019-07-14 15:41:05
# <class 'str'>
```

### strptime( dateStr, format )
```python
#!/usr/bin/env python3

from datetime import datetime
dateStrFormat = '%Y-%m-%d %H:%M:%S'

date = datetime.strptime( '2019-07-14 15:41:05', dateStrFormat )

print( date )
print( type( date ) )
    
# output:
# 2019-07-14 15:41:05
# <class 'datetime.datetime'>
```

### year, month, day, hour, minute, second, microsecond
```python
#!/usr/bin/env python3

from datetime import datetime

date = datetime.now()

print( date.year )
print( date.month )
print( date.day )
print( date.hour )
print( date.minute )
print( date.second )
print( date.microsecond )
print( type( dat ) )
    
# output:
# 2019
# 7
# 14
# 15
# 41
# 05
# 32054
# <class 'datetime.datetime'>
```

#
## date
### date( year, month, day )
```python
#!/usr/bin/env python3

from datetime import date
date = date( 2019, 2, 14 )

print( date )
print( type( date ) )
    
# output:
# 2019-02-14
# <class 'datetime.date'>
```

### today()
```python
#!/usr/bin/env python3

from datetime import date
date = date.today()

print( date )
print( type( date ) )
    
# output:
# 2019-07-14
# <class 'datetime.date'>
```

### strftime( format )
```python
#!/usr/bin/env python3

from datetime import date
dateStrFormat = '%Y-%m-%d %H:%M:%S'
date = date.today()
dateStr = date.strftime( dateStrFormat )

print( dateStr )
print( type( dateStr ) )
    
# output:
# 2019-07-14 00:00:00
# <class 'str'>
```

### year, month, day
```python
#!/usr/bin/env python3

from datetime import date
date = date.today()

print( date.year )
print( date.month )
print( date.day )
print( type( date ) )
    
# output:
# 2019
# 7
# 14
# <class 'datetime.date'>
```

#
## timedelta( [days=0] [, hours=0] [, minutes=0] [, seconds=0] [, microseconds=0] )

```python
#!/usr/bin/env python3

from datetime import date
from datetime import timedelta
date = date.today()
oneDay = timedelta( days = 1 )
oneHour = timedelta( hours = 1 )
oneMinute = timedelta( minutes = 1 )
oneSecond = timedelta( seconds = 1 )
oneMicrosecond = timedelta( microseconds = 1 )

tomorrow = date + oneDay

print( tomorrow )
print( type( tomorrow ) )
    
# output:
# 2019-07-15
# <class 'datetime.date'>
```