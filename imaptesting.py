# code moved to project vtiemaildownloader
# using the schedule from scheduletest file

from imap_tools import MailBox, AND, NOT
from os import getenv
from dotenv import load_dotenv

load_dotenv()
imap_host = getenv('IMAP_HOST')
imap_user = getenv('IMAP_USER')
imap_pass = getenv('IMAP_PASS')
msg_subject = getenv('MSG_SUBJECT')
folder_save = getenv('FOLDER_SAVE')
print(imap_host)

with MailBox (imap_host).login(imap_user, imap_pass) as mailbox:
    for msg in mailbox.fetch(NOT(subject=msg_subject)):
        mailbox.move(msg.uid, 'Deleted Items')
        print(msg.date, msg.subject, len(msg.text or msg.html))
    for msg in mailbox.fetch(AND(subject=msg_subject)):
        for att in msg.attachments:
            print(att.filename, att.content_type)
            with open(folder_save+'{}'.format(att.filename), 'wb') as f:
                f.write(att.payload)
        mailbox.move(msg.uid, 'Saved')