import argparse
import sys, time
from datetime import datetime
sys.path.extend(['..', '.'])
from fetch import fetch, get_samples, answer
import logging as log

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('module')
    return parser.parse_args()

def get_target(YEAR, DAY, fake=False):
    epoch = datetime(1970, 1, 1)
    target = datetime(YEAR, 12, DAY, 5, 0, 0, 100)
    if fake:
        return time.time() + 10
    return (target - epoch).total_seconds()

def run(YEAR, DAY, p1_fn, p2_fn, cmds = {}):
    fake_time = "fake time" in cmds
    force = "force fetch" in cmds
    run_samples = "input only" not in cmds and "run samples" in cmds
    if run_samples:
        for fname, data in sorted(get_samples(YEAR, DAY)):
            if len(data) > 0:
                print(fname)
                print("Sample part 1: {}".format(p1_fn(data)))
                print("Sample part 2: {}".format(p2_fn(data)))
    
    target = get_target(YEAR, DAY, fake=fake_time)
    fmt_str = '%(asctime)-15s %(filename)8s:%(lineno)-3d %(message)s'
    log.basicConfig(level=log.DEBUG, format=fmt_str)
    now = time.time()
    left = target - now
    if left > 0:
        log.debug("Target: {} Now: {}".format(target, now))
        log.debug("Seconds Left: {}".format(left))
    if "samples only" in cmds:
        return
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
        





