import math
euler_const = 0.5772156649

# equation 1 in the paper
def c(n):
    if(n==0):
        return 0
    lhs = 2.0 * H(n)
    rhs = 2.0*(n-1.0)/n
    return lhs-rhs

# harmonic number approximation
def H(n):
    if n == 1.0:
        return 1.0
    else:
        return math.log(n-1) + euler_const

# algorithm 3
def PathLength(x,T,e=0):
    if T.left is None:  # is external node
        return e + c(T.size)
    a = T.SplitAtt
    if(x[a] < T.SplitValue):
        return PathLength(x, T.left, e+1)
    else:
        return PathLength(x, T.right, e+1)


def anomaly_score(x, forest, sample_size):
    average = 0.0

    for tree in forest:
        average += PathLength(x, tree)

    average = average / len(forest)
    c_value = c(sample_size)

    return 2**(-1 * (average/c_value))  # equation 2 in the paper   [  s^-(E(h(x)) / c(n))  ]



