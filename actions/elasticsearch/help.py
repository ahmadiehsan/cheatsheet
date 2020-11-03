from core.helpers import generate_help_text

help_data = {
    'install': {
        'description': 'install elasticsearch 2 on machine',
        'args': {
            'os': 'debian, ubuntu'
        }
    }
}

if __name__ == '__main__':
    generate_help_text(help_data)
