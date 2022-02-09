### Overview

#### Setup

Setup a ubuntu os based EC2 instance

Install docker 
```
apt install docker.io
```

Run docker, download image 
```
docker run -p 8888:8888 jupyter/pyspark-notebook:b418b67c225b
```

Open the link showed in terminal and change the IP address to Public IP
