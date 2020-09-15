import datetime
import sys
import time
from pathlib import Path

import pytz as pytz
from mss.windows import MSS as mss

# The simplest use, save a screen shot of the 1st monitor

root = sys.argv[1] if len(sys.argv) >1 else 'cache'
interval = 60*2 if len(sys.argv) <= 2 else float(sys.argv[2])*60
while True:
    now = datetime.datetime.now(tz=pytz.timezone('Europe/Berlin'))
    if now.hour < 6:
        continue
    if now.hour > 22:
        continue
    folder = f'{root}/{now.year}-{now.month:02d}/{now.day:02d}'
    Path(folder).mkdir(parents=True, exist_ok=True)
    try:
        mss().shot(mon=1, output=f'{folder}/{now.hour:02d}_{now.minute:02d}_1.png')
    except Exception as ex:
        print(ex)
    try:
        mss().shot(mon=2, output=f'{folder}/{now.hour:02d}_{now.minute:02d}_2.png')
    except Exception as ex:
        print(ex)
    time.sleep(interval)