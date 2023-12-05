# A binary tree node has data, pointer to left child and a pointer to
#   right child
 
 
import time
import sys

sys.setrecursionlimit(100000000)  # Set an appropriate limit

class node:
 
    def __init__(self):
        # instance fields found by C++ to Python Converter:
        self.data = 0
        self.vc = 0
        self.left = None
        self.right = None
 
 
# Driver program to test above functions
def main():
    # Let us construct the tree given in the above diagram
    # root = Globals.newNode(20)
    # root.left = Globals.newNode(8)
    # root.left.left = Globals.newNode(4)
    # root.left.right = Globals.newNode(12)
    # root.left.right.left = Globals.newNode(10)
    # root.left.right.right = Globals.newNode(14)
    # root.right = Globals.newNode(22)
    # root.right.right = Globals.newNode(25)

    dataset = ["kecil_dp", "kecil_bnb", "sedang_dp", "sedang_bnb", "besar_dp", "besar_bnb"]
    
    for data in dataset:
        datafile = f"./{data}.txt"
        # datafile = "./kecil_dp.txt"

        with open(datafile, 'r') as file:
            first_line_array = list(map(int, file.readline().split()))
            nested_list = [list(map(int, line.split())) for line in file.readlines() if line]
        
        root = Globals.newNode(1)
        root.left = Globals.newNode(nested_list[0][0])
        root.right = Globals.newNode(nested_list[0][1])
        lastLeft = root.left
        lastRight = root.right

        # TURN THE INPUT DATA TO TREE
        for i in range(len(nested_list) - 1):
            if i%2 == 0:
                # left
                newRoot = lastLeft
                if (len(nested_list[i+1]) > 1):
                    newRoot.left = Globals.newNode(nested_list[i+1][1])   
                    lastLeft = newRoot.left 
                else:
                    continue
            elif i%2 == 1:
                newRoot = lastRight
                if (len(nested_list[i+1]) > 1):
                    newRoot.right = Globals.newNode(nested_list[i+1][2])  
                    lastRight = newRoot.right
                else:
                    continue
        

        start_time = time.perf_counter()
        print("Size of the smallest vertex cover is ", end='')
        print(Globals.vCover(root), end='')
        print()
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        print(f"Execution time for {datafile} is {execution_time} ms")

        print("\n", end='')
    
 
class Globals:
    # A utility function to find min of two integers
    @staticmethod
    def min(x, y):
        if(x < y):
            return x
        else:
            return y
 
    # A memoization based function that returns size of the minimum vertex cover.
 
    @staticmethod
    def vCover(root, recursion_limit=1000):
        # The size of minimum vertex cover is zero if tree is empty or there
        # is only one node
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        
         # If recursion limit is reached, return 0
        if recursion_limit <= 0:
            return 0

        # Decrement the recursion limit
        recursion_limit -= 1
        
        # If vertex cover for this node is already evaluated, then return it
        # to save recomputation of same subproblem again.
        if root.vc != 0:
            return root.vc
        
        # print(root.data)
 
        # Calculate size of vertex cover when root is part of it
        # print("===")
        size_incl = 1 + Globals.vCover(root.left, recursion_limit) + Globals.vCover(root.right, recursion_limit)
        # Calculate size of vertex cover when root is not part of it
        size_excl = 0
        if root.left:
            size_excl += 1 + \
                Globals.vCover(root.left.left, recursion_limit) + \
                Globals.vCover(root.left.right, recursion_limit)
            # print("size excl", size_excl)
        if root.right:
            size_excl += 1 + \
                Globals.vCover(root.right.left, recursion_limit) + \
                Globals.vCover(root.right.right, recursion_limit)
            # print("size incl", size_incl)
 
        # Minimum of two values is vertex cover, store it before returning
        root.vc = Globals.min(size_incl, size_excl)
        # print("root vc", root.vc)
        return root.vc
 
    # A utility function to create a node
    @staticmethod
    def newNode(data):
        temp = node()
        temp.data = data
        temp.left = temp.right = None
        temp.vc = 0  # Set the vertex cover as 0
        return temp
 
 
if __name__ == "__main__":
    main()

