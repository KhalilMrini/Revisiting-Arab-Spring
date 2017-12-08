from pyspark import SparkContext, SQLContext 

TWITTER_PATH =  'hdfs:////datasets/tweets-leon'

sc = SparkContext()
sqlc = SQLContext(sc)

schema = [
    'Language',
    'ID',
    'Date',
    'User',
    'Content'
]

def fetch_data_as_rdd(spark_context):
    return spark_context.textFile(TWITTER_PATH)

def convert_rdd_to_df(rdd):
   	return rdd.map(lambda x: x.split('\t')).toDF(schema)

sample_rdd = fetch_data_as_rdd(sc)
sample_df = convert_rdd_to_df(sample_rdd)

print('\nRDD:')
print(sample_rdd.take(5))

print('\nDF:')
sample_df.show(5)
