import math
import random
import numpy as np

# weight for feature x1, x2,... xn
distribution = [0.67, .33]

summed_distrbution = []
prev = 0

for loc, i in enumerate(distribution):
    summed_distrbution.append( prev + distribution[loc])
    prev = distribution[loc]

if summed_distrbution[-1] < 1:
    print("Probability distribution must sum to 1")
    exit();

def iForest(X, t, ψ):
    Forest = []
    l = math.ceil(math.log2(ψ))

    for i in range(0,t):
        Xprime, X = sample(X,ψ)
        Forest.append(iTree(Xprime, 0, l))
    return Forest

# l is maximum depth
# e is current depth
# X is the data partition (numpy array) that this IForest node is constructed from
def iTree(X, e, l):
    if e >= l or X.shape[0] <= 1:
        return Node(X.shape[0])
    else:

        q=0
        rnd_num = random.uniform(0, 1)
        while  summed_distrbution[q] < rnd_num :
            q = q+1

        column = X[:, q]  # get the value for each point along feature q
        min_value = np.amin(column)
        max_value = np.amax(column)

        p = calc_split(min_value, max_value)

        XL,XR = filter_data(X, q, p)  # filter to get the right and left partition

        return Node(X.shape[0], iTree(XL, e+1, l), iTree(XR, e+1, l), q, p)  # left tree, right tree, split point, split value

def calc_split(min_v,max_v):
    return random.uniform(min_v, max_v)

def filter_data(X,q,p):

    XL = []
    XR = []

    for point in X:
        if point[q] < p:
            XL.append(point)
        elif point[q] > p:
            XR.append(point)
        elif len(XL) == 0:
            XL.append(point)
        else:
            XR.append(point)

    return np.array(XL), np.array(XR)  # appending to list is fast, so use list for filtering but return as np array


def sample(X, ψ):
    return X[0:ψ], X[ψ:]


class Node:
    def __init__(self, size, left=None, right=None, SplitAtt=None, SplitValue=None):
        self.size = size
        self.left = left
        self.right = right
        self.SplitAtt = SplitAtt
        self.SplitValue = SplitValue
