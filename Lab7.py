import math as m
import numpy as np

def m_covariance(tab):
    return np.dot(tab.T, tab)

def m_inversion(tab):
    return np.linalg.inv(tab)

def leftInversion(tab):
    cov = m_covariance(tab)
    inversion = m_inversion(cov)

    return np.dot(inversion, tab.T)

def linearRegression(tab):
    tab_x = np.array([[1, x[0]]for x in tab])
    tab_y = np.array([x[1]for x in tab])
    leftInver = leftInversion(tab_x)
    
    return np.dot(leftInver, tab_y)

xy = np.array([[2, 1], [5,2], [7, 3], [8, 3]])

print(linearRegression(xy))
