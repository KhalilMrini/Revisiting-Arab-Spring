from pyspark import SparkContext, SQLContext 

TAR_PATH =  'hdfs:////datasets/Spinn3r/icwsm2011/01-14-SOCIAL_MEDIA.tar.gz'


import tarfile
sc = SparkContext()
sqlc = SQLContext(sc)

# Reading the .tar.gz file
tar = sc.binaryFiles(TAR_PATH)


# Members are the components (files, folders...) found inside the compressed file
#members = tar.getmembers()
#member_count = len(members)

print tar.take(10)