import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

import imgkit
import xlrd
from jdatetime import datetime

from core.config import EMAIL
from core.employees import EMPLOYEES
from core.helpers import asset, result, send_email, resource, jinja2_env

color_map = {
    'ضعیف': 'red',
    'نیازمند تلاش بیشتر': 'red',
    'در حد انتظار': 'green',
    'خوب': 'green',
    'عالی': 'golden',
}

if __name__ == '__main__':
    password = getpass(f'Password for {EMAIL["USERNAME"]} smtp: ')

    for employee in EMPLOYEES.actives():
        now = datetime.now()

        # get employee data resource
        workbook = xlrd.open_workbook(resource(employee.username, 'qa_report.xlsx'))
        sheet = workbook.sheet_by_index(0)

        # read from sheet
        last_col_index = sheet.ncols - 1
        last_sprint_name = sheet.cell_value(0, last_col_index)

        detail_rows = []
        for row_index in range(sheet.nrows)[2:]:
            key = sheet.cell_value(row_index, 0)
            value = sheet.cell_value(row_index, last_col_index)
            detail_rows.append(f'{key} {value}')

        # make jinja2 ready
        templates_env = jinja2_env()

        # generate certificate image
        certificate_template = templates_env.get_template('certificate.html')

        with open(asset('templates', 'temp.html'), 'w') as temp_file:
            temp_file.write(certificate_template.render(
                color=color_map[sheet.cell_value(1, last_col_index)],
                full_name=employee.full_name,
                level=sheet.cell_value(1, last_col_index),
                sprint_name=last_sprint_name,
                detail_rows=detail_rows,
                now=now.strftime("%Y/%m/%d, %H:%M"),
            ))

        image_file_name = f'{now.strftime("%Y_%B_%d")}.jpg'
        imgkit.from_file(
            asset('templates', 'temp.html'),
            result(employee.username, image_file_name),
            options={'encoding': "UTF-8", 'width': 800, 'quality': 100}
        )

        os.remove(asset('templates', 'temp.html'))

        # send email
        message = MIMEMultipart('alternative')
        message['Subject'] = 'گزارش عملکرد شما در' + ' ' + last_sprint_name
        message['From'] = EMAIL['SENDER']
        message['To'] = ', '.join(employee.emails)

        email_template = templates_env.get_template('email.html')
        message_text = MIMEText(email_template.render(sprint_name=last_sprint_name), 'html')
        message.attach(message_text)

        with open(result(employee.username, image_file_name), 'rb') as img_file:
            message_image = MIMEImage(img_file.read())
            message_image.add_header('Content-ID', '<certificate_img>')
            message.attach(message_image)

        send_email(password, employee.emails, message)
