Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a =
SyntaxError: invalid syntax
>>> a = [ 'she' , 'sells' , 'sea' , 'shells' , 'by' , 'the' , 'sea' , 'shore' ,]
>>> b = "selfish shellfish"
>>> c = [1, 1, 2, 3, 5, 8, 13]
>>> b[3:4]
'f'
>>> c[-2]
8
>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[3]
'shells'
>>> a[2]
'sea'
>>> 'by' in a
True
>>> 'self' in b
True
>>> a[2] == a[6]
True
>>> [1,2,5] in c
False
>>> 'sh' in c
False
>>> a[3] == b[8:13]
False
>>> False
False
>>> dog = 'damlmatian'
>>> len (dog)
10
>>> dogs = [dog, 'poodle', 'boxer']
>>> len (dog)
10
>>> one = [1,2,3,4]
>>> two = [7,6,5,4]
>>> three = ["y1", "friends", "fun"]
>>> print (one + two)
[1, 2, 3, 4, 7, 6, 5, 4]
>>> print (one[3])
4
>>> one.remove(4)
>>> len(dogs)
3
>>> len \
    jkhffd
SyntaxError: invalid syntax
>>> one.remove.__call__(4)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    one.remove.__call__(4)
ValueError: list.remove(x): x not in list
>>> one.remove(4)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    one.remove(4)
ValueError: list.remove(x): x not in list
>>> one = [1,2,3,4]
>>> two = [7,6,5,4]
>>> three = ["y1", "friends", "fun"]
>>> one.remove(4)
>>> print(one)
[1, 2, 3]
>>> one.pop(1)
2
>>> one.append (4)
>>> print (one)
[1, 3, 4]
>>> one.sort()
>>> print(one)
[1, 3, 4]
>>> ValueError: list.remove(x): x not in list
SyntaxError: invalid syntax
>>> my_str ="meat"
>>> my_str[2] = "e"
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    my_str[2] = "e"
TypeError: 'str' object does not support item assignment
>>> x,y,z = (3,4,5)
>>> my_tuple = (3,4,5)
>>> (x+y+z)
12
>>> print (my_tuple+my_tuple)
(3, 4, 5, 3, 4, 5)
>>> print (x*3)
9
>>> TypeError: 'str' object does not support item assignment
SyntaxError: invalid syntax
>>> print(my_tuple*3)
(3, 4, 5, 3, 4, 5, 3, 4, 5)
>>> print (my_tuple[0]==x)
True
>>> print (x[0])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print (x[0])
TypeError: 'int' object is not subscriptable
>>> my_tuple[0]=17
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    my_tuple[0]=17
TypeError: 'tuple' object does not support item assignment
>>> my_tuple[0]=17 print(my_tuple)
SyntaxError: invalid syntax
>>> my_tuple=[3,4,5]
>>> my_tuple[0]=17
>>> print(my_tuple)
[17, 4, 5]
>>> my_tuple=(3,4,5)
>>> my_tuple=(6,7,8)
>>> my_tuple.append(4)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    my_tuple.append(4)
AttributeError: 'tuple' object has no attribute 'append'
>>> my_list=[3,4,5]
>>> my_list.append(3)
>>> my_list
[3, 4, 5, 3]
>>> my_tuple+(17,)
(6, 7, 8, 17)
>>> my_tuple=my_tuple+(17,)
>>> my_tuple
(6, 7, 8, 17)
>>> (6, 7, 8, 17)
(6, 7, 8, 17)
>>> x=17
>>> print (x)
17
>>> import turtle
>>> print (turtle.pos)
<function pos at 0x7f12d6ecb158>
>>> time.sleep(3)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    time.sleep(3)
NameError: name 'time' is not defined
>>> import time
>>> time.sleep(3)
>>> time=3
>>> time.sleep(3)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    time.sleep(3)
AttributeError: 'int' object has no attribute 'sleep'
>>> print(type(turtle.pos))
<class 'function'>
>>> print (turtle.pos())
(0.00,0.00)
>>> 
