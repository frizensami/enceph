# Deployment Instructions
1. `git clone` this repository and `cd` into it
2. Install `docker`
3. Run `docker-compose up`
4. Add the admin user by doing `docker-compose run web python manage.py createsuperuser` (you may have to hit Control-C to kill the current containers)
5. Run `docker-compose up` to start the system again (you mean want to do this inside `screen` to persist it, e.g. `screen -L -S compose` and then run `docker-compose up`, finally detaching with `Control-A D`)
    - Note that for production, this should be `WEB_EXTERNAL_PORT=80 DJANGO_ENV=PRODUCTION SECRET_KEY=<SECRET_KEY> docker-compose up` (or the port should be 443 if using HTTPS)
    - To use sqlite: `DJANGO_DB=SQLITE docker-compose up`
6. Set up firewall to disable connections on port 8000

## HTTPS Setup
1. Follow instruction at https://certbot.eff.org/lets-encrypt/ubuntubionic-other to authorize the domain
2. Setup nginx's production config to server the files (look at the repos for an example)
3. Deny requests to port 8000 through the firewall (ufw in our case)

## Notes
- node_modules is checked in because of some problem with gulp/semantic together. 
