import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Insert:
    # check if empty
    # if empty put node here/at root
    # else
    # if new < node.value
    #    leftnode.insert value
    # if >= 
    #    rightnode.insertvalue

    #### self.left is the left node and you can call self.left.method
    #### self.right is the right node and you can call self.right.method
    #### The above are true if self.left and self.right are not None, if either is None, then we must create a new BST using BinarySearchTree(value)
    
    def insert(self, value):
        
        if self.value == None:
            self.value = value
            return
        elif value >= self.value:
            if self.right == None:
                new_node = BinarySearchTree(value)
                self.right = new_node
                return
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left == None:
                new_node = BinarySearchTree(value)
                self.left = new_node
                return
            else: 
                self.left.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # find:
        # if node is none
        # return false
        # if node.value == findvalue
        #     return true
        # else
        #     if find <  node.value
        #         find on  left node
        #     else
        #         find on right node

        if self == None:
            return False
        elif self.value == target:
            return True
        elif target > self.value:
                if self.right == None: 
                    return False
                else:
                    return self.right.contains(target)
        else: ##remaining case target < self.value
            if self.left == None: 
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # get_max:
        # if there's a right:
        # get max on  right
        # else
        #return node.value

        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

        # if self.right:
        #     return self.right.get_max()
        # else:
        #     return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
  
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)  

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return
        if node.left != None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right != None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(self)
        if node.value == None:
            return
        else:
            while q.size != 0:
                node = q.dequeue()
                print(node.value)
                if node.left != None:
                    q.enqueue(node.left)
                if node.right != None:
                    q.enqueue(node.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        if node.value == None:
            return
        else:
            while stack.size != 0:
                node = stack.pop()
                print(node.value)
                if node.left != None and node.left.value != self.value:
                    stack.push(node.left)
                if node.right != None and node.right.value != self.value:
                    stack.push(node.right)
            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node == None:
            return
        else:
            print(node.value)
            if node.left != None:
                self.pre_order_dft(node.left)
            if node.right != None:
                self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node == None:
            return
        else:
            if node.left != None:
                self.post_order_dft(node.left)
            if node.right != None:
                self.post_order_dft(node.right)
            print(node.value)
            

example = BinarySearchTree(4)
example.insert(5)
example.insert(7)
example.insert(3)
example.insert(6)
example.insert(8)
example.insert(2)

example.post_order_dft(example)