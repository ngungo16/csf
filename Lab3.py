n = 100
a, b = 0, 1
temp =0
series = ['fibonacci','sum']

if series == 'fibonacci':
    for i in range (1,n):
     a,b = b,a +b
     print 'the nth fibonacci number'
elif series == 'sum':
    for i in range (1,n+1):
     temp = 3*i
     temp = temp +3
    print 'the value for the pattern 3n'
else:
    print 'Invalid string'
