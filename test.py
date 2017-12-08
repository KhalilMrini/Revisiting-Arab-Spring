from pyspark import SparkContext

TWITTER_PATH =  'hdfs:////datasets/tweets-leon'

sc = SparkContext()
sample_lines_rdd = sc.textFile(TWITTER_PATH)
sample_lines_rdd.take(5)