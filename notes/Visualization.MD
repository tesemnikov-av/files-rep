# visualization-rep

https://www.kaggle.com/vanshjatana/a-simple-tutorial-to-data-visualization/data#Cat-Plot


```python
#SEABORN

# палитра
from matplotlib import pyplot as plt
import seaborn as sb
current_palette = sb.color_palette()
sb.palplot(sb.color_palette("Greens"))
plt.show()

# обрезать ось х
sns.distplot(amount_val, ax=ax[0], color='r')
ax[0].set_title('Distribution of Transaction Amount', fontsize=14)
ax[0].set_xlim([min(amount_val), max(amount_val)])



# Гистограмма
df.Age.hist() гистограмма для одной переменной
df.plot() линяя для одной переменной через Pandas
plt.plot(df.index, df.income)линяя для одной переменной через  ьфездщедши


data['Age'].hist(density=True) # density=True выведет долю, а не количество


# Диаграмма рассеяния - корелляция между переменными
#(точечная диаграмма, англ. scatter plot)
df.plot.scatter(x='writing_score' , y='reading_score')

gr = sns.lmplot(x='writing_score' , y='reading_score' , data=df , hue='gender' , fit_reg=False ) # seaborn ; hue -  группировать по; fit_reg - убрать регрессионные прямые ; gr.set_xlabels('Math 





```
https://m.habr.com/ru/post/468295/

КОГОРТА
http://www.gregreda.com/2015/08/23/cohort-analysis-with-python/


```python
# Построить два графика по Survived 
g = sns.FacetGrid(train_df, col='Survived')
g.map(plt.hist, 'Age', bins=20)
```
![Титаник Возраст](https://github.com/tesemnikov-av/files-rep/blob/master/survived_graph.png)

```python
# grid = sns.FacetGrid(train_df, col='Pclass', hue='Survived')
grid = sns.FacetGrid(train_df, col='Survived', row='Pclass', size=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend();
```
![Титаник Класс Каюты](https://github.com/tesemnikov-av/files-rep/blob/master/pclass.png)


```python
# и вот не средние, а просто значения длительности для каждого возраста, но цветом покажем, кто согласился на депозит, а кто нет
df['y'] = df['y'].replace(to_replace=['no', 'yes'], value=[0,1])
df.plot.scatter(x='age', y='duration', c='y', colormap='viridis', alpha=0.5, figsize=(16,9)) # c => color
# colormap - название цветовой темы
# alpha - прозрачность
# figsize - размер полотна
# смотрите, здесь жёлтые это yes, а фиолетовые это no
# кажется, что фиолетовые четко выстилают дно этого графика
```
![Титаник Согласие](https://github.com/tesemnikov-av/files-rep/blob/master/Unknown1.png)

```python
# histogram with Seaborn

fig, ax = plt.subplots(figsize = (9,4))
ax.set_title('Возраст')
ax.set(ylabel='Частота')
ax = sns.distplot(df['age'], color = 'green')
```
![Титаник Age](https://github.com/tesemnikov-av/files-rep/blob/master/age.png)

```python
# Гистограмма CTR
import seaborn as sns
fig, ax = plt.subplots(figsize = (9,4))
ax.set_title('Гистограмма CTR')
ax.set(ylabel='Частота')
ax = sns.distplot(df.loc[df['id_adv'] == 1]['CTR'], color = 'red')
ax = sns.distplot(df.loc[df['id_adv'] == 2]['CTR'], color = 'green')
ax = sns.distplot(df.loc[df['id_adv'] == 3]['CTR'], color = 'blue')
ax = sns.distplot(df.loc[df['id_adv'] == 4]['CTR'], color = 'gray')
ax = sns.distplot(df.loc[df['id_adv'] == 5]['CTR'], color = 'yellow')
```
![Титаник CTR](https://github.com/tesemnikov-av/files-rep/blob/master/CTR.png)

```python
# Взаимосвязь CTR и CPM для каждого объявления
df['COLOR'] = df['id_adv']
df.plot.scatter(y='CTR', x='CPM', c='COLOR', colormap='viridis', alpha=0.5, figsize=(16,9))
```
![Титаник CTR](https://github.com/tesemnikov-av/files-rep/blob/master/CTR_CPM.png)

```python
# correlation map data.corr()
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()
```
![correlation map](https://github.com/tesemnikov-av/files-rep/blob/master/data_corr.png)


```python
# Set the style of plots
plt.style.use('fivethirtyeight')

# Plot the distribution of ages in years
plt.hist(app_train['DAYS_BIRTH'] / 365, edgecolor = 'k', bins = 25)
plt.title('Age of Client'); plt.xlabel('Age (years)'); plt.ylabel('Count');
```
![age of client](https://github.com/tesemnikov-av/files-rep/blob/master/age_of_client.png)

```python
plt.figure(figsize = (10, 8))

# KDE plot of loans that were repaid on time
sns.kdeplot(app_train.loc[app_train['TARGET'] == 0, 'DAYS_BIRTH'] / 365, label = 'target == 0')

# KDE plot of loans which were not repaid on time
sns.kdeplot(app_train.loc[app_train['TARGET'] == 1, 'DAYS_BIRTH'] / 365, label = 'target == 1')

# Labeling of plot
plt.xlabel('Age (years)'); plt.ylabel('Density'); plt.title('Distribution of Ages');
```
![distribution](https://github.com/tesemnikov-av/files-rep/blob/master/distribution.png)

```python
plt.figure(figsize = (8, 8))

# Graph the age bins and the average of the target as a bar plot
plt.bar(age_groups.index.astype(str), 100 * age_groups['TARGET'])

# Plot labeling
plt.xticks(rotation = 75); plt.xlabel('Age Group (years)'); plt.ylabel('Failure to Repay (%)')
plt.title('Failure to Repay by Age Group');
```
![age group](https://github.com/tesemnikov-av/files-rep/blob/master/age_group.png)

```python
# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4,8]), :]

# Each line in its own column
sns.set_style("white")
gridobj = sns.lmplot(x="displ", y="hwy", 
                     data=df_select, 
                     height=7, 
                     robust=True, 
                     palette='Set1', 
                     col="cyl",
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.show()
```
![age group](https://github.com/tesemnikov-av/files-rep/blob/master/cyl)

```python
# Постройте график зависимости средней велчины звонка от возраста
pd.DataFrame(df.groupby(['age'])['duration'].mean()).plot()
df.groupby(['age'])['duration'].mean().plot.bar(figsize=(16,9))
df.query("id_adv == 1").groupby(['date'])['CTR'].sum().plot.bar(figsize=(10,6))
```



PIE 1
```python
import pandas as pd
%matplotlib inline
df = pd.DataFrame([8,8,1,2], index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot(kind='pie', subplots=True, figsize=(8, 8))
```
![pie1](https://github.com/tesemnikov-av/files-rep/blob/master/pie1)

PIE 2
```python

import matplotlib.pyplot as plt

# Pie chart
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
# only "explode" the 2nd slice (i.e. 'Hogs')
explode = (0, 0.1, 0, 0)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()
```
![pie2](https://github.com/tesemnikov-av/files-rep/blob/master/pie2)

PIE3

```python
labels = ['Female', 'Male']
size = data['Gender'].value_counts()
colors = ['lightgreen', 'orange']
explode = [0, 0.1]

plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(size, colors = colors, explode = explode, labels = labels, shadow = True, autopct = '%.2f%%')
plt.title('Gender', fontsize = 20)
plt.axis('off')
plt.legend()
plt.show()
```
![Distr](https://github.com/tesemnikov-av/files-rep/blob/master/__results___13_0.png)




```python
plt.rcParams['figure.figsize'] = (15, 8)
sns.countplot(data['Age'], palette = 'hsv')
plt.title('Distribution of Age', fontsize = 20)
plt.show()
```
![Distr](https://github.com/tesemnikov-av/files-rep/blob/master/__results___15_0.png)


```python
sns.jointplot(df["доход"], df["возраст"], kind='kde')
```


![Distr](https://github.com/tesemnikov-av/files-rep/blob/master/Unknown-2.png)

```python
# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')
 
# Custom the histogram and add rug:
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='hex', marginal_kws=dict(bins=30, rug=True))

```
![Distr](https://github.com/tesemnikov-av/files-rep/blob/master/82_seaborn_jointplot6.png)

```python

import plotly.graph_objects as go
import urllib, json

url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())
fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label']
  ))])

fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                  font_size=10)
fig.show()
```

![Distr](https://github.com/tesemnikov-av/files-rep/blob/master/notnull.png)


# много картинок аля хитмэп
sns.pairplot(training)



https://blog.algorexhealth.com/2018/03/almost-10-pie-charts-in-10-python-libraries/

Код для разных графиков
https://python-graph-gallery.com/292-choropleth-map-with-folium/

Поиск типа графиков в зависимости от данных
https://www.data-to-viz.com


Заливка fill
```python
import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Fills and Alpha Example")
plt.show()
```

HEATMAP ISNULL
```python
fig, ax = plt.subplots(figsize=(9,5))
sns.heatmap(train.isnull(), cbar=True, cmap="YlGnBu_r")
plt.show()
```
PROGRESS BAR
```python
from tqdm import trange
import time
for i in trange(100):
    time.sleep(0.01)
```


```
#https://www.kaggle.com/shahules/complete-eda-baseline-model-0-708-lb

stopwords = set(STOPWORDS)

def show_wordcloud(data, title = None,ax=None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=100,
        max_font_size=30, 
        scale=3,
        random_state=1 
        )
    
    wordcloud=wordcloud.generate(str(data))
    ax.imshow(wordcloud,interpolation='nearest')
    ax.axis('off')
    #plt.show()
    
fig,ax=plt.subplots(1,3,figsize=(20,12))

for i in range(3):
    new=df[df['sentiment']==sent[i]]['text']
    show_wordcloud(new,ax=ax[i])
    ax[i].set_title(sent[i],color=colors[i])
```


```
from termcolor import colored
print("ddfdf",colored('hello', 'blue'), colored('world', 'green'))
print(colored('Hello, World!', 'red', attrs=['reverse', 'blink']))
```
