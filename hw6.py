 
 
 # problem 3 Sorting Dictionary
 
 # Write a script that sorts the elements by mass (from elements.py)
 
 elements = OrderedDict.fromkeys('123456')

 elements.move_to_end('2')
 ''.join(elements.keys())
 '134562'
 elements.move_to_end('2', last=False)
 ''.join(elements.keys())
 '213456'
  
  # dictionary sorted by mass value
 OrderedDict(sorted(elements.items(), key=lambda t: t[1]))

 

# Problem 4:Sorting lists
# Write a script that sorts the radio active list alphabetically (radioactive.txt)

for k in sorted(set(Radio_Active)):
 return k


