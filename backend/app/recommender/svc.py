from sklearn import svm
from sklearn.model_selection import cross_val_score


class SVC:
    def __init__(self, kernel="linear", gamma='scale', C=0.01):
        self.kernel = kernel
        self.gamma = gamma
        self.C = C

    def select(self, map, star_map):
        x = star_map[["x", "y"]]
        y = star_map["stars"]

        model = svm.SVC(kernel=self.kernel, gamma=self.gamma,
                        C=self.C)
        model.fit(x, y)

        predicted = model.predict(map[["x", "y"]])
        map["stars"] = predicted
        map = map.sort_values(by=['stars'], ascending=False)

        return map

    def score(self, data):
        x = data[["x", "y"]]
        y = data["stars"]

        model = svm.SVR(kernel=self.kernel, gamma=self.gamma, C=self.C)

        return cross_val_score(model, x, y, cv=5)
