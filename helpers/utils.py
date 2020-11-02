import inspect
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart

from helpers.config import EMAIL


def send_email(smtp_password, receiver_email, message: MIMEMultipart):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL['SMTP_SERVER'], EMAIL['PORT'], context=context) as server:
        server.login(EMAIL['USERNAME'], smtp_password)
        server.sendmail(EMAIL['SENDER'], receiver_email, message.as_string())


def asset(*args):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    caller_filename = module.__file__
    current_action_assets_dir = os.path.join(os.path.dirname(caller_filename), 'assets')
    return os.path.join(current_action_assets_dir, *args)


def results(*args):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    caller_filename = module.__file__
    current_action_results_dir = os.path.join(os.path.dirname(caller_filename), 'results')
    return os.path.join(current_action_results_dir, *args)
