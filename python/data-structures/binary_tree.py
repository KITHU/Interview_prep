""" 
   A binary tree meets these three facts
        1. Has exactly one root node 
        2. At most two children per node 
        3. Exactly one path b/n root and any node
"""


class Node:
    def __init__(self ,val):
        self.val = val
        self.right = None
        self.left = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f 

# Depth first for  a binary tree

def depthfirst(root):
    if root == None:
        return []
        
    rightvalue = depthfirst(root.right)
    leftvalue = depthfirst(root.left)
    

    return [root.val, *leftvalue, *rightvalue]

result = depthfirst(a)
print(result)  # ['A', 'B', 'D', 'E', 'C', 'F']

# Breadth first for a binary tree

def breadth_first(root):
    if root == None:
        return []
    queue = [root]
    result = []
    while(len(queue)> 0):
        current = queue.pop()
        result.append(current.val)
        if (current.left != None):
            queue.insert(0,current.left)
        if (current.right != None):
            queue.insert(0,current.right)

    return result

print(breadth_first(a)) # ['A', 'B', 'C', 'D', 'E', 'F']
