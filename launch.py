import subprocess
import threading

def launch_program(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run: {command}. Error: {e}")

if __name__ == "__main__":
    # Replace these commands with the actual programs you want to run
    commands = [
        "python autoFoot.py 1",
        "python autoFoot.py 2",
        "python autoFoot.py 3",
        "python autoFoot.py 4",
    ]

    threads = []

    for command in commands:
        thread = threading.Thread(target=launch_program, args=(command,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All programs have been launched.")
