def solution(g):
    #columns rather than rows for efficiency
    transposed = tuple(zip(*g))
    #generate first column's preimages
    preimgs = precol(transposed[0])

    #initialize first pair end values to 1
    precount = dict()
    for pair in preimgs:
        precount[pair[0]] = 1

    #loop through, adding the ways to get to the first value in the pair in the
    #previous iteration to the location of the second value in the pair for the
    #current iteration
    for col in transposed:
        #generate preimage
        preimgs = precol(col)
        count = dict()
        for pair in preimgs:
            #check all values initialized
            if pair[0] not in precount: precount[pair[0]] = 0
            if pair[1] not in count: count[pair[1]] = 0
            #check left side of next column with right side of previous column
            #by adding prev iter left number sum to curr iter right number sum
            count[pair[1]] += precount[pair[0]]
        #reset prev for next iteration
        precount = count

    return sum(precount.values())


#generate first column's preimages
def precol(col):
    possib = ((0, 0), (0, 1), (1, 0), (1, 1))
    curr = devol[col[0]]
    for i in range(1, len(col)):
        new = []
        for tes in curr:
            for comb in possib:
                if evol[(tes[i], comb)] == col[i]:
                    new.append(tes+(comb,))
        curr = tuple(new)
    bin_ret = [tuple(zip(*i)) for i in curr]
    #convert to decimal pair
    return [tuple([bitlist(nu) for nu in possibl]) for possibl in bin_ret]

#convert list of bits to integer
def bitlist(bitsl):
    out = 0
    for bit in bitsl:
        out = (out << 1) | bit
    return out

#base matrices for evolution/devolution
evol = {((0, 0), (0, 0)): 0, ((0, 0), (0, 1)): 1, ((0, 0), (1, 0)): 1,
        ((0, 0), (1, 1)): 0, ((0, 1), (0, 0)): 1, ((0, 1), (0, 1)): 0,
        ((0, 1), (1, 0)): 0, ((0, 1), (1, 1)): 0, ((1, 0), (0, 0)): 1,
        ((1, 0), (0, 1)): 0, ((1, 0), (1, 0)): 0, ((1, 0), (1, 1)): 0,
        ((1, 1), (0, 0)): 0, ((1, 1), (0, 1)): 0, ((1, 1), (1, 0)): 0, ((1, 1), (1, 1)): 0}
devol = {0: (((0, 0), (0, 0)), ((0, 0), (1, 1)), ((0, 1), (0, 1)), ((0, 1), (1, 0)),
             ((0, 1), (1, 1)), ((1, 0), (0, 1)), ((1, 0), (1, 0)), ((1, 0), (1, 1)),
             ((1, 1), (0, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 0)), ((1, 1), (1, 1))),
         1: (((1, 0), (0, 0)), ((0, 1), (0, 0)), ((0, 0), (1, 0)), ((0, 0), (0, 1)))}
