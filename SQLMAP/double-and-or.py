#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
# 导入正则模块，用于字符的替换
import re
# sqlmap中lib\core\enums中的PRIORITY优先级函数
from lib.core.enums import PRIORITY

# 定义脚本优先级
__priority__ = PRIORITY.NORMAL


# 脚本描述函数
def dependencies():
    pass


def tamper(payload, **kwargs):
    # 将payload进行转存
    retVal = payload
    if payload:
        # 使用re.sub函数不区分大小写替换and和or
        # 替换为anandd和oorr
        retVal = re.sub(r"(?i)(or)", r"Corr", retVal)
        retVal = re.sub(r"(?i)(and)", r"anandd", retVal)
    # 把最后修改好的payload返回
    return retVal

