# nothing app

## Run and Remove
To start application you need docker host. <br>

Start command: <br>
<code> $ docker-compose up -d --build </code> 

Running up will be available on docker host machine with URL: <br>
*http://127.0.0.1:5001*

Stop application: <br>
<code> $ docker-compose down --rmi all </code> 

Remove persistent volume: <br>
<code> $ docker volume rm nothing_pgdata </code> 

## Run tests
NB: for ranning tests **requests** and **pytest** must be installed on docker host. <br>
To run tests in project root directory run: <br>
<code> $ pytest -v </code>
