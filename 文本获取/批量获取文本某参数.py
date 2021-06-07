#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re

with open(r'C:\Users\WilliamL71Oi\Desktop\zhuce.txt', 'r', encoding='utf-8') as files:
    f = str(files.readlines())
    patterns = re.findall(r'"organizationInfoId":"(.*?)"', f, re.S)
    for pattern in patterns:
        print(pattern + '\n')
