```python
# Среднее значение
# заменить на lambda
def arithmetical_mean(array):
    sum = 0
    for obj in array:
        sum += obj
    return sum/len(array)

# Размах
def scope(a,b):
    return b - a
list = { 5, 8 }
list2 = { 12 , 34 }
map(lambda a,b: b - a, list, list2)

# Дисперсия
def dispersion(array):
    sum = 0
    mean = arithmetical_mean(array)
    for obj in array:
        sum += (obj - mean)**2
    return sum / (len(array)-1) # Для выборки
    # return sum / len(array)   # Для генеральной совокупности

# Среднеквадратичное (стандартное) отклонение
def standard_deviation(array):
    return dispersion(array)**0.5

# Требуется проверить
# Стандартизация или z-преобразование # доделать
def standardization(array):
    mean = arithmetical_mean(array)
    std_dev = standard_deviation(array)
    std = []
    for obj in array:
        std.append((obj-mean)/std_dev)
    return std

# Стандартная ошибка
def standard_error(standard_deviation, number_of_observations):
    return standard_deviation / (number_of_observations)**0.5

# Доверительный интервал
print(standard_error(5 , 100))
def confidence_interval(arithmetical_mean, standard_error):
#   95%  доверительный интервал
#    return [ (arithmetical_mean - (1.96 * standard_error) ) , (arithmetical_mean + (1.96 * standard_error) ) ]
#   99% доверительный интервал
    return [ (arithmetical_mean - (2.58 * standard_error) ) , (arithmetical_mean + (2.58 * standard_error) ) ]

# Расстояни Хи Квадрат
from scipy.stats import chisquare
b=chisquare([18, 55, 27], f_exp=[25, 50, 25])
print (b)
```

Гомоскедатичность



