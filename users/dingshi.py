from datetime import datetime
import os

import requests
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    r=requests.get("http://www.baidu.com")
    print(r.content)
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=300)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
