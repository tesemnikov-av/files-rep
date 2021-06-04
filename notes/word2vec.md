```python
import gensim.downloader as api
model = api.load("word2vec-ruscorpora-300")

import pandas as pd
pd.DataFrame(api.info())

for n in model.most_similar(positive=[u'пожар_NOUN']):
    print n[0], n[1]
пожарище_NOUN 0.618148565292
возгорание_NOUN 0.592390716076
сгорать_VERB 0.589370012283
наводнение_NOUN 0.575950324535
тушение_NOUN 0.572953224182
пожарный_NOUN 0.562128543854
поджог_NOUN 0.561940491199
сгорать::дотла_VERB 0.547737360001
поджигать_VERB 0.534844279289
незатушить_VERB 0.534272968769

# Лишнее слово
print(model.doesnt_match('яблоко_NOUN груша_NOUN виноград_NOUN банан_NOUN лимон_NOUN картофель_NOUN'.split()))
# > картофель_NOUN

print(model.most_similar(positive=['пицца_NOUN', 'россия_NOUN'], negative=['италия_NOUN'])[0][0])
# пельмень_NOUN

```
