#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

message = Mail(
    from_email='FROM_EMAIL',
    to_emails='TO_EMAIL',
    subject='Scraped Lenta Headlines',
    html_content='<strong>see attached</strong>')

with open('df_lenta.csv', 'rb') as f:
    data = f.read()
    f.close()
    
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('df_lenta.csv'),
    FileType('text/csv'),
    Disposition('attachment')
)
message.attachment = attachedFile

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

