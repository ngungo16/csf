 
from element import *
 
 # problem 3 Sorting Dictionary
 
 # Write a script that sorts the elements by mass (from elements.py)
 
elements2 = OrderedDict.fromkeys('123456')

elements2.move_to_end('2')
''.join(elements2.keys())
'134562'
elements2.move_to_end('2', last=False)
''.join(elements2.keys())
'213456'
  
# dictionary sorted by mass value
OrderedDict(sorted(elements2.items(), key=lambda t: t[1]))

 


 # Problem 4:Sorting lists
# Write a script that sorts the radio active list alphabetically (radioactive.txt)

for k in sorted(set(Radio_Active)):
 return k


