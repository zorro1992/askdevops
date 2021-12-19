## Guide to start python and connect to vs code.

- Run the docker build command to build the image
- This should mount your current working dir to /work inside the docker container.


```
docker build --target dev . -t python
docker run -it -v ${PWD}:/work python sh
```

Inside the container 

```
/work # python --version
Python 3.9.
```