from pyspark.sql import *
from lib.logger import Log4J
from lib.utils import get_spark_app_config


if __name__ == "__main__":
    conf = get_spark_app_config()
    spark = SparkSession.builder \
            .config(conf=conf) \
            .getOrCreate()

    logger = Log4J(spark)
    logger.info("Starting the Spark Job")
    #Processing code
    conf_out = spark.sparkContext.getConf()
    logger.info(conf_out.toDebugString())
    logger.info("Ending Spark Job")
    spark.stop()