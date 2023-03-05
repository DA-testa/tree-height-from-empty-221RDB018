# Nina Aljanaki 221RDB018
def compute_height(n, lst):    
    max_height = 0
    # Your code here
    stack = []
    visited = []
    level = []
    for j in range(0, n):
        visited.append(0)
        level.append(0)

    for i in range(0,n):
        if visited[i] == 0:
            visited[i] = 1
            level[i] = 1
            stack.append(i)
            while lst[i] != -1:
                if visited[lst[i]] == 0:
                    visited[lst[i]] = 1
                    stack.append(lst[i])
                    for j in stack:
                        level[j] += 1
                    i = lst[i]
                else:
                    for j in stack:
                        level[j] += level[lst[i]]
                    lst[i] = -1
            stack.clear()

    max_height = max(level)
    return max_height

def main():
    input_t = ""
    text_input = input()
    # implement input form keyboard and from files
    if "I" in text_input:
        n = int(input()) # input number of elements
        input_t = input() # input values in one variable, separate with space, split these values in an array
        
    # let user input file name to use, don't allow file names with letter a    
    if "F" in text_input:
        filename = input()
        if "a" in filename:
           return
        else:
            filename = "test/" + filename
            f = open(filename)
            n = f.readline()
            # print(n)
            input_t = f.readline()
            f.close()
    array = input_t.split(sep=" ")
    lst = []
    for i in array:
        lst.append(int(i))  
    print(compute_height(n, lst)) # call the function and output it's result

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
