'''
Created on Feb 9, 2018

@author: gongyo
'''

pass

print 'test if-elif-else'
a = 1
if(a < 0):
    print "Negative"
elif (a == 0):
    print "zero"
else:
    print "Positive"    

print 'while-for'
a = 0
while a < 3:
    a += 1
    print ("a=" + str(a));  # TypeError: cannot concatenate 'str' and 'int' objects

for c in "test1":
    print "c=" + c,
    
colors = ["red", 'yellow']
colors.append("black")


def compare(c1="str", c2="str"):
    return c1 < c2


compare2 = lambda c1, c2: (c1 < c2);
    
colors.sort(cmp=compare2, key=None, reverse=False)

for c in colors:
    print "c=" + c,
    
for c in range(len(colors)):  # #pritn 0, 1
    print "c=" + str(c),  # #start with 0
    
for index, item in enumerate(colors):
    print 'item=' + item
        
for c in range(4, 3):  #  nothing printed
  print "c=" + str(c),
