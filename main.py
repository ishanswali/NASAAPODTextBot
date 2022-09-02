import datetime
import os
import time

import schedule

from etext import send_sms_via_email, send_mms_via_email
from getimage import retrieve, saveimage

phone_number = "518-878-4103"
provider = "T-Mobile"

# "apodtexts@gmail.com", "xhiuwqquipciyvaq"
# "tempacc1889@gmail.com", "ydwfwowovdnbizfw"

sender_credentials = ("tempacc1889@gmail.com", "ydwfwowovdnbizfw")


# send_sms_via_email(phone_number, message, provider, sender_credentials, subject="Test text message")
# send_mms_via_email(phone_number, message, file_path, mime_maintype, mime_subtype, provider, sender_credentials, subject=' ')


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
schedule.every(3).minutes.do(run)

while True:
    schedule.run_pending()
    time.sleep(1)
