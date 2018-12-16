# Deployment Instructions
1. `git clone` this repository and `cd` into it
2. Install `docker`
3. Run `docker-compose up`
4. Add the admin user by doing `docker-compose run web python manage.py createsuperuser` (you may have to hit Control-C to kill the current containers)
5. Run `docker-compose up` to start the system again (you mean want to do this inside `screen` to persist it)