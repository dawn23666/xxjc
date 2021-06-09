import requests,re,string,keyboard,random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
def ranstr(num):
    H = 'abcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(num):
        salt += random.choice(H)
        del i
    return salt
salt = ranstr(9)
email_name = 'a' + salt + '@outlook.com'
email_pass = ranstr(15)
options = webdriver.ChromeOptions()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
driver = webdriver.Chrome(r'.\driver.exe',chrome_options = options)
driver.get("https://outlook.live.com/owa/?nlp=1&signup=1")
login_form = driver.find_element_by_id('MemberName')
login_form.send_keys('a' + salt )
driver.find_element_by_id('iSignupAction').click()
driver.implicitly_wait(3.5)
login_pass = driver.find_element_by_xpath("//*[@id='PasswordInput']")
login_pass.send_keys(email_pass)
driver.find_element_by_xpath("//*[@id='iSignupAction']").click()
login_form = driver.find_element_by_xpath("//*[@id='LastName']")
login_form.send_keys('1')
login_form = driver.find_element_by_xpath("//*[@id='FirstName']")
login_form.send_keys('1')
login_form.send_keys(Keys.ENTER)
try:
    login_form = driver.find_element_by_xpath("//*[@id='BirthYear']")
    login_form.send_keys('1980')
except:
    driver.find_element_by_xpath("//*[@id='BirthYear']/option[20]").click()
driver.find_element_by_xpath("//*[@id='BirthMonth']/option[2]").click()
driver.find_element_by_xpath("//*[@id='BirthDay']/option[20]").click()
driver.find_element_by_xpath("//*[@id='iSignupAction']").click()
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
def send_verification_code():
    c = {'email':email_name}
    requests.post('https://xxjc.vip/auth/send',data=c,headers=headers)
print('OK!')
keyboard.wait(']')
send_verification_code()
z = input('emailcode:')
def login():
    d = {'email':email_name,'name':email_name,'passwd':email_name,'repasswd':email_name,'wechat':email_name,'imtype':'1','code':'0','emailcode':z}
    requests.post('https://xxjc.vip/auth/register',headers=headers,data=d)
    s = {'email':email_name,'passwd':email_name,'code':''}
    f = requests.post('https://xxjc.vip/auth/login',headers=headers,data=s)
    i = requests.get('https://xxjc.vip/user',headers=headers,cookies=f.cookies)
    html = i.text
    url = re.findall('<input type="text" class="input form-control form-control-monospace cust-link col-xx-12 col-sm-8 col-lg-7" name="input1" readonly value="(.*?)" readonly="true">',html)
    ssrjson = url[0]
    a = '{\"configs\" : [ 			{ 				\"remarks\" : \"\", 				\"id\" : \"7DD53D24B7DA27E51453A9FD81EEF215\", 				\"server\" : \"server host\", 				\"server_port\" : 8388, 				\"server_udp_port\" : 0, 				\"password\" : \"0\", 				\"method\" : \"aes-256-cfb\", 				\"protocol\" : \"origin\", 				\"protocolparam\" : \"\", 				\"obfs\" : \"plain\", 				\"obfsparam\" : \"\", 				\"remarks_base64\" : \"\", 				\"group\" : \"FreeSSR-public\", 				\"enable\" : true, 				\"udp_over_tcp\" : false 			} 		], 		\"index\" : 0, 		\"random\" : true, 		\"sysProxyMode\" : 3, 		\"shareOverLan\" : true, 		\"localPort\" : 1080, 		\"localAuthPassword\" : \"o3-VjtCQCBLlVletTSc2\", 		\"dnsServer\" : \"\", 		\"reconnectTimes\" : 2, 		\"balanceAlgorithm\" : \"LowException\", 		\"randomInGroup\" : false, 		\"TTL\" : 0, 		\"connectTimeout\" : 5, 		\"proxyRuleMode\" : 2, 		\"proxyEnable\" : false, 		\"pacDirectGoProxy\" : false, 		\"proxyType\" : 0, 		\"proxyHost\" : \"\", 		\"proxyPort\" : 0, 		\"proxyAuthUser\" : \"\", 		\"proxyAuthPass\" : \"\", 		\"proxyUserAgent\" : \"\", 		\"authUser\" : \"\", 		\"authPass\" : \"\", 		\"autoBan\" : false, 		\"sameHostForSameTarget\" : false, 		\"keepVisitTime\" : 180, 		\"isHideTips\" : false, 		\"nodeFeedAutoUpdate\" : true, 		\"serverSubscribes\" : [ 			{ 				\"URL\" : \"'+ssrjson+'\", 				\"Group\" : \"\", 				\"LastUpdateTime\" : 0 			} 		], 		\"token\" : {  		}, 		\"portMap\" : {  		} 	}'
    with open('gui-config.json', 'w') as f:
        f.write(a)
login()
driver.quit()