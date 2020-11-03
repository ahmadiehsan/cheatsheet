import os
import smtplib
import ssl
from email.mime.base import MIMEBase

from jinja2 import Environment, select_autoescape, FileSystemLoader

from core.config import EMAIL, BASE_DIR


def send_email(smtp_password, receiver_emails, message: MIMEBase):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL['SMTP_SERVER'], EMAIL['PORT'], context=context) as server:
        server.login(EMAIL['USERNAME'], smtp_password)
        server.sendmail(EMAIL['SENDER'], receiver_emails, message.as_string())


def asset(*args, **kwargs):
    if kwargs.get('from_core'):
        return os.path.join(BASE_DIR, 'core', 'assets', *args)

    action_dir = os.environ['RUNNING_ACTION_DIR']
    action_assets_dir = os.path.join(action_dir, 'assets')
    return os.path.join(action_assets_dir, *args)


def resource(*args):
    action_dir = os.environ['RUNNING_ACTION_DIR']
    action_resources_dir = os.path.join(action_dir, 'resources')
    return os.path.join(action_resources_dir, *args)


def result(*args):
    action_dir = os.environ['RUNNING_ACTION_DIR']
    action_results_dir = os.path.join(action_dir, 'results')
    return os.path.join(action_results_dir, *args)


def jinja2_env():
    env = Environment(
        loader=FileSystemLoader([
            asset('templates'),
            asset('templates', from_core=True)
        ]),
        autoescape=select_autoescape(['html', 'xml'])
    )
    env.globals['asset'] = asset
    return env
