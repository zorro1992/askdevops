### Working with AWS EMR


- Become root user on EMR master node
- Copy main.py into a file inside linux server
- Now you can run spark-submit

```
spark-submit --master yarn --deploy-mode cluster main.py
spark-submit --master yarn --deploy-mode cluster --driver-memory 8g main.py

```