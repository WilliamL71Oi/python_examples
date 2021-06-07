#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    retVal = payload
    if payload:
		# 把count(*)替换为count(1)
        retVal = re.sub(r"(?i)count\(\*\)", r"count(1)", payload)

    return retVal

