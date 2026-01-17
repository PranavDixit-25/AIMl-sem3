import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

np.random.seed(0)
X = np.random.randn(100, 2) * [5, 20] + [50, 100]
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
cov_mat = np.cov(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
idx = eig_vals.argsort()[::-1]
eig_vecs = eig_vecs[:, idx]
X_pca = X_std @ eig_vecs[:, :2]
plt.scatter(X_std[:, 0], X_std[:, 1], alpha=0.6, label="Standardized Data")
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, label="PCA Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.title("PCA on Standardized Data")
plt.show()
