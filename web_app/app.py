import subprocess 
from src import create_app

# wait for db to be ready
subprocess.run(['sh', './web_app/wait_for_db.sh'])

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
