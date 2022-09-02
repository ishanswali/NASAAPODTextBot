from etext import send_mms_via_email
from getimage import retrieve

phone_number = "518-881-7414"
message = ""
provider = "T-Mobile"

file_path = 'dino.jpg'
mime_maintype = 'image'
mime_subtype = 'jpg'

# "apodtexts@gmail.com", "xhiuwqquipciyvaq"
# "tempacc1889@gmail.com", "ydwfwowovdnbizfw"

sender_credentials = ("tempacc1889@gmail.com", "ydwfwowovdnbizfw")


# send_sms_via_email(phone_number, message, provider, sender_credentials, subject="Test text message")
#send_mms_via_email(phone_number, message, file_path, mime_maintype, mime_subtype, provider, sender_credentials, subject=' ')


apoddata = retrieve()