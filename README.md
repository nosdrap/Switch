# Switch

Just simple switch function for python

## Usage

```python
from switch import *

# value = switch(variable,array)
# variable = variable you want to switch
# array = [[value,return_value],["default",return_value]
# return_value = value or function name
# "default" must be last or it will ignore any options after

value = switch(x,array)
print(value)

function = switch(x,array)
function()
```