def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    old_leng=len(line)
    remove(line)
    new_leng=len(line)
    for value in range(new_leng-1):
        if line[value]==line[value+1] and value+1<new_leng:
            line[value]=line[value]*2
            line[value+1]=0
    remove(line)
    last_leng=len(line)
    times=old_leng-last_leng
    for value in range(times):
        line.append(0)
    return line


def remove(line):
    #remove zerros
    leng=len(line)
    for value in range(leng):
        if 0 in line:
            line.remove(0)
    return line
print merge([2,2,4,4,4,16,16,0,0,0,0])       
