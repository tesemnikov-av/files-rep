## Heart Disease UCI (Дерево решений)

![image](https://lh3.googleusercontent.com/proxy/i34MRnSxkBKPVrJQr6yHZ3S5ThkOHPIvFyJyZMYqBsAV1z4pOQbGASYe3-l8ITFU1075PLgjxP8vjrJZIqQwqlW9QbJXez8LT9WKw5IQpf0bHDqEqacIfwa1DGRMQdP0QC5daIRnm-ozeCh6ZSgBJKM7l1Y-lDkYVUa-QtQvcdNJiDNExlDlWh9NxstH_SxLfY_e8bPQ4_ogSpNmjOQxziklBjEJq6XCqw)

```scala
import org.apache.spark.mllib.evaluation.MulticlassMetrics
import org.apache.spark.mllib.tree.DecisionTree
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint

// load data
val heart = sc.textFile("/Users/tesemnikov-av/Downloads/heart.csv")

// show 4 exapmle
heart.take(4).foreach(println)

// filter header
def isHeader(line: String): Boolean = line.contains("age")
val no_header = heart.filter(!isHeader(_))

// LabeledPoint
val data = no_header.map { line => 
val values = line.split(',').map(_.toDouble)
val featureVector = Vectors.dense(values.init)
val label = values.last
LabeledPoint(label, featureVector)
}

// train test val split
val Array(trainData, cvData, testData) = data.randomSplit(Array(0.8, 0.1, 0.1))

// cache
trainData.cache()
cvData.cache()
testData.cache()

// create and fit model
val model = DecisionTree.trainClassifier(train, 2 , Map[Int,Int](), "gini", 4, 100)

// prediction
val predictionsAndLabels = test.map(example =>
    (model.predict(example.features), example.label)
)

// metrics
val metrics = new MulticlassMetrics(predictionsAndLabels)

metrics.recall(0)
metrics.precision(0)
metrics.confusionMatrix
metrics.accuracy

```

## House Prices - Advanced Regression Techniques (Пример регрессии)
![image](https://storage.googleapis.com/kaggle-competitions/kaggle/5407/media/housesbanner.png)

```scala
import org.apache.spark.mllib.tree.configuration.BoostingStrategy
import org.apache.spark.mllib.tree.GradientBoostedTrees
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.evaluation.RegressionMetrics
import org.apache.spark.mllib.linalg.Vectors

// load data
val price = sc.textFile("/Users/tesemnikov-av/Downloads/kc_house_data.csv")

// header
def isHeader(line: String): Boolean = line.contains("id")
val no_header = price.filter(!isHeader(_))

def toDouble(s: String) = {
    val tmp = s replaceAll ("\"", "")
    if ("?".equals(tmp)) Double.NaN else tmp.toDouble
}

// case class HouseData(id1: String, id2: String, 
//    features:Array[Double],price: Int)

def parse(line: String) = {
    val pieces = line.split(',')
    val id1 = pieces(0) replaceAll ("\"", "")
    val id2 = pieces(1).toString
    val price = pieces(2).toInt
    val features = Vectors.dense(pieces.slice(3, 20).map(toDouble) ) 
    
    LabeledPoint(price, features)
}

val data = no_header.map(line => parse(line))
val Array(trainData, testData) = data.randomSplit(Array(0.7, 0.3))

val boostingStrategy = BoostingStrategy.defaultParams("Regression")
boostingStrategy.numIterations = 50
boostingStrategy.treeStrategy.maxDepth = 5
boostingStrategy.treeStrategy.categoricalFeaturesInfo = Map[Int, Int]()

val model = GradientBoostedTrees.train(trainData, boostingStrategy)

val labelsAndPredictions = testData.map { point =>
  val prediction = model.predict(point.features)
  (point.label, prediction)
}

val mae_raw = labelsAndPredictions.take(10).map{ case(v, p) => (v - p).round.abs.toDouble }

def mean(xs: Iterable[Double]) = xs.sum / xs.size

mean(mae_raw)

// val regressionMetrics = new RegressionMetrics(labelsAndPredictions)
// println(s"RMSE = ${regressionMetrics.rootMeanSquaredError}")


```scala
scala> :h?   # history
scala> 'b' :: res1 # добавить b в массив res
```
