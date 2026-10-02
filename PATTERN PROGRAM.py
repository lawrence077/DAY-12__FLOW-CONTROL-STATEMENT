Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> for i in range(1, 6):
...     for j in range(i):
...         print("*", end=" ")
...     print()
... 
...     
* 
* * 
* * * 
* * * * 
* * * * * 
>>> for i in range(1, 6):
...     for j in range(1, 6):
...         if j <= i:
...             print("*", end=" ")
...     print()
... 
...     
* 
* * 
* * * 
* * * * 
* * * * * 
>>> for i in range(5, 0, -1):
...     for j in range(i):
...         print("*",end=" ")
    print()

    
* * * * * 
* * * * 
* * * 
* * 
* 
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

    
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

    
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
