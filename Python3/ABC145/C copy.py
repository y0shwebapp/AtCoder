import numpy as np
from scipy.spatial import distance
from scipy.sparse.csgraph import floyd_warshall
n = int(input())
xy = np.zeros((n, 2))
for i in range(n):
    xy[i, 0], xy[i, 1] = (int(x) for x in input().split())
print(np.sum(distance.cdist(xy, xy, metric='euclidean'))/n)