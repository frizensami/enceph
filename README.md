# Deployment Instructions
1. `git clone` this repository and `cd` into it
2. Install `docker`
3. Run `docker-compose up`
4. Add the admin user by doing `docker-compose run web python manage.py createsuperuser` (you may have to hit Control-C to kill the current containers)
5. Run `docker-compose up` to start the system again (you mean want to do this inside `screen` to persist it, e.g. `screen -L -S compose` and then run `docker-compose up`, finally detaching with `Control-A D`)
    - Note that for production, this should be `DJANGO_ENV=PRODUCTION SECRET_KEY=<SECRET_KEY> docker-compose up`
    - To use sqlite: `DJANGO_DB=SQLITE docker-compose up`