# nothing app

## Run and Remove
To start application you need docker host
Start command:
<sub> $ docker-compose up -d --build </sub> 

Running up will be available on docker host machine with URL:
*http://127.0.0.1:5001*

Stop application:
<sub> $ docker-compose down --rmi all </sub> 

Remove persistent volume:
<sub> $ docker volume rm nothing_pgdata </sub> 
