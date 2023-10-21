# Simple Flask API with GET, POST, PUT methods

## Usage

1. Clone repository with ```git clone https://github.com/CHRNVpy/FlaskDev.git```
2. Navigate to app directory with ```cd app```
3. Run ```docker compose up```. This will build both Mongo and Flask_app images and run container
4. Once container is running you can send requests to ```http:localhost:8080/api``` 

**Example Request Body for GET, POST:**

```markdown
{
  "key": "name",
  "value": "Anton"
}
```

**Example Request Body for PUT:**

```markdown
{
  "key": "name",
  "value": "Anton",
  "new_value": "Max"
}
```