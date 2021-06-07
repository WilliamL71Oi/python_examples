# -*- coding:utf-8 -*-
# pip install python-whois
import whois

data = whois.whois('qianxin.com')
print(data)
print("域名：" + str(data.domain_name) +'\n')
print("注册商：" + str(data.registrar) +'\n')
print("域名服务器：" + str(data.whois_server) +'\n')
print("传送URL：" + str(data.referral_url) +'\n')
print("更新时间：" + str(data.updated_date) + '\n')
print("创建时间：" + str(data.creation_date) + '\n')
print("过期时间：" + str(data.expiration_date) + '\n')
print("DNS：" + str(data.name_servers) + '\n')
print("状态：" + str(data.status) + '\n')
print("邮箱：" + str(data.emails) + '\n')
print("DNSSEC：" + str(data.dnssec) + '\n')
print("名字：" + str(data.name) + '\n')
print("组织：" + str(data.org) + '\n')
print("地址：" + str(data.address) + '\n')
print("城市：" + str(data.city) + '\n')
print("区域：" + str(data.state) + '\n')
print("邮编：" + str(data.zipcode) + '\n')
print("国家：" + str(data.country) + '\n')




'''
# whois查询
def whoisSearch():
    textIpDomainR.delete('0.0', 'end')
    data = whois(whoisEn.get())
    textIpDomainR.insert(INSERT, whoisEn.get() + " 的WHOIS查询结果为：" + '\n\n')
    textIpDomainR.insert(INSERT, "域名：" + str(data.domain_name) + '\n\n')
    textIpDomainR.insert(INSERT, "注册商：" + str(data.registrar) + '\n\n')
    textIpDomainR.insert(INSERT, "域名服务器：" + str(data.whois_server) + '\n\n')
    textIpDomainR.insert(INSERT, "传送URL：" + str(data.referral_url) + '\n\n')
    textIpDomainR.insert(INSERT, "更新时间：" + str(data.updated_date) + '\n\n')
    textIpDomainR.insert(INSERT, "创建时间：" + str(data.creation_date) + '\n\n')
    textIpDomainR.insert(INSERT, "过期时间：" + str(data.expiration_date) + '\n\n')
    textIpDomainR.insert(INSERT, "DNS：" + str(data.name_servers) + '\n\n')
    textIpDomainR.insert(INSERT, "状态：" + str(data.status) + '\n\n')
    textIpDomainR.insert(INSERT, "邮箱：" + str(data.emails) + '\n\n')
    textIpDomainR.insert(INSERT, "DNSSEC：" + str(data.dnssec) + '\n\n')
    textIpDomainR.insert(INSERT, "名字：" + str(data.name) + '\n\n')
    textIpDomainR.insert(INSERT, "组织：" + str(data.org) + '\n\n')
    textIpDomainR.insert(INSERT, "地址：" + str(data.address) + '\n\n')
    textIpDomainR.insert(INSERT, "城市：" + str(data.city) + '\n\n')
    textIpDomainR.insert(INSERT, "区域：" + str(data.state) + '\n\n')
    textIpDomainR.insert(INSERT, "邮编：" + str(data.zipcode) + '\n\n')
    textIpDomainR.insert(INSERT, "国家：" + str(data.country) + '\n\n')
'''
