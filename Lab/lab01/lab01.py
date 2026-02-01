def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return int(str(n)[len(str(n)) - k - 1]) if k <= len(str(n)) else 0
""" 第一步：通过整除，去掉目标位右边的所有数字
    # 第二步：通过取余，只保留当前的最右一位
    也就是通过把目标数字放在个位的方法来解决。好处是不用判断k超出n范围，会直接得到0，不用自己处理越界的情况 """


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return a + b + c - min(a, b, c) - max(a, b, c) 


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k > 1 :
        pred = n 
        for i in range(n - k + 1 , n ):
            curr = pred  * i
            pred = curr
        result = curr
    elif k == 1 :
        result = n
    else :
        result = 1
    
    return result
""" 可以有更加简洁的循环方式，直接从n开始递减
 def falling(n, k):
    total = 1
    while k > 0:
        total *= n
        n -= 1
        k -= 1
    return total """

def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    total = 0
    if n // k :
        pred = n 
        while pred != 0 :
            curr = pred - k
            pred = curr
            print(n - curr)
            total += 1
    else :
        pass

    return total 
""" range(start, stop, step) 可以直接跳过不符合条件的数字，效率极高。 
def divisible_by_k(n, k):
    count = 0
    # 从 k 开始，每次增加 k，直到不超过 n
    for i in range(k, n + 1, k):
        print(i)
        count += 1
    return count"""

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    total = 0
    for c in str(y) :
        total +=  int(c)

    return total 
""" 纯数学迭代：% 10（取最后一位）和 // 10（去掉最后一位）。
def sum_digits(y):
    total = 0
    while y > 0:
        total += y % 10
        y //= 10
    return total """

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
        
    return False if str(n).find('88') == -1 else True 
""" def double_eights(n):
    return '88' in str(n) 
    可以用 while 循环判断 n % 100 == 88。"""
    
    
