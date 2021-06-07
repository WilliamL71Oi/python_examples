import dns.resolver


domain = input('请输入：')
def dns_query(domain, type):
    try:
        A = dns.resolver.resolve(domain, type)
        for i in A.response.answer:
            for j in i:
                print(j)
    except dns.resolver.NoAnswer:
        print(domain + ' 此域名，DNS未响应！')


dns_query(domain, 'NS')
dns_query(domain, 'A')
dns_query(domain, 'MX')
dns_query('www.' + domain, 'CNAME')

