import datetime
from urllib import request

PATH = 'images/'


def download_web_image(url):
    name = datetime.datetime.now()
    full_name = PATH + str(name) + '.jpg'
    request.urlretrieve(url, full_name)

download_web_image('http://placekitten.com/300/300/')
