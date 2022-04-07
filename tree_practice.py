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
def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.value)
         res = res + self.inorderTraversal(root.right)
      return res
def PostorderTraversal(self, root):
    res = []
    if root:
        res = self.PostorderTraversal(root.left)
        res = res + self.PostorderTraversal(root.right)
        res.append(root.data)
    return res

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()