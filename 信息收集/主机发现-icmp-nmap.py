#!/usr/bin/python3
# -*- coding: utf-8 -*-

import nmap
import optparse


def NmapScan(targetIP):
	# 实例化PortScanner对象
	nm = nmap.PortScanner()
	try:
		# hosts为目标IP地址,argusments为Nmap的扫描参数
		# -sn:使用ping进行扫描
		# -PE:使用ICMP的 echo请求包(-PP:使用timestamp请求包 -PM:netmask请求包)
		result = nm.scan(hosts=targetIP, arguments='-sn -PE')
		# 对结果进行切片，提取主机状态信息
		state = result['scan'][targetIP]['status']['state']
		print("[{}] is [{}]".format(targetIP, state))
	except Exception  as e:
		pass


if __name__ == '__main__':
	parser = optparse.OptionParser('usage: python %prog -i ip \n\n'
                                    'Example: python %prog -i 192.168.1.1[192.168.1.1-100]\n')
	# 添加目标IP参数-i
	parser.add_option('-i','--ip',dest='targetIP',default='192.168.1.1',type='string',help='target ip address')
	options,args = parser.parse_args()
	# 判断是单台主机还是多台主机
	# ip中存在-,说明是要扫描多台主机
	if '-' in options.targetIP:
		# 代码意思举例：192.168.1.1-120
		# 通过'-'进行分割，把192.168.1.1和120进行分离
		# 把192.168.1.1通过','进行分割,取最后一个数作为range函数的start,然后把120+1作为range函数的stop
		# 这样循环遍历出需要扫描的IP地址
		for i in range(int(options.targetIP.split('-')[0].split('.')[3]),int(options.targetIP.split('-')[1])+1):
			NmapScan(options.targetIP.split('.')[0] + '.' + options.targetIP.split('.')[1] + '.' + options.targetIP.split('.')[2] + '.' + str(i))
	else:
		NmapScan(options.targetIP)


