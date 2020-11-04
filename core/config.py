import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACTIONS_DIR = os.path.join(BASE_DIR, 'actions')

EMAIL = {
    'SMTP_SERVER': 'smtp.gmail.com',
    'PORT': 465,  # For SSL
    'USERNAME': 'ehsanahmadi1374@gmail.com',
    'SENDER': 'ehsanahmadi1374@gmail.com',
}

ROCKET_CHAT = {
    'API_URL': 'https://chat.mparsict.com/api/v1/',
    'USER_ID': 'oEzJbP4LP5jMktE3Y'
}
