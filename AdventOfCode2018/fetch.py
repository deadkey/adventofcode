import requests
import os

def download(day):

    filename = 'data{}'.format(str(day))
    exists = os.path.isfile(filename)
    if not exists:
        jar = requests.cookies.RequestsCookieJar()
        jar.set('session', '53616c7465645f5fbf65ce2fefe8df5afe28dcce2141071956151540a5882ac43f9c40f0366528637cd5a3c0242a4f6d')
        url = "https://adventofcode.com/2018/day/{}/input".format(str(day))
        r = requests.get(url, cookies=jar)
        with open(filename,'w') as f:
            f.write(r.text)

def fetch(day):
    download(day)

    filename = 'data{}'.format(str(day))
    return open(filename, 'r').read()

def fetchlines(day):
    download(day)

    filename = 'data{}'.format(str(day))
    lines = open(filename, 'r').readlines()
    return [x.strip() for x in  lines]
