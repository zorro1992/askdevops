import configparser

from pyspark import SparkConf


def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for (key, val) in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key, val)
    return spark_conf


def load_data_csv(spark, data_file):
    return spark.read \
        .option("header", "true") \
        .option("interSchema", "true") \
        .csv(data_file)


def transform_data_csv(spark, df):
    transform_df = df.where("Age < 40") \
        .select("Age", "Gender", "Country", "state")
    return transform_df
