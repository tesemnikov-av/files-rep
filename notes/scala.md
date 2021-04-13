
val rdd = sc.parallelize(Vector.range(0,99))

val v = Vector.range(0, 10)


scala dataframe
Seq((1, null), (2, "b")).toDF("number","letter")

println(s"$name is last name $surname")

def my_mean(a: Array[Int]): Float = {
    a.sum / a.size.toFloat
}

sort 
aSet.sortWith(_ < _)


EXAMPLE:
https://spark.apache.org/docs/latest/mllib-linear-methods.html#classification
https://github.com/apache/spark/blob/master/data/mllib/sample_libsvm_data.txt
https://github.com/apache/spark/blob/master/data/mllib/sample_multiclass_classification_data.txt



# DataSets vs DataFrame
scala> val data = Seq((1,2,3), (4,5,6), (6,7,8), (9,19,10))
data: Seq[(Int, Int, Int)] = List((1,2,3), (4,5,6), (6,7,8), (9,19,10))

scala> val ds = spark.createDataset(data)
ds: org.apache.spark.sql.Dataset[(Int, Int, Int)] = [_1: int, _2: int ... 1 more field]

scala> ds.show()
+---+---+---+
| _1| _2| _3|
+---+---+---+
|  1|  2|  3|
|  4|  5|  6|
|  6|  7|  8|
|  9| 19| 10|
+---+---+---+

```scala
val rawData = sc.textFile("/Users/tesemnikov-av/Downloads/heart.csv")

val header = rawData.first
val rawData2 = rawData.filter(line => line != header)

val data = rawData.map { line =>
val values = line.split(',').map(_.toDouble)
val featureVector = Vectors.dense(values.init)
val label = values.last - 1
LabeledPoint(label, featureVector)
}
```
