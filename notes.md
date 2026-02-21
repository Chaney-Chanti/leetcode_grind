# Tips to remember

## General python things to avoid
* Avoid using list.pop(), this is O(n). The dequeue() data structure .pop() method is O(1). This is because lists are a dynamic array with contiguous memory. Every element must also be shifted over by 1. Dequeue() is implemented as a linked list under the hood, so the data is not in contiguous blocks of memory. That is why linked lists are O(1) and not O(n).

## General python things to keep in mind
* to iterate both inde and value, use enumerate. i.e.
```
a = ["Python", "Java", "C++"]
for i, v in enumerate(a):
    print(i, v)
```
* 
