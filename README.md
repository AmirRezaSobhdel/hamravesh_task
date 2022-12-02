## Hamravesh Task

### Keywords
Django, Celery, Docker-in-Docker, Flower


### assumptions
1. there is no information about port exposal in the tasks statement,
so I assumed that the containers are only going to execute a command and then finnish.
and are not running forever, like a django server.
If it was like this, I was going to implement a celery beat task to check the status of 
all containers (running/finished) in an interval of 1 minute.
but now, I run each ***"docker run"*** command in a celery job, and wait for it to finish in the celery job.


### Endpoints

django is running on port 8000

* auth: I have used a simple jwt based authentication system. to use the service, create a jwt token by siging up a user and set the Authorization cookie.
* ***/app/***
  - GET : get the list of all apps
  - POST : create a new app
* ***/app/<app_id>/***
  - GET : retrieve the app
  - DELETE : delete the app
  - PUT : update the app
* ***/app/<app_id>/run/***
  - GET : get the history of built containers from the app in a list
  - POST : an empty post to this endpoint, starts a new container from the app


you can see the statistics of the celery jobs on Flower in http://localhost:5555/ .