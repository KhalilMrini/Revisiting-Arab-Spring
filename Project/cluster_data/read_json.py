from pyspark import SparkContext, SQLContext 

SPINNER_JSON_PATH =  'hdfs:////datasets/Spinn3r/spinn3r.json'

sc = SparkContext()
sqlContext = SQLContext(sc)


#Try to read directly json file:
#json_rdd = sc.textFile(SPINNER_JSON_PATH)

#print('\nRDD:')
#print(json_rdd.take(5))

df = sqlContext.read.json(SPINNER_JSON_PATH)

print('\nDF:')
df.show(100)
