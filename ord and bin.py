Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> for i in range(1,6):
...     for j in range(0,i):
...         print(chr(i+64), end=' ')
...     print()
... 
...     
A 
B B 
C C C 
D D D D 
E E E E E 
>>> 
>>> name= 'LAWRENCE,JAMES,CRISTIANO,GOD'
>>> for i in name:
...     print(i,ord(i),bin(ord(i)))
... 
...     
L 76 0b1001100
A 65 0b1000001
W 87 0b1010111
R 82 0b1010010
E 69 0b1000101
N 78 0b1001110
C 67 0b1000011
E 69 0b1000101
, 44 0b101100
J 74 0b1001010
A 65 0b1000001
M 77 0b1001101
E 69 0b1000101
S 83 0b1010011
, 44 0b101100
C 67 0b1000011
R 82 0b1010010
I 73 0b1001001
S 83 0b1010011
T 84 0b1010100
I 73 0b1001001
A 65 0b1000001
N 78 0b1001110
O 79 0b1001111
, 44 0b101100
G 71 0b1000111
O 79 0b1001111
D 68 0b1000100
name= 'lawrence, shah, omgandhan, asraf'
for i in name:
    print(i,ord(i),bin(ord(i)))

    
l 108 0b1101100
a 97 0b1100001
w 119 0b1110111
r 114 0b1110010
e 101 0b1100101
n 110 0b1101110
c 99 0b1100011
e 101 0b1100101
, 44 0b101100
  32 0b100000
s 115 0b1110011
h 104 0b1101000
a 97 0b1100001
h 104 0b1101000
, 44 0b101100
  32 0b100000
o 111 0b1101111
m 109 0b1101101
g 103 0b1100111
a 97 0b1100001
n 110 0b1101110
d 100 0b1100100
h 104 0b1101000
a 97 0b1100001
n 110 0b1101110
, 44 0b101100
  32 0b100000
a 97 0b1100001
s 115 0b1110011
r 114 0b1110010
a 97 0b1100001
f 102 0b1100110
