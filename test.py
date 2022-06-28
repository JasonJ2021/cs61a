def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if(n < 0):
        return 0
    if(n == 0 ):
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if(n < 0):
        return 0 
    if(n == 0):
        return 1
    result = 0
    if(k < 0):
        print("ERROR!")
    for i in range(1,k + 1):
        result += count_k(n-i , k)
    return result

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return  [s[i]*i for i in range(len(s)) if i % 2 == 0]

def mult(list):
    result = 1
    for i in list:
        result *= i
    return result

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    list = [[s[j:len(s):i] for j in range(0 , len(s)) if j + i <len(s)] for i in range(2,len(s))] 
    result = 0
    # for i in range(len(list)):
    #     print(list[])
    if(len(list) == 0) :
        return 1
    for i in range(len(list)):
        for j in range(len(list[i])):
            result = max(result , mult(list[i][j]))
    
    return result
