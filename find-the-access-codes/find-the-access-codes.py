def solution(l):
    # no sorting
    trips = 0
    doubs = [0]*len(l)

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                doubs[i] += 1
                trips += doubs[j]
    return trips

    #code will multicount repeated numbers
    #ex. [1,1,2,4] will return 4 ([1,1,2],[1,1,4],[1,2,4],[1,2,4])
    #    multicount of [1,2,4] due to repeating number (two 1s)
