import pandas as pd
import base64
import os

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn import tree
from matplotlib import pyplot as plt


BASE_IMG_PATH = './img/'
BASE_PATH = './'

df = pd.read_csv(BASE_PATH + 'creditcard.csv')


def getSKLearnImg(rand_state=42, max_depth=3):
    fname = BASE_IMG_PATH + 'skl' + str(rand_state)  + '_' + str(max_depth) + '.png'
    if (not os.path.exists(fname)):
        X = df.drop(['Class'], axis=1)
        y = df['Class']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rand_state)
        DecsTreeModel = DecisionTreeClassifier(criterion='entropy', max_depth=max_depth)
        DecsTreeModel.fit(X_train, y_train)


        fig = plt.figure(figsize=(25, 20))
        _ = tree.plot_tree(DecsTreeModel,
                           feature_names=list(X.columns.values), class_names=['0', '1'],
                           filled=True)

        fig.savefig(fname)


    with open(fname, "rb") as image:
        img = image.read()
        barray = base64.b64encode(img).decode('utf-8')

    return barray
