# How it started out
1. As I go through leetcode 75, I realize that every question is under a topic, which tells me what data structure to use. However, I should know how to solve the question intuitivley without knowing the structure which at the moment, I still coukldn't confidently know which structure to use. I guess it's fine for now.
2. I find that even if I know the solution conceptually, sometimes I have trouble programming it out. An example of trouble would be programming the end conditions of loops. Even if I am able to program it out, ChatGBT provides a cleaner way.


# Tips to remember

## Topics:
* Trees
    - BFS:
    ```
    from collections import deque
    
    def bfs_tree(root):
        if not root:
            return
    
        queue = deque([root])
    
        while queue:
            node = queue.popleft()
            print(node.val)
    
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    ```
    - DFS:
    ```
    def dfs_tree(root):
    if not root:
        return

    print(root.val)      # Preorder
    dfs_tree(root.left)
    dfs_tree(root.right)
    ```
    - Finding shortest path, used BFS. If need to visit all nodes, then use DFS.
* Linked Lists
    - Finding the middle of list, use tortoise and hare
    - Reverse a list, memorize:
    ```
    prev = None
    curr = slow

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    ```

## General python things to avoid
* Avoid using list.pop(), this is O(n). The dequeue() data structure .pop() method is O(1). This is because lists are a dynamic array with contiguous memory. Every element must also be shifted over by 1. Dequeue() is implemented as a linked list under the hood, so the data is not in contiguous blocks of memory. That is why linked lists are O(1) and not O(n).

## General python things to keep in mind
* to iterate both index and value, use enumerate. i.e.
```
a = ["Python", "Java", "C++"]
for i, v in enumerate(a):
    print(i, v)
```
* When passing parameters in Python, it uses pass-by-object-reference. (https://medium.com/@compuxela/what-is-pass-by-object-reference-in-python-75e7c51599f1)
*      No copy is made.
*      The object lives in one place in memory.
*      Both variables point to it
*  Python is not:
*      pass-by-value ❌
*      pass-by-reference (like C++ references) ❌
*  Python if almost like pass by reference with the exception that Python always passes a reference to an object — but assignment (=) rebinds the local name to a new object.
