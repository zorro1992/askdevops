from pyspark.sql import *
spark=SparkSession.builder.appName("HelloSpark").getOrCreate()
spark
df=spark.read.option('header','True').csv('s3a://brozen/data_2.csv',inferSchema=True)
df.show()
df2=df.drop('ip_address')
df2.write.csv('s3a://brozen/data_3.csv')