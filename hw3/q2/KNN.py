##### Treat this as separate script file (file name : KNN) for the model #####
class KNN(object):
    def __init__(self):
        pass

    def train(self, X, y, k):
        # Learn the training instances
        self.x_train = X
        self.y_train = y
        self.k = k

    def predict(self, x_test):
        num = x_test.shape[0]
        y_pred = np.empty_like(self.y_train)

        for i in range(num):
            L = []
            distances = np.sum(np.abs(self.x_train - x_test[i, :]), axis=1)
            min_indices = np.argsort(distances)
            for j in range(self.k):
                L.append(self.y_train[min_indices[j]])
            y_pred[i] = Counter(L).most_common(1)[0][0]
        return y_pred



##### Separate script file for model fitting ###########
import numpy as np
import KNN as KNN

knn = KNN.KNN
k = 5
knn.train(x_train, y_train, k)
y_predict = knn.predict(x_test)
print('accuracy: {}' .format(np.mean(y_predict == y_test)))
