import sys
import threading
import numpy
def compute_height(n, parents):
    # Write this function
    max_height=0
    child_to_parent = {}
    # create a dictionary of the parents and their children
    for i in range(len(parents)):
        if parents[i] not in child_to_parent:
            child_to_parent[parents[i]] = [i]
        else:
            child_to_parent[parents[i]].append(i)
    # recursively look through the dictionary to find the longest path
    def find_height(parent):
        if parent not in child_to_parent:
            return 0
        else:
            max_height_current = 0
            for child in child_to_parent[parent]:
                max_height_current = max(max_height_current, find_height(child))
            return 1 + max_height_current
    return find_height(-1)

def main():
    # implement input form keyboard and from files
    
    file_name = input("Please enter a file name (no 'a'): ")
    while 'a' in file_name:
        file_name = input("Please enter a valid file name (no 'a'): ")
    # input number of elements
    n = int(input("Please enter the number of elements: "))
    # input values in one variable, separate with space, split these values in an array
    parents_str = input("Please enter the values in one variable, separated by spaces: ")
    parents_arr = [int(x) for x in parents_str.split(" ")]
    # call the function and output it's result
    result = compute_height(n, parents_arr)
    print("The height of the tree is:", result)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# # python3

# import sys
# import threading
# import numpy


# def compute_height(n, parents):
#     # Write this function
#     max_height = 0
#     # Your code here
#     return max_height


# def main():
#     # implement input form keyboard and from files
    
#     # let user input file name to use, don't allow file names with letter a
#     # account for github input inprecision
    
#     # input number of elements
#     # input values in one variable, separate with space, split these values in an array
#     # call the function and output it's result
#     pass

# # In Python, the default limit on recursion depth is rather low,
# # so raise it here for this problem. Note that to take advantage
# # of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
# main()
# # print(numpy.array([1,2,3]))
