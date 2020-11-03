#!/usr/bin/env python

import os
import subprocess
import sys

from core.config import ACTIONS_DIR, BASE_DIR
from core.helpers import clean_command_args


def check_path(path, message):
    if not os.path.exists(path):
        print(message)
        sys.exit()


if __name__ == '__main__':
    command_args = clean_command_args(sys.argv)

    try:
        action_name = command_args.pop(0)
    except IndexError:
        print('Invalid call')
        sys.exit()

    action_dir = os.path.join(ACTIONS_DIR, action_name)
    check_path(action_dir, 'Invalid action')

    os.environ['PYTHONPATH'] = BASE_DIR
    os.environ['RUNNING_ACTION_DIR'] = action_dir

    if 'help' in command_args:
        del command_args[0]
        runner = os.path.join(action_dir, 'help.py')
        check_path(runner, 'Action not contain help command')
    else:
        runner = os.path.join(action_dir, 'run.py')
        check_path(runner, 'Invalid command')

    try:
        subprocess.run(['python', runner, *command_args])
    except KeyboardInterrupt:
        print('Process interrupted by user')
    except:
        print('Something went wrong')
