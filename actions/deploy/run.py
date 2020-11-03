import subprocess
import sys

from core.helpers import asset, clean_command_args

if __name__ == '__main__':
    command_args = clean_command_args(sys.argv)
    subprocess.run(['make', '-f', asset('Makefile'), *command_args])
