Frameworks/services/modules
Flask REST
Postgres
sqlalchemy 

RUN LOCALLY in dev mode
With Docker
docker build --build-arg CODECASH=`date +%s` -t csr2131/$APP .
docker run -t -p 8000:80 -v $PWD:/slideshare-backend-local --env-file=secret.env csr2131/slidegraph

Without Docker
source ./secret.sh
gunicorn [--reload] slideshare:app

DEPLOY
aws ecs update-service --cluster slidegraph-production --service slidegraph --force-new-deployment


TODO
- move gunicorn options to config file
- add "secure" option to auth cookie (need ssl cert)
- move aws credentials to directory
- update affiliations
- update password
