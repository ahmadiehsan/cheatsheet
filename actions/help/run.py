from os import walk

from helpers.config import ACTIONS_DIR

if __name__ == '__main__':
    print('\n')
    print('Available Actions:')

    _, dir_names, _ = next(walk(ACTIONS_DIR))
    for dir_name in dir_names:
        print('\t', dir_name)

    print('\n')
