# Name: Ngoc (Ann) Nguyen
# Evergreen Login: ngungo16
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test 

n=0
total = 0
while (n < 100): # using while loop to calculate the sum(1+2+...n)
   n=n+1
   total=total+n
print total
   
   
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

#using for loop to print decimal numbers

for n in range (2,10):
    print 1.0/n

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

## using for loop, via loop, via formular
n=10
triangular = 0
for i in range (1,n+1): 
    triangular = triangular + i
print 'triangular number',n, 'via loop:', triangular
print 'triangular number',n, 'via formula:',(n*(n+1))/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

## calculating factorial
n=10
factorial =1
for i in range (1,n+1):
    factorial = factorial*i
print'factorial number',n, 'via loop:', factorial
    
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

## multiple factorials in reverse order

n = 10
f=1
k=n
while k!=0:
    for i in range (1, k+1):
        f = f*i
    print "%s" % f
    f = 1
    k -= 1

        
   
 
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

## calculating sum of reciprocals
n=10
j=1.0
for i in range (1,n+1):
    j= (1.0/i)*j
print '%s' % j


###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
