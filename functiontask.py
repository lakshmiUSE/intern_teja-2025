import subprocess
def run_command(command):
    try:
        result=subprocess.run(command,capture_output=True,text=True,check=True)
        print("command executed successfully!\n")
        print(result.stdout)
    except subprocess.CalledProcessError:
        print("Error:Command execution failed.")
    except FileNotFoundError:
        print("Error:command not found.")
    except Exception as e:
        print(f"unexpected error:{e}")
run_command(["taslkist"])