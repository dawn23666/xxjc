import requests,json,re,time,os,random,string
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
htmlcookie = requests.get('https://xxjc.vip')
a = input('email:')
c = {'email':a}
requests.post('https://xxjc.vip/auth/send',data=c,headers=headers,cookies=htmlcookie.cookies)
z = input('emailcode:')
d = {'email':a,'name':a,'passwd':a,'repasswd':a,'wechat':a,'imtype':'1','code':'0','emailcode':z}
requests.post('https://xxjc.vip/auth/register',headers=headers,data=d)
s = {'email':a,'passwd':a,'code':''}
f = requests.post('https://xxjc.vip/auth/login',headers=headers,data=s)
i = requests.get('https://xxjc.vip/user',headers=headers,cookies=f.cookies)
html = i.text
url = re.findall('<button class="copy-text btn btn-subscription col-xx-12 col-sm-3 col-lg-2" type="button" data-clipboard-text="(.*?)">',html)
ssrjson = url[0]
a = '{\"configs\" : [ 			{ 				\"remarks\" : \"\", 				\"id\" : \"7DD53D24B7DA27E51453A9FD81EEF215\", 				\"server\" : \"server host\", 				\"server_port\" : 8388, 				\"server_udp_port\" : 0, 				\"password\" : \"0\", 				\"method\" : \"aes-256-cfb\", 				\"protocol\" : \"origin\", 				\"protocolparam\" : \"\", 				\"obfs\" : \"plain\", 				\"obfsparam\" : \"\", 				\"remarks_base64\" : \"\", 				\"group\" : \"FreeSSR-public\", 				\"enable\" : true, 				\"udp_over_tcp\" : false 			} 		], 		\"index\" : 0, 		\"random\" : true, 		\"sysProxyMode\" : 3, 		\"shareOverLan\" : true, 		\"localPort\" : 1080, 		\"localAuthPassword\" : \"o3-VjtCQCBLlVletTSc2\", 		\"dnsServer\" : \"\", 		\"reconnectTimes\" : 2, 		\"balanceAlgorithm\" : \"LowException\", 		\"randomInGroup\" : false, 		\"TTL\" : 0, 		\"connectTimeout\" : 5, 		\"proxyRuleMode\" : 2, 		\"proxyEnable\" : false, 		\"pacDirectGoProxy\" : false, 		\"proxyType\" : 0, 		\"proxyHost\" : \"\", 		\"proxyPort\" : 0, 		\"proxyAuthUser\" : \"\", 		\"proxyAuthPass\" : \"\", 		\"proxyUserAgent\" : \"\", 		\"authUser\" : \"\", 		\"authPass\" : \"\", 		\"autoBan\" : false, 		\"sameHostForSameTarget\" : false, 		\"keepVisitTime\" : 180, 		\"isHideTips\" : false, 		\"nodeFeedAutoUpdate\" : true, 		\"serverSubscribes\" : [ 			{ 				\"URL\" : \"'+ssrjson+'\", 				\"Group\" : \"\", 				\"LastUpdateTime\" : 0 			} 		], 		\"token\" : {  		}, 		\"portMap\" : {  		} 	}'
with open('gui-config.json', 'w') as f:
    f.write(a)