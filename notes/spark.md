```python
scala> :h?   # history

```
## Пример дерева решений

```python
# load data
val heart = sc.textFile("/Users/tesemnikov-av/Downloads/heart.csv")

# show 4 exapmle
heart.take(4).foreach(println)

# filter header
def isHeader(line: String): Boolean = line.contains("age")
val heart_2 = heart.filter(!isHeader(_))

# LabeledPoint
val data = heart_2.map { line => 
val values = line.split(',').map(_.toDouble)
val featureVector = Vectors.dense(values.init)
val label = values.last
LabeledPoint(label, featureVector)
}

# train test val split
val Array(trainData, cvData, testData) = data.randomSplit(Array(0.8, 0.1, 0.1))

# create model
val model = DecisionTree.trainClassifier(trainData, 2 , Map[Int,Int](), "gini", 4, 100)

```
