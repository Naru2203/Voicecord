from sys import executable
from os import system, name
from subprocess import check_call
import time

def install():
    print('Installing Requirements Package...')
    time.sleep(1)
    python = executable
    check_call([python, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    print("Successfully Installed Requirements Package! You're Good To Go")
if __name__ == "__main__":
    install()
