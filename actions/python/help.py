from core.helpers import generate_help_text

help_data = {
    'install': {
        'description': 'install python on machine',
        'args': {
            'version': '3.9, 3.5'
        }
    },
    'virtualenv': {
        'description': 'install and create virtualenv',
        'args': {
            'path': 'absolute path for creating virtualenv',
            'version': 'version of python, ex. python3',
            'name': 'virtualenv name without any "env" prefix or suffix',
            'settings': 'relative path of project settings in python mode'
        }
    },
    'locale': {
        'description': 'fix "Python locale error: unsupported locale setting" error'
    },
}

if __name__ == '__main__':
    generate_help_text(help_data)
