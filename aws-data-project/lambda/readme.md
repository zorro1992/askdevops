### Creating lambda layer

Not all python package shall be present in lambda , Certain packages needs to be installed from our end too.

How to do this ?

```
mkdir lambda_layers
cd lambda_layers/
mkdir python
cd python/
pip3 install requests -t ./
ls -lrt
cd ..
ls -lrt
zip -r python_modules.zip .
```

Then use Lambda layer and upload from local system.
We can also use S3 bucket for the same.