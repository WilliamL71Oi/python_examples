#!/usr/bin/python3
# -*- coding: utf-8 -*-

import nmap
import optparse


def NmapScan(targetIP, targetPort):
    # 实例化PortScanner对象
    nm = nmap.PortScanner()
    try:
        # hosts为目标IP地址,argusments为Nmap的扫描参数
        # -p:对指定端口进行扫描
        result = nm.scan(hosts=targetIP, arguments='-p' + str(targetPort))
        # 对结果进行切片，提取端口信息
        # 这里需要注意的是,提取信息时需要把端口转化为int型
        port_infor = result['scan'][targetIP]['tcp'][int(targetPort)]
        # 分别显示  端口号：端口状态
        print("[{}] : [{}]".format(targetPort, port_infor['state']))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parser = optparse.OptionParser('usage: python %prog -i ip -p port\n\n'
                                   'Example: python %prog -i 192.168.1.1 -p 80,3306\n')
    # 添加目标IP参数-i
    parser.add_option('-i', '--ip', dest='targetIP', default='192.168.1.1', type='string', help='target ip address')
    # 添加扫描端口参数-p
    parser.add_option('-p', '--port', dest='targetPort', default='80', type='string', help='target port')
    options, args = parser.parse_args()
    for i in range(0, len(options.targetPort.split(','))):
        NmapScan(options.targetIP, options.targetPort.split(',')[i])

