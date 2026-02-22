# How it started out
1. As I go through leetcode 75, I realize that every question is under a topic, which tells me what data structure to use. However, I should know how to solve the question intuitivley without knowing the structure which at the moment, I still coukldn't confidently know which structure to use. I guess it's fine for now.
2. I find that even if I know the solution conceptually, sometimes I have trouble programming it out. An example of trouble would be programming the end conditions of loops. Even if I am able to program it out, ChatGBT provides a cleaner way.
3. 

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
