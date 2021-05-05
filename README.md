# docker_example

To use: Clone this repo and put your code into the services/web/project directory.

To build and run: 

If you don't have docker-compose installed, follow the instructions at this link to do so
https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9

Then, run the following commands to build and run the docker container.

```
cd services/web

source env/bin/activate

cd ../../ && docker-compose up --build -d
```

To view the logs after running the container, use docker-compose logs -f.

To stop:

docker-compose down