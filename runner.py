import os
import subprocess
import sys

from core.config import ACTIONS_DIR, BASE_DIR

if __name__ == '__main__':
    action_name = sys.argv[1]
    action_dir = os.path.join(ACTIONS_DIR, action_name)
    action_runner = os.path.join(ACTIONS_DIR, action_name, 'run.py')

    os.environ['PYTHONPATH'] = BASE_DIR
    os.environ['RUNNING_ACTION_DIR'] = action_dir

    subprocess.run(['python', action_runner])
