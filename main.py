import datetime
import os
import time

import schedule

from etext import send_sms_via_email, send_mms_via_email
from getimage import retrieve, saveimage

phone_number = "<YOUR NUMBER HERE>"
provider = "<YOUR PROVIDER HERE>"

sender_credentials = ("<YOUR EMAIL HERE>", "<YOUR APP PASSWORD HERE>")


def run():
    apoddata = retrieve()

    file_path = saveimage(apoddata)
    time.sleep(15)
    mime_maintype = apoddata['media_type']
    mime_subtype = apoddata['url'].split(".")[-1]
    message = apoddata['explanation']

    date = datetime.datetime.now()
    print(date.minute)

    send_sms_via_email(phone_number, apoddata['title'], provider, sender_credentials,
                       subject="Astronomy Picture of the Day " + "%s/%s/%s" % (date.month, date.day, date.year))
    print("Sent subject")
    time.sleep(15)

    send_mms_via_email(phone_number, "", file_path, mime_maintype, mime_subtype, provider, sender_credentials,
                       subject=' ')
    print("sent image")
    time.sleep(15)

    send_sms_via_email(phone_number, message, provider, sender_credentials, subject=" ")
    print("sent message")
    time.sleep(15)

    os.remove(file_path)
    print("DELETED IMAGE")


run()
schedule.every(24).hours.do(run)

while True:
    schedule.run_pending()
    time.sleep(1)
