# CONTRIBUTING

## How to run the Dockerfile locally

```
docker run -dp 5006:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run"
```