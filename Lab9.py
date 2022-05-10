import math as m
import numpy as np

float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})

def projection(u, v):
    uv = np.dot(u.T, v)
    uu = np.dot(u.T, u)

    if uu == 0:
        return u

    return (uv/uu)*u

def tabLength(u):
    return m.sqrt(np.dot(u.T, u))

def qDecomposition(a):
    vTab = []

    for i in range(len(a[1])):
        tmp = []

        for x in a:
            tmp.append(x[i])

        vTab.append(tmp)
        tmp = []

    uTab = []
    q = []

    for v in vTab:
        v = np.array(v)
        sumProj = 0

        for u_x in uTab:
            u_x = np.array(u_x)
            sumProj += projection(u_x, v)

        u = v - sumProj
        uTab.append(u)

        if tabLength(u) == 0:
            e = u
        else:
            e = (1/tabLength(u))*u
        q.append(e)

    return np.array(q).T


def tabPlusOne(a):
    q = qDecomposition(a)
    qTa = np.dot(q.T, a)
    qTq = np.dot(qTa, q)

    return qTq


def matrixEigenvalues(a):
    newTab = a
    i = 0

    while (np.diag(newTab)-np.dot(newTab, np.ones((5, 1))).T).all() > 0.001:
        newTab = tabPlusOne(newTab)
        i = i+1

    return np.diag(newTab)

a = np.array([[1, 2, 3, 4, 5], [2, 2, 3, 4, 5], [ 3, 3, 3, 4, 5], [4, 4, 4, 4, 5], [5, 5, 5, 5, 5]])

result = matrixEigenvalues(a)
print(np.round(result, decimals=3))
