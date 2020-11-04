from core.helpers import generate_help_text

help_data = {
    'qa': {
        'description': 'scrum quality assessment'
    },
    'points': {
        'description': 'scrum points estimation helper'
    }
}

if __name__ == '__main__':
    generate_help_text(help_data)
