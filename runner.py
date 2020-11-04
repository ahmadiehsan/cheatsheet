#!/usr/bin/env python

import os
import subprocess
import sys

from core.config import ACTIONS_DIR, BASE_DIR
from core.helpers import clean_command_args


def check_path(path, message='Path is not exist', terminate=True):
    if not os.path.exists(path):
        if not terminate:
            return False

        print(message)
        sys.exit()

    return True


if __name__ == '__main__':
    command_args = clean_command_args(sys.argv)

    try:
        action_name = command_args.pop(0)
    except IndexError:
        print('Invalid call')
        sys.exit()

    action_dir = os.path.join(ACTIONS_DIR, action_name)
    check_path(action_dir, message='Invalid action')

    os.environ['PYTHONPATH'] = BASE_DIR
    os.environ['RUNNING_ACTION_DIR'] = action_dir

    if 'help' in command_args:
        run = os.path.join(action_dir, 'help.py')
        check_path(run, message='Action not contain help command')
    else:
        run = os.path.join(action_dir, 'run.py')

        if not check_path(run, terminate=False):
            run = os.path.join(action_dir, f'{command_args[0]}.py')
            check_path(run, message='Invalid command')

    try:
        subprocess.run(['python', run, *command_args])
    except KeyboardInterrupt:
        print('Process interrupted by user')
    except:
        print('Something went wrong')
