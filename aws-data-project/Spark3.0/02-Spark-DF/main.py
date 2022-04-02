import sys

from pyspark.sql import *
from lib.logger import Log4J
from lib.utils import get_spark_app_config,load_data_csv,transform_data_csv

if __name__ == "__main__":
    conf = get_spark_app_config()
    spark = SparkSession.builder \
        .config(conf=conf) \
        .getOrCreate()

    logger = Log4J(spark)

    if len(sys.argv) != 2:
        logger.error("Usage: main.py <filename>")
        sys.exit(-1)

    logger.info("Starting the Spark Job")

    df = load_data_csv(spark, sys.argv[1])
    df.show()
    transform_df = transform_data_csv(spark, df)
    transform_df.show()

    logger.info("Ending Spark Job")
    spark.stop()
