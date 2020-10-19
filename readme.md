## Apollo Gateway Service Micro Django
Finale of a journey through building a django-graphql based micro service.
The repo also explores using [ariadne](https://ariadnegraphql.org/) to build a federated schema.
This is part of a micro service architecture where 
this handles the federation using an **Apollo** gateway service.
## Tech stack
1. [Django](https://www.djangoproject.com/) for backend and business logic
2. [Ariadne](https://ariadnegraphql.org/) to resolve python/django objects to graphql API
3. [Docker](https://docs.docker.com/get-docker/) and
 [Docker compose](https://docs.docker.com/compose/) for container management and deployment.
4. [Gunicorn](https://gunicorn.org/) To serve Django in a production state
5. [Nginx](https://www.nginx.com/) To act as a reverse proxy for Gunicorn.
6. [Apollo federation](https://www.apollographql.com/docs/apollo-server/federation/introduction/) To generate a unified data graph from the federated schemas
 
## Overall Architecture.

1. [Doctors service](https://github.com/KimaruThagna/micro-django) part 1
2. [Patient's service](https://github.com/KimaruThagna/patient-microservice) part 2
3. [Diagnosis service](https://github.com/KimaruThagna/diagnosis-microservice) part 3

## Installation and running

For federation to work, all 3 services should be up and running.
Access and run all the 3 services' `docker-compose.yml` files in different terminals using the command

```bash
docker-compose up --build
```
Once all 3 services are up and running on their specific and defined ports, 
the last thing is to run the gateway. Open a new terminal window and use:

```bash
npm run start-gateway
```
Gateway will be available at http://localhost:4000



## Example queries

Now we can execute GraphQL operations as if it were implemented as a monolithic service:


```graphql

```