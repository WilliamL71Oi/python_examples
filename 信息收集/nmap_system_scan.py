#!/usr/bin/python3
# -*- coding: utf-8 -*-

import nmap
import optparse


def NmapScan(targetIP):
	# 实例化PortScanner对象
	nm = nmap.PortScanner()
	try:
		# hosts为目标IP地址,argusments为Nmap的扫描参数(-O为进行操作系统探测)
		result = nm.scan(hosts=targetIP, arguments='-O')
		# 对结果进行切片，提取操作系统相关的信息
		os = result["scan"][targetIP]['osmatch'][0]['name']
		print("="*20)
		print("ip:{} \nos:{}".format(targetIP, os))
		print("="*20)
	except Exception  as e:
		print(e)


if __name__ == '__main__':
	parser = optparse.OptionParser('usage: python %prog -i ip \n\n'
                                    'Example: python %prog -i 192.168.1.1\n')
	# 添加目标IP参数-i
	parser.add_option('-i','--ip',dest='targetIP',default='192.168.1.1',type='string',help='target ip address')
	options,args = parser.parse_args()
	# 将IP参数传递给NmapScan函数
	NmapScan(options.targetIP)



