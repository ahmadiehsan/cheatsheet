from core.helpers import generate_help_text

help_data = {
    'install': {
        'description': 'install kubeadm on machine',
        'args': {
            'os': 'debianbase'
        }
    },
    'init': {
        'description': 'init kubeadm on production machine',
        'args': {
            'os': '~~debian~~ or ubuntu'
        }
    }
}

if __name__ == '__main__':
    generate_help_text(help_data)
