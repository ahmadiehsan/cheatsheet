import os
import subprocess
import sys

from helpers.config import ACTIONS_DIR, BASE_DIR

if __name__ == '__main__':
    os.environ['PYTHONPATH'] = BASE_DIR

    action = sys.argv[1]
    subprocess.run(['python', os.path.join(ACTIONS_DIR, action, 'run.py')])
