import pyperclip
import re
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'}
email = input('email:')
verification_code = {'email': email}
url = 'https://xxjc.in/'
requests.post(url + 'auth/send', data=verification_code, headers=headers)
emailcode = input('emailcode:')
d = {'email': email, 'name': email, 'passwd': email, 'repasswd': email, 'wechat': email, 'imtype': '1', 'code': '0',
     'emailcode': emailcode}
requests.post(url + 'auth/register', headers=headers, data=d)
s = {'email': email, 'passwd': email, 'code': ''}
login = requests.post(url + 'auth/login', headers=headers, data=s)
i = requests.get(url + 'user', headers=headers, cookies=login.cookies)
html = i.text
web_data = re.findall(
    '<button class="copy-text btn btn-subscription col-xx-12 col-sm-3 col-lg-2" type="button" data-clipboard-text="('
    '.*?)">',
    html)
ssrjson = web_data[0]
pyperclip.copy(ssrjson)
a = '{"Configs":[{"Id":"3b0a24e3f82e41e282f43a6b33aac8c1","server":"server host","Server_Port":8388,' \
    '"Server_Udp_Port":0,"Password":"0","Method":"aes-256-cfb","Protocol":"origin","ProtocolParam":"","obfs":"plain",' \
    '"ObfsParam":"","Remarks_Base64":"","Group":"Default Group","SubTag":"","Enable":true,"UdpOverTcp":false}],' \
    '"Index":0,"Random":false,"SysProxyMode":2,"ShareOverLan":true,"LocalPort":33333,"ReconnectTimes":2,' \
    '"BalanceType":4,"RandomInGroup":true,"Ttl":60,"ConnectTimeout":5,"ProxyRuleMode":2,"ProxyEnable":false,' \
    '"PacDirectGoProxy":false,"ProxyType":0,"ProxyHost":"","ProxyPort":1,"ProxyAuthUser":"","ProxyAuthPass":"",' \
    '"ProxyUserAgent":"","AuthUser":"","AuthPass":"","AutoBan":false,"CheckSwitchAutoCloseAll":true,"LogEnable":true,' \
    '"SameHostForSameTarget":false,"IsPreRelease":false,"AutoCheckUpdate":true,"LangName":"","DnsClients":[{' \
    '"Enable":true,"DnsType":1,"Ipv6First":false,"DnsServer":"208.67.222.222","Port":853,"Timeout":10000,' \
    '"IsEDnsEnabled":false,"EcsIp":"208.67.222.222","EcsSourceNetmask":32,"EcsScopeNetmask":0,"IsTcpEnabled":true,' \
    '"IsUdpEnabled":true},{"Enable":true,"DnsType":1,"Ipv6First":false,"DnsServer":"208.67.220.220","Port":853,' \
    '"Timeout":10000,"IsEDnsEnabled":false,"EcsIp":"208.67.222.222","EcsSourceNetmask":32,"EcsScopeNetmask":0,' \
    '"IsTcpEnabled":true,"IsUdpEnabled":true},{"Enable":true,"DnsType":1,"Ipv6First":false,"DnsServer":"1.1.1.1",' \
    '"Port":853,"Timeout":10000,"IsEDnsEnabled":false,"EcsIp":"208.67.222.222","EcsSourceNetmask":32,' \
    '"EcsScopeNetmask":0,"IsTcpEnabled":true,"IsUdpEnabled":true},{"Enable":true,"DnsType":1,"Ipv6First":false,' \
    '"DnsServer":"1.0.0.1","Port":853,"Timeout":10000,"IsEDnsEnabled":false,"EcsIp":"208.67.222.222",' \
    '"EcsSourceNetmask":32,"EcsScopeNetmask":0,"IsTcpEnabled":true,"IsUdpEnabled":true},{"Enable":true,"DnsType":1,' \
    '"Ipv6First":false,"DnsServer":"1.12.12.12","Port":853,"Timeout":10000,"IsEDnsEnabled":false,' \
    '"EcsIp":"208.67.222.222","EcsSourceNetmask":32,"EcsScopeNetmask":0,"IsTcpEnabled":true,"IsUdpEnabled":true}],' \
    '"ServerSubscribes":[{"Url":"' + ssrjson + '","Tag":"6F239D5508B9326E482DB5022257098E","LastUpdateTime":0,' \
                                               '"AutoCheckUpdate":true,"ProxyType":0}],"PortMap":{}}'
with open('gui-config.json', 'w') as f:
    f.write(a)
