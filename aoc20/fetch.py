import requests
from secret import session
import os, glob, time
from datetime import datetime
import bs4
import logging as log

def dl(fname, day, year):
    
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', session)
    url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
    r = requests.get(url, cookies=jar)
    if 'Puzzle inputs' in r.text:
        log.w('Session cookie expired?')
        return r.text
    if "Please don't repeatedly request this endpoint before it unlocks!" in r.text:
        log.w('Output not available yet')
        return r.text
    if r.status_code != 200:
        log.w('Not 200 as status code')
        return r.text
    with open(fname,'w') as f:
        f.write(r.text)
    return 0

def mkdirs(f):
    try:
        os.makedirs(f)
    except: pass


def fetch(year, day, log, force=False, wait_until=-1):
    filename = 'cache/{}-{}.in'.format(year, day)
    mkdirs('cache')
    exists = os.path.isfile(filename)
    if not exists or force:
        if wait_until != -1:
            to_sleep = wait_until - time.time()
            while to_sleep > 0:
                log.debug('Sleeping for {:.3f} s'.format(to_sleep))
                time.sleep(min(to_sleep, 1))
                to_sleep = wait_until - time.time()

        out = dl(filename, day, year)
        if out != 0:
            return out
    return open(filename, 'r').read().strip('\n')


def get_samples():
    samples = []
    for fname in glob.glob('*.in'):
        inp = open(fname, 'r').read().strip('\n')
        samples.append((fname, inp))
    return samples


def answer(year, day, level, res):
    print("You are about to submit {} to part {} day {}, year {}".format(res, level, day, year))
    print("Are you sure? (y)es/(n)o")
    ans = input()
    if ans == 'y' or ans == 'yes':
        print('Submitting {}'.format(answer))
        text = submit(year, day, level, res)
        if "That's the right answer!" in text:
            print('AC!')
        else:
            print('WRONG!')
        print('>> ' + text)
        return text
    else:
        print('Skipping submit')

def submit(year, day, level, result):
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', session)
    url = 'https://adventofcode.com/{}/day/{}/answer'.format(year, day)
    data = {b"answer" : (str(result)).encode('utf-8'), b'level' : str(level).encode('utf-8')}
    r = requests.post(url, data = data, cookies=jar)
    if not r.status_code == 200:
        return 'StatusCode: {}\n{}'.format(r.status_code, r.text)
    
    html = bs4.BeautifulSoup(r.text, 'html.parser')
    return html.find('article').text



def get_target(YEAR, DAY, fake=False):
    epoch = datetime(1970, 1, 1)
    target = datetime(YEAR, 12, DAY, 5, 0, 0, 100)
    if fake:
        return time.time() + 10
    return (target - epoch).total_seconds()


def run_samples(p1_fn, p2_fn):
    for fname, data in sorted(get_samples()):
        if len(data) > 0:
            print(fname)
            print("Sample part 1: {}".format(p1_fn(data)))
            print("Sample part 2: {}".format(p2_fn(data)))


def run(YEAR, DAY, p1_fn, p2_fn, cmds = {}):
    force = "force fetch" in cmds
    
    target = get_target(YEAR, DAY)
    fmt_str = '%(asctime)-15s %(filename)8s:%(lineno)-3d %(message)s'
    log.basicConfig(level=log.DEBUG, format=fmt_str)
    now = time.time()
    left = target - now
    if left > 0:
        log.debug("Target: {} Now: {}".format(target, now))
        log.debug("Seconds Left: {}".format(left))
 
    v = fetch(YEAR, DAY, log, wait_until=target, force=force)
    if "print input" in cmds:
        print(v)
    res1 = p1_fn(v)
    res2 = p2_fn(v)
    print('part_1: {}'.format(res1))
    print('part_2: {}'.format(res2))
    if 'submit1' in cmds:
        answer(YEAR, DAY, 1, res1)
        
    if 'submit2' in cmds:
        answer(YEAR, DAY, 2, res2)
        
