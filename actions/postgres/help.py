from core.helpers import generate_help_text

help_data = {
    'install': {
        'description': 'install postgres on machine'
    },
    'create': {
        'description': 'create db and user',
        'args': {
            'db': 'database name',
            'user': 'database owner',
            'pass': "user's password"
        }
    }
}

if __name__ == '__main__':
    generate_help_text(help_data)
