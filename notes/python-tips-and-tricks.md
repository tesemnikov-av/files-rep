```python
Merging dictionaries
dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }
print (merged)
# {'a': 1, 'b': 3, 'c': 4}

#if
x = "Success!" if (y == 2) else "Failed!"

counter
print(Counter("aaaaabbbbbccccc"))
# Counter({'a': 5, 'b': 5, 'c': 5})

List Comprehensions
filtered = [i for i in range(20) if i%2==0]
print(filtered)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def get_user(id):
    # fetch user from database
    # ....
    return name, birthdate

name, birthdate = get_user(4)

Reversing strings and lists
revarray = [1, 2, 3, 4, 5][::-1]
print(revarray)
# [5, 4, 3, 2, 1]

Using map()
list_of_ints = list(map(int, "1234567")))
print(list_of_ints)
# [1, 2, 3, 4, 5, 6, 7]


Get unique elements from a list or string
print (set("aaabbbcccdddeeefff"))
# {'a', 'b', 'c', 'd', 'e', 'f'}

>>> 10 
10 
>>> _ * 3 
30 

# Ignore a value when unpacking
x, _, y = (1, 2, 3) # x = 1, y = 3 
# Ignore the multiple values. It is called "Extended Unpacking" which is available in only Python 3.x
x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5  
# Ignore the index
for _ in range(10):     
    do_something()  
# Ignore a value of specific location
for _, val in list_of_tuple:
    do_something()
    
    
    
 [[1] for _ in range(pos_texts.shape[0])] + [[0] for _ in range(neg_texts.shape[0])]
```
