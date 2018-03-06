# Flask Postgres Docker

This setup is built for app that uses flask for backend,
postgres for the database and docker for faster deployment.

You may need to install docker locally to run the app. For installation process, (if you are using ubuntu) visit [here](https://www.sujaykundu.com/blog/2018/02/14/building-apps-with-docker.html)

Want to learn docker ? You should visit [here](https://docker-curriculum.com)

# Install docker compose

```
$ sudo pip install docker-compose
```

## Clone the app

```
$ git clone https://github.com/sujaykundu777/flask-postgres-docker.git ```
## Run the app

```
$ cd flask-postgres-docker
$ docker-compose up -e POSTGRES_PASSWORD=password
```
