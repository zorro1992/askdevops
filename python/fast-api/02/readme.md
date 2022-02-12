### Setup and Overview

### Setup 

```
virtualenv venv
source venv/bin/activate
pip3 install fastapi
pip3 install "uvicorn[standard]"
deactivate
```

To run fastapi
`uvicorn main:app --reload` 

Swagger documentation 
`localhost:8000/docs`

Redoc
`localhost:8000/redoc`

