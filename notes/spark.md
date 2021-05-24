```python
scala> :h?   # history
scala> 'b' :: res1 # добавить b в массив res

```
## Пример классификации (дерева решений)

```python
import org.apache.spark.mllib.evaluation.MulticlassMetrics
import org.apache.spark.mllib.tree.DecisionTree
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint

# load data
val heart = sc.textFile("/Users/tesemnikov-av/Downloads/heart.csv")

# show 4 exapmle
heart.take(4).foreach(println)

# filter header
def isHeader(line: String): Boolean = line.contains("age")
val no_header = heart.filter(!isHeader(_))

# LabeledPoint
val data = no_header.map { line => 
val values = line.split(',').map(_.toDouble)
val featureVector = Vectors.dense(values.init)
val label = values.last
LabeledPoint(label, featureVector)
}

# train test val split
val Array(trainData, cvData, testData) = data.randomSplit(Array(0.8, 0.1, 0.1))

# cache
trainData.cache()
cvData.cache()
testData.cache()

# create and fit model
val model = DecisionTree.trainClassifier(train, 2 , Map[Int,Int](), "gini", 4, 100)

# prediction
val predictionsAndLabels = test.map(example =>
    (model.predict(example.features), example.label)
)

# metrics
val metrics = new MulticlassMetrics(predictionsAndLabels)

metrics.recall(0)
metrics.precision(0)
metrics.confusionMatrix
metrics.accuracy

```

## Пример регрессии

```python

# load data
val price = sc.textFile("/Users/tesemnikov-av/Downloads/kc_house_data.csv")

# header
def isHeader(line: String): Boolean = line.contains("id")
val no_header = price.filter(!isHeader(_))

def toDouble(s: String) = {
    val tmp = s replaceAll ("\"", "")
    if ("?".equals(tmp)) Double.NaN else tmp.toDouble
}

def parse(line: String) = {
    val pieces = line.split(',')
    val id1 = pieces(0) replaceAll ("\"", "")
    val id2 = pieces(1).toString
    val price = pieces(2).toInt
    val param = pieces.slice(3, 20).map(toDouble) 
    
    (id1, id2, param, price)
}

parse(no_header.first)


