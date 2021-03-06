import wmi
import os
import socket

w = wmi.WMI()  # 获取电脑使用者信息
for CS in w.Win32_ComputerSystem():
    # print(CS)
    print("电脑名称: %s" % CS.Caption)
    print("使用者: %s" % CS.UserName)
    print("制造商: %s" % CS.Manufacturer)
    print("系统信息: %s" % CS.SystemFamily)
    print("工作组: %s" % CS.Workgroup)
    print("机器型号: %s" % CS.model)
    print("")
# 获取操作系统信息
for OS in w.Win32_OperatingSystem():
    # print(OS)
    print("操作系统: %s" % OS.Caption)
    print("语言版本: %s" % OS.MUILanguages)
    print("系统位数: %s" % OS.OSArchitecture)
    print("注册人: %s" % OS.RegisteredUser)
    print("系统驱动: %s" % OS.SystemDevice)
    print("系统目录: %s" % OS.SystemDirectory)
    print("")
# 获取电脑IP和MAC信息
tmplist = []
for interface in w.Win32_NetworkAdapterConfiguration(IPEnabled=1):
    tmpdict = {}
    # print(interface)
    tmpdict["Description"] = interface.Description
    tmpdict["IPAddress"] = interface.IPAddress[0]
    tmpdict["IPSubnet"] = interface.IPSubnet[0]
    tmpdict["DefaultIPGateway"] = interface.DefaultIPGateway
    tmpdict["MAC"] = interface.MACAddress
    tmpdict["DHCPServer"] = interface.DHCPServer
    tmpdict["DNSServerSearchOrder"] = interface.DNSServerSearchOrder
    tmplist.append(tmpdict)
for i in tmplist:
    print('\t' + '\t' + "网络描述：" + '\t' + i["Description"])
    print('\t' + '\t' + "MAC地址：" + '\t' + i["MAC"])
    print('\t' + '\t' + "IP地址：" + '\t\t' + i["IPAddress"])
    print('\t' + '\t' + "子网掩码：" + '\t' + i["IPSubnet"])
    print('\t' + '\t' + "默认网关：" + '\t' + str(i["DefaultIPGateway"]))
    print('\t' + '\t' + "DHCP服务器：" + '\t' + str(i["DHCPServer"]))
    print('\t' + '\t' + "DNS服务器：" + '\t' + str(i["DNSServerSearchOrder"]))
    print("")

# 获取电脑CPU信息
for processor in w.Win32_Processor():
    # print(processor)
    print("CPU型号: %s" % processor.Name.strip())
    print("CPU核数: %s" % processor.NumberOfCores)
    print("")
# 获取BIOS信息
for BIOS in w.Win32_BIOS():
    # print(BIOS)
    print("使用日期: %s" % BIOS.Description)
    print("主板型号: %s" % BIOS.SerialNumber)
    print("当前语言: %s" % BIOS.CurrentLanguage)
    print("")
# 获取内存信息
for memModule in w.Win32_PhysicalMemory():
    totalMemSize = int(memModule.Capacity)
    print("内存厂商: %s" % memModule.Manufacturer)
    print("内存型号: %s" % memModule.PartNumber)
    print("内存大小: %.2fGB" % (totalMemSize / 1024 ** 3))
    print("")
# 获取磁盘信息
for disk in w.Win32_DiskDrive():
    diskSize = int(disk.size)
    print("磁盘名称: %s" % disk.Caption)
    print("硬盘型号: %s" % disk.Model)
    print("磁盘大小: %.2fGB" % (diskSize / 1024 ** 3))
    print("")
# 获取显卡信息
for xk in w.Win32_VideoController():
    print("显卡名称: %s" % xk.name)


