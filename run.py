import subprocess

def run_server():
   
    subprocess.run(["uvicorn", "app.main:app", "--reload"], check=True)

if __name__ == "__main__":
  
    run_server()
