import json
import shutil  # to save it locally
import urllib.request
import requests

def retrieve():
    apodurl = 'https://api.nasa.gov/planetary/apod?'
    mykey = 'api_key=hjuqO6UVlN7ntufAmcd35myyVekM7kWE0bKfuHBd'

    apodurlobj = urllib.request.urlopen(apodurl + mykey)

    apodread = apodurlobj.read()

    decodeapod = json.loads(apodread.decode('utf-8'))

    return decodeapod

def saveimage(apod):
    image_url = apod['url']

    filename = apod["title"].replace(" ", "_").replace(":", "_") + '.'+image_url.split(".")[-1]

    r = requests.get(image_url, stream=True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print("")
        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')

    return filename



# https://www.educative.io/blog/how-to-use-api-nasa-daily-image