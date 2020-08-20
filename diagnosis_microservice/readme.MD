## Diagnosis Service Micro Django
Part 3 of a journey through building a django-graphql based micro service.
The repo also explores using [ariadne](https://ariadnegraphql.org/) to build a federated schema.
This is part of a micro service architecture where this handles the patient's service. Other services in this project are the `Patients` and `diagnosis` services.
## Tech stack
1. [Django](https://www.djangoproject.com/) for backend and business logic
2. [Ariadne](https://ariadnegraphql.org/) to resolve python/django objects to graphql API
3. [Docker](https://docs.docker.com/get-docker/) and
 [Docker compose](https://docs.docker.com/compose/) for container management and deployment.
4. [Gunicorn](https://gunicorn.org/) To serve Django in a production state
5. [Nginx](https://www.nginx.com/) To act as a reverse proxy for Gunicorn.
 
## Overall Architecture.
**Micro-django 3** is modelled as a diagnosis service app. The whole architecture involves 3 micro services
1. [Doctors service](https://github.com/KimaruThagna/micro-django) part 1
2. [Patient's service](https://github.com/KimaruThagna/patient-microservice) part 2
3. [Diagnosis service](https://github.com/KimaruThagna/diagnosis-microservice) part 3

and a final service running [apollo federation](https://www.apollographql.com/docs/apollo-server/federation/introduction/) that allows a client to access all 3 services
via a single data graph by implementing a [gateway](https://www.apollographql.com/docs/apollo-server/federation/gateway/).
The gateway service repo can be found [here](https://github.com/KimaruThagna/hospital-federated)

## Installation and running
A pre requisite to install and run this service is 
having [docker]() and [docker compose]() installed
Once installed, clone this repo into your local machine  and copy the contents of `example.env` into your own `.env` file. 
Change the variables as need be

Navigate to the position of the `docker-compose.yml` file
To spin up the service, run the command
```apex
docker-compose up
```
To access the service via the broswer, log on to [http://0.0.0.0:1337/]() since we are serving the app via NGINX

To view the app from the admin side, access the admin via the url [http://0.0.0.0:1337/admin]() and log in with the superuser credentials created in the `.env` file

## Sample Query

-`single record`

```graphql
{
  diagnosis_note(uid:"1ea4bed2-e34b-4e0e-b5a5-bdcd222cd061")
  {
    status
    object
    {
      uid
      diagnosis
      consulting_doctor{license_number}
      visiting_patient{patient_number}
    }
  }
}
```

-`multiple_records`

```graphql
{
  diagnosis_notes
  {
    status
    object
    {
      uid
      diagnosis
      consulting_doctor{license_number}
      visiting_patient{patient_number}
    }
  }
}
```
## Sample Mutation
- `createDiagnosis`
```graphql
mutation{
  createDiagnosis(creation_input:
  {    
    diagnosis:"Patient seems to be exhibiting yellow coloration. Jaundice detected"
    visiting_patient:{patient_number:"000000"}
    consulting_doctor:{license_number:"111111"}
  })
  {
    status
    object
  {
    diagnosis
  }
  }
}
```

-`updateDiagnosis`
```graphql
mutation{
  updateDiagnosis(creation_input:
  {
    uid:"aebada07-2633-4952-9786-9648638745b4"
    diagnosis:"Patient seems to be exhibiting yellow coloration. Jaundice detected"
    visiting_patient:{patient_number:"000000"}
    consulting_doctor:{license_number:"111111"}
  })
  {
    status
    object
  {
    diagnosis
  }
  }
}
```
-`archive_diagnosis`
```graphql
mutation{
 archiveDiagnosis(uid:"1ea4bed2-e34b-4e0e-b5a5-bdcd222cd061")
  {
    status
  
  }
}
```