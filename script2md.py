#!/usr/bin/env python3
# This trims the HTML to just the script
# and saves it as markdown

import re
import os

from scrape import unescape
from download import EPISODE_NUMBERS

default_dir = 'scripts'

for ep in EPISODE_NUMBERS:
    ep_file = open(str(os.path.join(default_dir,ep + '.shtml')))
    raw = str(ep_file.read())
    try: 
        start = re.search(r'Episode ([0-9]*) | (82&amp;83) - ',raw).start()
    except:
        print(f"***trouble starting episode {ep}***")
    raw = raw[start:]
    end = re.search(r'(.*?)(?=</td>)',raw).end()
    raw = raw[:end]

    # Add markdown bar after cast
    raw = re.sub('===*','-------------------------------------------',raw)

    # Cleanup
    raw = raw.replace('\t','')
    raw = raw.replace('<br><br>','\n\n')
    raw = raw.replace('<br>', '')
    raw = raw.replace('&nbsp;','')
    escaped = unescape(raw)

    clean_ep_file_path = str(os.path.join(default_dir,'cleaned',ep + '.md'))
    cleaned_ep_file = open(clean_ep_file_path,'w')
    cleaned_ep_file.write(escaped)

    ep_file.close()
    cleaned_ep_file.close()
    print(f"Exported {clean_ep_file_path}")
