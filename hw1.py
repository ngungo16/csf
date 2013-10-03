# Name: Ngoc (Ann) Nguyen
# Evergreen Login: ngungo16@evergreen.edu
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

b = -5.86
sum = (b**2) - 4*8.5408 # calculate the sum value inside the square root
math.sqrt(sum) 
sol1 = ((0-b)+ math.sqrt(sum))/2
sol2 = ((0-b)- math.sqrt(sum))/2
print sol1
print sol2

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test
list = hw1_test
print list.a
print list.b
print list.c
print list.d
print list.e
print list.f



###
### Problem 3
###

print "Problem 3 solution follows:"

print str ((list.a and list.b) or (not list.c) and not (list.d or list.e or list.f))


###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
