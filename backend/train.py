import pandas as pd
from sklearn import svm
from sklearn.model_selection import cross_val_score

data = pd.read_csv('train/data.csv')
x = data[['x', 'y']]
y = data['stars']

best = None
bestModel = None

for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
    for gamma in ['scale', 'auto', 0.01, 0.05, 0.1, 0.15]:
        for C in [0.01, 0.05, 0.1, 0.5, 1, 2, 5]:
            model = svm.SVC(kernel=kernel, gamma=gamma, C=C)
            score = cross_val_score(model, x, y, cv=5)
            if best is None or score.mean() > best.mean():
                best = score
                bestModel = f"SVR({kernel},{gamma},{C})"


print(best.mean())
print(bestModel)
