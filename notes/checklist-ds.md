# checklist-ds

Избавление от категориальных признаков
```python
columns = [i for i in data.columns]
dummies = pd.get_dummies(data,
                         columns=columns,
                         drop_first=True,
                         sparse=True)
```
