
# Python version 3.12.6

## Build the container

docker build build -t fastapi .


## Run the container

docker-compose up -d


### Extras

Enable production mode by commenting out the 'command'

``` 
services:
  fastapi:
    image: fastapi:latest
    ports:
      - 8000:8000
    # Uncomment the line below to run fastAPI in DEV mode.
    command: ["fastapi","dev", "main.py","--host" ,"0.0.0.0", "--port", "8000" ]
    volumes:
      - ./src:/app
  
```
