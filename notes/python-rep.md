


# python-rep

Exception


```python

dir(response) # смотрим какие методы доступны для объекта response
list( set(a) & set(b)) #пересечение множеств

help(list) - описание help

with ... as ... : 
#читать

dir(person) - посмотреть все аттрибуты

print('value a = {0} , b = {1}'.format(a,b))

#переопределить метод инициализации класса родителя
def __init__():
super().__init__()
a = 0;
вызвать метод класса родителя

3 кита ООП
полиморфизм наследование инкапсуляция



x = [ 1 , 3 , 4 ]
try:
    print(x[4])
except IndexError as err:
    print('index error' , err.args)
```

```python
isinstance(a,(float, int, str))
>>> type(a) == int

def fib(x):
    if x == 0 or x == 1 :
        return 1
    else:
        return fib(x-1) + fib(x -2)
print(fib(31))
```
Для модулей
```python
def fib(x):
    """
    Узнать число из последовательности Фибаначи по его номеру.
    """
    if x == 0 or x == 1 :
        return 1
    else:
        return fib(x-1) + fib(x -2)

print(fib.__doc__)

if __name__ == "__main__":
    print(fib(7))





a = [1,3,4,6]
list(map(lambda x: x ** 3, a))
```




s = " {who} love {city} "
print(s.template( who = "i" , city = "moscow" )

```python
d = { 'b' : 'a' , 'a':'4' }
print(d['a'])
print(d.keys())
c = {'c':'6'}
d.update(c)
print(d)

# создание списка 
x = [ i * i for i in x if i > 0 ]

a = [ 1 , 3 , 5 ]
print(a[-1]) # 5

print("ab" in "fdab") #True
print("fdab".find("ab")) #2

s = " the man walked "
print(s.startswith( "the man" , "the dog" , " dog" ))

lambda
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))

k,n = map(int, x) -> k = int(x1) , n = int(x2)

def even(x):
    if x % 2 == 0
    return true
evens =  list(filter(even, [ 1, 4 ]))
print(evens)
```
