from core.helpers import generate_help_text

help_data = {
    'scaffolding': {
        'description': """
        create base for project in production server, somethings like below
        
        <project>
        ├── app
        │   ├── under-construction
        │   └── <and root of other project content>
        ├── etc
        │   └── nginx
        │       └── sites-available
        └── var
            └── log
                └── <project>
        """,
        'args': {
            'project': 'project name'
        }
    }
}

if __name__ == '__main__':
    generate_help_text(help_data)
