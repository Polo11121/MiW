import math as m
import numpy as np

def projection(u, v):
    uv = np.dot(u.T, v)
    uu = np.dot(u.T, u)

    if uu == 0:
        return u

    return (uv/uu)*u

def tabLength(u):
    return m.sqrt(np.dot(u.T, u))

a = np.array([[1, 0], [1, 1], [0, 1]])

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

    for u_x in vTab:
        u_x = np.array(u_x)
        sumProj += projection(u_x, v)

    u = v - sumProj
    uTab.append(u)
    e = (1/tabLength(u))*u
    q.append(e)

q = np.array(q).T
r = np.dot(q.T, a)

new_a = np.round(np.dot(q, r), decimals=8)

print(q, r, new_a, sep="\n")
