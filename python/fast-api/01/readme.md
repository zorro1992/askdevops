### Setup and Overview

### Setup 

```
virtualenv venv
source venv/bin/activate
pip3 install "uvicorn[standard]"
deactivate
```

To run fastapi
`uvicorn main:app --reload` 