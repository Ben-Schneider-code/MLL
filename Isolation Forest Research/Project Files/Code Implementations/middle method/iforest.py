import math
import random
import numpy as np

alpha = 0.0

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
        Q = X.shape[1]  # the number of features
        q = random.randint(0, Q-1)  # select an attribute
        column = X[:, q]  # get the value for each point along feature q
        min_value = np.amin(column)
        max_value = np.amax(column)

        p = calc_split(min_value, max_value)

        XL,XR = filter_data(X, q, p)  # filter to get the right and left partition

        return Node(X.shape[0], iTree(XL, e+1, l), iTree(XR, e+1, l), q, p)  # left tree, right tree, split point, split value

def calc_split(min_v,max_v):
    diff = max_v - min_v
    range_value = random.uniform(-1.0*alpha, alpha)*diff
    mid = (min_v + max_v) / 2

    p = mid + range_value
    return p

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
