import numpy as np

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = None

    def fit(self, X):
        # اختيار centroids random
        indices = np.random.choice(len(X), self.ncentroid, replace=False)
        self.centroids = X[indices]

        for _ in range(self.max_iter):
            # assign clusters
            distances = np.linalg.norm(X[:, None] - self.centroids, axis=2)
            labels = np.argmin(distances, axis=1)

            # update centroids
            new_centroids = []
            for i in range(self.ncentroid):
                cluster = X[labels == i]
                if len(cluster) > 0:
                    new_centroids.append(cluster.mean(axis=0))
                else:
                    new_centroids.append(self.centroids[i])
            self.centroids = np.array(new_centroids)

    def predict(self, X):
        distances = np.linalg.norm(X[:, None] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)