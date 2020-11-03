from os import walk

from core.config import ACTIONS_DIR

if __name__ == '__main__':
    print('Available Actions:')

    _, dir_names, _ = next(walk(ACTIONS_DIR))
    actions = []
    for dir_name in dir_names:
        actions.append(dir_name)

    actions.sort()
    print('\n'.join(f'\t{a}' for a in actions))

    print('Usage:')
    print('\tpython runner.py <action_name>')
