def solution(l):
    g = generate_graph(l)
    matches = reduce(g)
    return len(l) - matches

#determine if two initial banana holdings will loop
def loop(x,y):
    #loops when sum of reduced numbers (no common divisors) is pwr2
    base = int((x+y)/gcd(x,y))
    return bool(base & (base - 1))

#euclidean gcd - might have to find package
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

#create a graph with edges representing possible loops
# and vertices representing guards
def generate_graph(l):
    G = {i: [] for i in range(len(l))}
    for i in range(len(l)):
        for j in range(i, len(l)):
            if i != j and loop(l[i], l[j]):
                G[i].append(j)
                G[j].append(i)
    return G

#maximum matching
def reduce(g):
    #well known - Blossom algorithm
    #Micali-Vazirani algorithm - reduced runtime by 1000x but too long to write here
    #brute force ok because low max guards numbers

    matched = 0
    checks = len(g[max(g, key=lambda key: len(g[key]))])

    while len(g) > 1 and checks >= 1:
        #find node with min edges
        init_mw_node = min(g, key=lambda key: len(g[key]))
        #check node has edges (needed for tests with odd number guards - tests 3 and 5)
        if (len(g[init_mw_node])) < 1 :
            del g[init_mw_node]
        else:
            #find pair node with least edges
            temp_sec_min = [len(g[g[init_mw_node][0]])+1,1]
            for node_i in g[init_mw_node]:
                if len(g[node_i]) < temp_sec_min[0]:
                    temp_sec_min = [len(g[node_i]), node_i]
                #remove node from graph (remove from other node lists)
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == init_mw_node:
                        del g[node_i][check_i]
                        break
            #remove pair node from graph (remove from other node lists)
            for node_i in g[temp_sec_min[1]]:
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == temp_sec_min[1]:
                        del g[node_i][check_i]
                        break
            #remove nodes from graph
            del g[init_mw_node]
            del g[temp_sec_min[1]]
            #increment number of matches
            matched += 2
        if len(g) > 1:
            checks = len(g[max(g, key=lambda key: len(g[key]))])
    return matched
