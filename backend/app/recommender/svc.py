from sklearn import svm


class SVC:
    def __init__(self, kernel="rbf", gamma=0.05, C=1):
        self.kernel = kernel
        self.gamma = gamma
        self.C = C

    def select(self, map, star_map):
        x = star_map[["x", "y"]]
        y = star_map["stars"]

        model = svm.SVR(kernel=self.kernel, gamma=self.gamma,
                        C=self.C)
        model.fit(x, y)

        predicted = model.predict(map[["x", "y"]])
        print(predicted)
        map["stars"] = predicted
        map = map.sort_values(by=['stars'], ascending=False)

        return map
