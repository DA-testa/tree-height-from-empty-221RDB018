# Nina Aljanaki 221RDB018
def compute_height(n, lst):    
    max_height = 0
    # Your code here
    visited = [0] * n
    level = [0] * n

    for i in range(0,n):
        if visited[i] == 0:
            visited[i] = 1
            level[i] = 1
            stack = [i]
            
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
            n = int(n)
            # print(n)
            input_t = f.readline()
            f.close()
    array = input_t.split(sep=" ")
    lst = []
    for i in array:
        lst.append(int(i))  
    print(compute_height(n, lst)) # call the function and output it's result

main()
