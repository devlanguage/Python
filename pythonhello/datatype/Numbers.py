#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 当你指定一个值时，Number对象就会被创建：
var1 = 1
var2 = 13
var3 = 10
var4 = 44 // 3  # 取整除

# ##
b1 = False  # null or 0
b2 = True   

if 1 and 2:
    a = 3
elif 3 | 2:
    c = 3

print 2 ** 3;
print 2 is not 3;

# 您也可以使用del语句删除一些对象的引用。

# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]]
int1 = int('23')
int1 = long('23')
float1 = float(23)
float1 = complex(23, 4)

print "Real=", float1.real, ",Imaginary=", float1.imag  # #23.0, 4.0

float1 = float(23)

str1 = str(int1)
str2 = '23'

b1 = False;
b2 = True;

print int1 == str1  # #False
print str2 == str1  # #True

# 您可以通过使用del语句删除单个或多个对象的引用。例如：
del var1
del var3, var2
try:
    del var3
except Exception:
    print 'err', Exception.message, Exception.args
         
