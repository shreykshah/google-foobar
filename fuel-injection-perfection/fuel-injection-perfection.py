def solution(n):
    #input will be positive integer given as a String
    n = int(n)
    #counter for num steps taken
    i = 0
    while n > 1:
        #if even, bitshift down (divide by 2)
        if (n&1) == 0:
            n >>= 1
        #if last 2 bits are '01', subtraction is better (edgcase:3)
        elif (n&3) == 1 or n == 3:
            n -= 1
        #if last 2 bits are '11', addition is better
        else:
            n += 1
        i += 1
    return i
