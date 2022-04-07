# Trees
****
You might be wondering what a tree is in programming. No it isn't something that we have to water. It is more of a way to organize data. Most trees are used for sorting data but can be used as decision tree. Either way it is used a tree is made up of nodes and branches. Every tree will have a beginning node that we call the root. All other nodes will branch out from the root node. A path that you take from one node to another neighboring node is called a branch. A node that is pointing another node is considered the parent of the node it is pointing to. A node that is being pointed at is considered a child of the node that is pointing at it. Here is the basic structure of a tree.<br> ![Image of Computing Tree](/assets/Binary_tree.svg.png "Image of Computing Tree")
<br>1. What is the root of this tree?<br>2. What are the children of node 6?
<br>3. Who is the parent of node 7?<br>4. How many branches are in this tree?

<details><summary>Answers</summary>

1. The root of this tree is `2`.
2. The children of node `6` are `5` and `11`.
3. The parent of `7` is `2`.
4. There are 8 branches in this tree. [2->5, 5->9, 9->4, 2->7, 7->2, 7->6, 6->5, 6->11]

</details> 

****
## Creating a binary tree
We are going to make what is called a binary tree. This is like a normal tree except that a node can only have two children. So lets start by creating the root and node class. <br><br>
We are going to create a new class `Node`. So what data does a node have. Well in a binary tree it will point to a maximum of two other nodes. So we will assign those a `left` and a `right` variable. We will also need to store the value that the node has so we will store that as `value`. Ok lets write the class.
```python

class Node:
   def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value
   def PrintTree(self):
      print(self.value)

root = Node(10) # Tree with one node equal to 10
root.PrintTree() # This will print 10

```
Notice in the code how there is no `parent` variable. This is because a lot of trees only point one way, towards their children. We also added a print tree function so we could display the data of the tree to the console. Right now we are only printing the one node but we will add functionality to print multiple nodes after we write an insert function 
****
## Node.insert()
****
For this specific tree, we will want to be able to insert a new node to the left if the value is less than the node we want to insert after. We will insert the node to the right if the value is greater than. So if we are looking to insert after our original node `10` a value of `5` would go to the left and a value of `11` would go to the right. 

```python

class Node:
   def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value

   def insert(self, value):
# Compare the new value with the parent node
      if self.value: #Checks to see if node exists
        if value < self.value: #Checks if value is less than current node and moves it left
            if self.left is None:
               self.left = Node(value)
            else:
               self.left.insert(value)

        elif value > self.value:#Checks if value is more than current node and moves it right
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
      else:
         self.value = value #Ensures no copies

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.value),
      if self.right:
         self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree() # Prints 3,6,12,14
```
Notice how multiple instances of value cannot be stored at the same time. So if you tried to `insert(12)` nothing would happen. 

****
## In-Order Traversal
****
Traversal is going through your tree in a designated pattern. In-order traversal is when we go from the farthest left to the farthest right. We can do that by checking our left most nodes first then appending the next right node

```python
def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.value)
         res = res + self.inorderTraversal(root.right)
      return res
```
****
## Post-Order Traversal

****
Post-Order traversal the root is visited last. First we will traverse the left of the tree and then the right of the tree. But again we need to ensure that the root will be last. 

```python
def PostorderTraversal(self, root):
    res = []
    if root:
        res = self.PostorderTraversal(root.left)
        res = res + self.PostorderTraversal(root.right)
        res.append(root.value)
    return res
```
Here you can see that we go through the left most part of the tree first then we visit the right. At the end we are able to finally visit the node. 

****
## Pre-Order Traversal (Problem)
****
Pre-order traversal is very similar to Post-Order except we start with the root then go out. What you need to do is design a function that will allow for Pre-Order traversal.
### Requirements
1. Must display the node first.
2. Must traverse from left to right

(Hint: Notice the similarities and differences of the two previous functions)

<details><summary>Answer</summary>

```python

def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.value)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res

```

</details>

****
## Conclusion
That is a very basic structure of a tree. There are plenty of things you can do with sorting data. The data that you can put into a tree can be anything really. You just have to make sure there is a key to organize it whether it be numerical, alphabetical, by size, etc. 
****
# Table of Contents
## [Welcome](/0-welcome.md)<br>
## [Queues](/1-queue.md)<br>
## [Sets](/2-set.md)<br>
## [Trees](/3-tree.md)<br>