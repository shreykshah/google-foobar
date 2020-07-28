def solution(s):
    # wraparound is not a problem - pattern just shifts
    # double pointer - forward pointer checking against first letter

    #input verification
    if len(s) < 1:
        return 0
    if len(s) == 1:
        return 1

    p1 = 0
    p2 = 1
    orig = 1

    while p2 < len(s):
        #move forward pointer forward until same char as back point
        while s[p1] != s[p2]:
            p2 += 1
            if p2 >= len(s):
                return 1

        #check proposed substring
        if len(s)%p2 == 0:
            orig = p2 #remember end of proposed substring
            while p2 < len(s) and s[p1] == s[p2]:
                p1 += 1
                p2 += 1
            #check value should be returned (mod for bad return "aabaaba")
            if p2 >= len(s):
                return int(len(s)/orig)

        #reset values on proposed substring fail
        p1 = 0
        p2 += 1

    return 1
