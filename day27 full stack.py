'''
1.Finadall:
-----------
import re
txt = 'pyhton is a dynnamically typed language'
print(re.findall('[an]',txt))

2.search:
---------
import re
txt = 'pyhton is a dynnamically typed language'
print(re.search('[a]',txt)) 

3.Split:
--------
import re
txt = 'pyhton is a dynnamically typed language'
print(re.split(' ',txt)) 

4.sub:
------
import re
txt = 'python is a dynamically typed language'
print(re.sub(' ','&',txt))

5.fullmatch:
-----------
import re
dee = 

[]:
----
import re
dee = 'Python is a dynamically typed language9865' 
print(re.findall('[0-9]',dee))
print(re.findall('[a-z]',dee))
print(re.findall('[A-Z]',dee))

^:
----
import re
dee='Have a nice day20'
print(re.findall('^Have',dee))

$:
---
import re
txt =' I have 100 Rupees'
print(re.findall('Rupees$',txt))
print(re.search('Rupees$',txt))

.:
---
import re
txt = 'I am dinesh at 21'
print(re.findall('di....',txt))

*:
---
import re
txt = 'pyhton is dynamically typed language'
print(re.findall('p.*n',txt))
print(re.findall('p.*ython',txt))


+:
---
import re
txt = 'python is a language'
print(re.findall('p.+thon',txt))
print(re.search('p.+thon',txt))

import re
txt='python is a language'
print(re.search('p.{10}',txt))

'''
import re
txt='python is a language'
print(re.search('p.{10}',txt))











