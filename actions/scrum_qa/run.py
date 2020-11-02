import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import imgkit
import xlrd
from jdatetime import datetime
from jinja2 import Template

from helpers.config import EMAIL
from helpers.employees import EMPLOYEES
from helpers.utils import asset, results, send_email

color_map = {
    'ضعیف': 'red',
    'در حد انتظار': 'green',
    'عالی': 'golden',
}

if __name__ == '__main__':
    password = input(f'Password for {EMAIL["USERNAME"]} smtp: ')

    for employee in EMPLOYEES.actives():
        now = datetime.now()

        # get employee data resource
        workbook = xlrd.open_workbook(results(employee.username, 'resource.xlsx'))
        sheet = workbook.sheet_by_index(0)

        # read from sheet
        last_col_index = sheet.ncols - 1
        last_sprint_name = sheet.cell_value(0, last_col_index)

        detail_rows = []
        for row_index in range(sheet.nrows)[2:]:
            key = sheet.cell_value(row_index, 0)
            value = sheet.cell_value(row_index, last_col_index)
            detail_rows.append(f'{key} {value}')

        # generate certificate image
        with open(asset('templates', 'certificate.html'), 'r') as certificate_file:
            certificate = Template(certificate_file.read())

        with open(asset('templates', 'temp.html'), 'w') as temp_file:
            temp_file.write(certificate.render(
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
            results(employee.username, image_file_name),
            options={'encoding': "UTF-8", 'width': 800, 'quality': 100}
        )

        os.remove(asset('templates', 'temp.html'))

        # send email
        message = MIMEMultipart('alternative')
        message['Subject'] = 'گزارش عملکرد شما در' + ' ' + last_sprint_name
        message['From'] = EMAIL['SENDER']
        message['To'] = employee.email

        with open(asset('templates', 'email.html'), 'r') as html_file:
            message_text = MIMEText(html_file.read(), 'html')
            message.attach(message_text)

        with open(results(employee.username, image_file_name), 'rb') as img_file:
            message_image = MIMEImage(img_file.read())
            message_image.add_header('Content-ID', '<certificate_img>')
            message.attach(message_image)

        send_email(password, employee.email, message)
