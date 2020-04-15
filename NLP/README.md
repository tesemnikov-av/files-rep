```python
import nlp
```

pip install > /dev/null

```python

def tokenize_ru(file_text):
  tokens = word_tokenize(file_text)
  tokens = [i for i in tokens if (i not in string.punctuation)]
  tokens = [i for i in tokens if (i not in stop_words)]
  tokens = [i.replace("«", "").replace("»", "") for i in tokens]
  tokens = [ morph.parse(i)[0].normal_form for i in tokens ]
  return str(tokens).strip('[]').replace("'","").replace(",","")
  
def tokenize2_ru(file_text , tags = False):
  """
  Тэг указывают не для нормальной формы!
  """
  tokens = word_tokenize(file_text)
  tokens = [i for i in tokens if (i not in string.punctuation)]
  tokens = [i for i in tokens if (i not in stop_words)]
  tokens = [i.replace("«", "").replace("»", "") for i in tokens]
  tokens = [ morph.parse(i)[0].normal_form for i in tokens ]
  a = [ morph.parse(i)[0].tag.POS for i in tokens ] # tag.cyr_repr

  b = str(tokens).strip('[]').replace("'","").replace(",","")
  if tags == False:
    return b
  elif tags == True:
    b = b.split()
    out = []
    for i in range(0, len(a)):
      tmp = []
      tmp.append(b[i])
      tmp.append(a[i])
      out.append(list(tmp))
    return out
  else:
    raise KeyError('tags may by only boolean values')

```
