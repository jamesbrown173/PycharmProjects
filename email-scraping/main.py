import mailbox
import csv

mbox_file_path = '/Users/jamesbrown/Downloads/Takeout/Mail/all_mail.mbox'
csv_file_path = '/Users/jamesbrown/Downloads/Takeout/Mail/new.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['From', 'To', 'Subject', 'Date', 'Body'])

    mbox = mailbox.mbox(mbox_file_path)

    for message in mbox:
        from_address = message['From']
        to_address = message['To']
        subject = message['Subject']
        date = message['Date']
        body = message.get_payload()

        csv_writer.writerow([from_address, to_address, subject, date, body])
