import numpy as np

np.random.seed(42)

X = np.random.multivariate_normal(
    mean=[0, 0],
    cov=[[3, 1], [1, 0.5]],
    size=500
)

