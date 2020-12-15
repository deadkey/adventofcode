import requests
from secret import session
import os, glob, time
from datetime import datetime
import bs4
from shutil import copyfile
import progressbar
from datetime import date

def get_day(): return date.today().day
def get_year(): return date.today().year

def dl(fname, day, year):
    
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', session)
    url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
    r = requests.get(url, cookies=jar)
    if 'Puzzle inputs' in r.text:
        print('Session cookie expired?')
        return r.text
    if "Please don't repeatedly request this endpoint before it unlocks!" in r.text:
        print('Output not available yet')
        return r.text
    if r.status_code != 200:
        print('Not 200 as status code')
        return r.text
    with open(fname,'w') as f:
        f.write(r.text)
    return 0

def wait_until(YEAR, DAY):
    target = datetime(YEAR, 12, DAY, 6, 0, 0, 100)
    now = datetime.now()
    tE = target.timestamp()
    t0 = now.timestamp()
    M = int(tE-t0) + 1
    if M <= 0: return
    widgets=[
        ' [', progressbar.CurrentTime(), '] ',
        progressbar.Bar(),
        ' (', progressbar.ETA(), ') ',
    ]
    print(f'waiting from {now} until {target}')
    bar = progressbar.ProgressBar(max_value=int(tE-t0), widgets=widgets)
    while time.time() < tE:
        cT = time.time()
        bar.update(min(M, int(cT - t0)))
        time.sleep(1)
    bar.finish()

def get_args(argv):
    FF = "force fetch"
    DB = 0
    PR = "print input"
    so = 0
    io = 0
    stats = 0
    cmds = []    
    for arg in argv[1:]:
        if arg == 'f':
           cmds.append(FF)
        if arg == 's1' or  arg == '1':
           cmds.append("submit1")
        if arg == 's2' or arg == '2':
           cmds.append("submit2")
        if arg == 'p' or arg == 'pi':
           cmds.append(PR)
        if arg == 'so':
            so = 1
        if arg == 'io':
            io = 1
        if arg == 'db':
            DB = 1
        if arg == 'st' or arg == 'stat' or arg == 'stats':
            stats = 1
        if arg == 'p1' or arg == 'part1':
            cmds.append('p1')
        if arg == 'p2' or arg == 'part2':
            cmds.append('p2')
    return cmds, stats, io, so, DB
        


def mkdirs(f):
    try:
        os.makedirs(f)
    except: pass


def fetch(YEAR, DAY, cmds):
    force = "force fetch" in cmds
    
    target = get_target(YEAR, DAY)
    fmt_str = '%(asctime)-15s %(filename)8s:%(lineno)-3d %(message)s'
    wait_until(YEAR, DAY)
    
    filename = 'real.txt'
    exists = os.path.isfile(filename)
    if not exists or force:
        
        to_sleep = target - time.time()
        while to_sleep > 0:
            print('Sleeping for {:.3f} s'.format(to_sleep))
            time.sleep(min(to_sleep, 1))
            to_sleep = target - time.time()
        
        out = dl(filename, DAY, YEAR)
        if out != 0:
            return out
    v =  open(filename, 'r').read().strip('\n')
    if "print input" in cmds:
        print(v)
    
    return  v


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
        print('Submitting {}'.format(res))
        text = submit(year, day, level, res)
        if "That's the right answer!" in text:
            print('AC!')
            if level == 1: copyfile('d{}.py'.format(day), 'd{}_part1.py'.format(day))

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


def run_samples(p1_fn, p2_fn, cmds):
    default = 'p1' not in cmds and 'p2' not in cmds
    part1 = True if 'p1' in cmds or default else False
    part2 = True if 'p2' in cmds or default else False

    for fname, data in sorted(get_samples()):
        if len(data) > 0:
            print('Running: {}'.format(fname))
            res1 = p1_fn(data) if part1 else "Skipping"
            print("Sample part 1: {}".format(res1))
            res2 = p2_fn(data) if part2 else 'Skipping'
        
            
            print("Sample part 2: {}".format(res2))
            print('##############################')

def run(YEAR, DAY, p1_fn, p2_fn, cmds = {}):
    v = fetch(YEAR,  DAY,cmds)
    default = 'p1' not in cmds and 'p2' not in cmds
    part1 = True if 'p1' in cmds or default else False
    part2 = True if 'p2' in cmds or default else False
    print('Running real input')
    
    res1 = p1_fn(v) if part1 else "Skipping"
    print('part_1: {}'.format(res1))
    res2 = p2_fn(v) if part2 else 'Skipping'
        

 
    print('part_2: {}'.format(res2))
        

    if 'submit1' in cmds and part1:
        answer(YEAR, DAY, 1, res1)
    if 'submit2' in cmds and part2:
            answer(YEAR, DAY, 2, res2)
            
