# pandas-rep
вектор 1
матрица 1x1
тензор 1x1x...1

np.where(x > 0, 0, 1)

```python

df["Length"]= df["Message"].str.len() 


pd.set_option('display.max_rows', 1000)

df.apply(lambda x: [1, 2], axis=1)

#replace column
data["Category"] = [1 if each == "spam" else 0 for each in data["Category"]]

df['Time'] = np.NaN


df.reset_index() # преобразовать индекс в колонку
df.index = pd.RangeIndex(start=1, stop=251, step=1)

my_series = pd.Series([5, 6, 7, 8, 9, 10])
my_series2 = pd.Series([5, 6, 10.3] , [ 'a' , 'b' , 'c' ])
print(my_series2[my_series2 > 6]*2)

df = pd.DataFrame({
'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
'population': [17.04, 143.5, 9.5, 45.5],
'square': [2724902, 17125191, 207600, 603628]
})

data[['Survived', 'Name']]
df.columns # все колонки
df.describe() # сводные данные
df.describe(include='all').transpose() # Расширенные сводные данные и транспонирование матрицы (transpose() or df.T )
df.describe(exclude='O').transpose() # exclude 'O' - exclude object data
df.corr() #  матрица корреляций


df.query('Age < 18 & Sex == "male"')
df[(df.Age < 18) & (df.Sex == "female")]

df_copy = df.copy()

#по строкам
df2.loc[2] 
#по строкам
df2['country'] 
#по строкам и столбам по индексам
df2.iloc[0:4,3:5]
#по строкам и столбам по именам
df.loc = [ [ 'raw' ] , ['col']] # если один список - то строки
df.Name # Name - имя столбца

df2.index = ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine']

#Описание Data Frame
df.shape # узнать число строк и столбцов
df.dtypes # серия с описанием типа каждой колонки
df.get_dtype_counts() # возвращает серию с числом колонок каждого из типов

df.Fare.mean() - # среднее значение в колонке

print(df['country']) # Series
print(df[['country']]) # DataFrame

fixed_df = pd.read_csv('data/bikes.csv') # or https 
df.loc[df.city == 'moscow']
df.Name[df.Name == 'Dooley, Mr. Patrick']

df.mean() # среднее значение
df.var() # дисперсия 
df.country.unique()  # Показать уникальные
df.country.nunique() # Число уникальных значений

df.query("gender == 'male'")

df.rename(columns={'writing score' : 'writing_score'})

df.query("writing_score > 88")
df.query("gender == 'male' and writing_score > 88")

df.query("gender == 'male' and writing_score > @env_write") ; # env_write = 99
df.filter(like=“Steve” , axis=0) #axis=0 для фильтра строк. Колонки по умолчанию

print(df.groupby('country').mean())
print(df.groupby('country').aggregate({ 'square' : 'mean'})

df.groupby(['Pclass' , 'SibSp']).aggregate( mean_age=pd.NamedAgg(column = 'Age' , aggfunc = 'mean') , \
                                count_age=pd.NamedAgg(column = 'Age' , aggfunc = 'count'))

data.groupby(['Sex', 'Survived'])['Survived'].count()

print(df.groupby('country' , as_index=False).agg({ 'square' : 'mean'})) # index integer
print(df.groupby(['plan','group']).agg({ 'square' : 'mean'}))

print(df.sort_values(['plan' , 'mean'] , ascending=False)) #ascending От большего к меньшему
df.sort_values(['gender', 'math_score'], ascending=[True, False]) # Один по возрастанию второй по убыванию

# Топ 1
print(df.sort_values(['plan' , 'mean'] , ascending=False).groupby('group').head(1))

# Новая колонка
df['NewName'] = df['square']*3
df = df.assign(log_mean = np.log(df.Name))

# Удалить колоку
df.drop(['square'] , axis=1) # axis=1 - указывает на колонки а не строки


set_index(‘user_id’)

# Find NA value
df.isnull().sum()
df.isna().sum()
# Заполнить NA
X.fillna({'Age': X.Age.mean()})
# Номинативные переменные в 0 и 1
X = pd.get_dummies(X)

#Обучение модели
from sklearn import tree
import pandas as pd
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf.fit(X,y)

```
NUMPY
```python
# Случайное число от 0 до 1 
np.random.sample()
0.6336371838734877
np.random.sample(3)
array([ 0.53478558,  0.1441317 ,  0.15711313])
np.random.sample((2, 3))
array([[ 0.12915769,  0.09448946,  0.58778985],
       [ 0.45488207,  0.19335243,  0.22129977]])

# Аргументы От какого числа, До какого, Сколько
np.random.randint(0, 3, 10)
array([0, 2, 0, 1, 1, 0, 2, 2, 2, 0])

np.linspace(0, 2, 9)  # 9 чисел от 0 до 2 включительно
 

>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.random.choice(a, 10, p=[0.5, 0.25, 0.25, 0, 0, 0, 0, 0, 0, 0])
array([0, 0, 0, 0, 1, 2, 0, 0, 1, 1])

np.unique(sample, return_counts=True)
unique_values, counts = np.unique(sample, return_counts=True)
```

SCIPY
```
import scipy.stats as sts
# возьмём выборку из нормального распределения
norm_rv = sts.norm(0,1) # mead, std dev
sample = norm_rv.rvs(100) # count


```

data.drop_duplicates()
data.replace(-999, np.nan)
transform = lambda x: x[:4].upper()
data.rename(index=str.title, columns=str.upper)
data.str.contains('gmail')
sns.barplot(y=subset.index, x=subset.values)

Чтобы выбрать строки, значение столбца которых равно скаляру, some_value, используйте ==:

df.loc[df['column_name'] == some_value]
Чтобы выбрать строки, чье значение столбца в итерируемом some_values, используйте isin:

df.loc[df['column_name'].isin(some_values)]
Объедините несколько условий с &:

df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]
Обратите внимание на круглые скобки. Из-за правил приоритета оператора Python & связывается более тесно, чем <= и >=. Таким образом, скобки в последнем примере необходимы. Без скобок

df['column_name'] >= A & df['column_name'] <= B
анализируется как

df['column_name'] >= (A & df['column_name']) <= B
что приводит к значению Истины Серии, является неоднозначной ошибкой.

Чтобы выбрать строки, чье значение столбца не равно some_value, используйте !=:

df.loc[df['column_name'] != some_value]
isin возвращает логический ряд, поэтому, чтобы выбрать строки, значение которых отсутствует в some_values, some_values логический ряд с помощью ~:

df.loc[~df['column_name'].isin(some_values)]
