# machine-learning-rep

https://en.wikipedia.org/wiki/Precision_and_recall

https://craftappmobile.com/l1-и-l2-регуляризация-для-логистической-р/

http://bazhenov.me/blog/2012/07/21/classification-performance-evaluation.html

#примеры
https://www.kaggle.com/kernels

```python
import os
import pandas as pd
from sklearn import tree
import matplotlib
#from matplotlib.pyplot import plt
import seaborn as sns
%matplotlib inline

import sys
str1 = "/library/frameworks/python.framework/versions/3.7/lib/python3.7/site-packages/graphviz/"
sys.path.append(str1)

import os
os.environ["PATH"] += os.pathsep + '/library/frameworks/python.framework/versions/3.7/lib/python3.7/site-packages/graphviz/'

from IPython.display import SVG
from graphviz import Source
from IPython.display import display

from IPython.display import HTML
style="<style>svg{width: 20% !important; height: 20% !important;} </style>"
HTML(style)

X = pd.read_csv('train.csv' , sep=",")
y = X['Survived']
X = X.drop(['PassengerId' , 'Survived' , 'Name' , 'Ticket' , 'Cabin'] , axis=1)
X = pd.get_dummies(X) # категориальные признаки в количественные
X = X.fillna({'Age': X.Age.mean()})


clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf.fit(X,y)

graph = Source(tree.export_graphviz(clf, out_file = None ,
                feature_names = list(X), class_names = ['DEAD' , 'SURVIVED'] , filled = True))
display(SVG(graph.pipe(format = 'svg')))
```
Выборка из матрицы корреляции
```python
# functions for finding correlation
def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]
    
print("The Highest Correlation:" , get_top_abs_correlations(df, 1))
```

```python
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)


# матрица ошибок
from sklearn.metrics import confusion_matrix
# предсказываем на валидационном
Y_pred = model.predict(X_val)
# конвертируем предсказания в one hot
Y_pred_classes = np.argmax(Y_pred,axis = 1) 
# конвертируем валидационные проверочные в one hot
Y_true = np.argmax(Y_val,axis = 1) 
# считаем матрицу ошибок для всех
confusion_mtx = confusion_matrix(Y_true, Y_pred_classes) 
# строим ее на графике
f,ax = plt.subplots(figsize=(8, 8))
sns.heatmap(confusion_mtx, annot=True, linewidths=0.01,cmap="Greens",linecolor="gray", fmt= '.1f',ax=ax)
plt.xlabel("Предсказанный лейбл")
plt.ylabel("Истинный лейбл")
plt.title("Матрица ошибок")
plt.show()
```
![матрица ошибок](https://github.com/tesemnikov-av/files-rep/blob/master/matrix.png)

```python
fig, ax = plt.subplots(figsize=(9,5))
sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu_r")
plt.show()
```
![матрица ошибок](https://github.com/tesemnikov-av/files-rep/blob/master/na1.png)
```python
df.drop(columns=['region_2', 'taster_name', 'taster_twitter_handle', 'designation'], inplace=True)
df.dropna(inplace=True)

fig, ax = plt.subplots(figsize=(9,5))
sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu_r")
plt.show()
```
![матрица ошибок](https://github.com/tesemnikov-av/files-rep/blob/master/na2.png)
