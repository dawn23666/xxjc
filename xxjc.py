import requests,json,re,time,os,random,string,keyboard,pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from PIL import Image
from pytesseract import image_to_string
from PIL import ImageGrab
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
driver = webdriver.Chrome()
driver.get("https://outlook.live.com/owa/?nlp=1&signup=1")
login_form = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view']/div[@id='Credentials']/form[@id='CredentialsForm']/div/div[@id='CredentialsInputPane']/fieldset/div[@class='row']/div[@class='form-group col-xs-24']/div[2]/div[@class='ltr_override']/input[@id='MemberName']")
login_form.send_keys('a' + salt )
login_click = driver.find_element_by_id('iSignupAction').click()
sleep(3.5)
login_pass = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='Password']/form[@id='PasswordForm']/div[@class='row form-group']/div[@class='col-md-24']/input[@id='PasswordInput']")
login_pass.send_keys(email_pass)
del login_click
login_click = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='Password']/form[@id='PasswordForm']/div[@class='win-button-pin-bottom']/div[@class='row']/div[@class='button-container']/div[@class='inline-block']/input[@id='iSignupAction']").click()
del login_click,login_form,login_pass
sleep(1.5)
login_form = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='ProfileAccrual']/form[@id='ProfileAccrualForm']/div[@id='ProfileAccrualInputPane']/div[@class='row']/div[@class='form-group col-md-24'][1]/input[@id='LastName']")
login_form.send_keys('1')
del login_form
login_form = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='ProfileAccrual']/form[@id='ProfileAccrualForm']/div[@id='ProfileAccrualInputPane']/div[@class='row']/div[@class='form-group col-md-24'][2]/input[@id='FirstName']")
login_form.send_keys('1')
login_form.send_keys(Keys.ENTER)
del login_form
sleep(1.5)
login_form = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='BirthDateCountryAccrual']/form[@id='BirthDateCountryAccrualForm']/div[@id='BirthDateCountryAccrualInputPane']/div[@class='row'][2]/div[@class='form-group form-control force-padding']/div[@id='BirthYearContainer']/select[@id='BirthYear']/option[30]").click()
del login_form
login_form = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='BirthDateCountryAccrual']/form[@id='BirthDateCountryAccrualForm']/div[@id='BirthDateCountryAccrualInputPane']/div[@class='row'][2]/div[@class='form-group form-control force-padding']/div[@id='BirthMonthContainer']/select[@id='BirthMonth']/option[2]").click()
del login_form
login_form = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='BirthDateCountryAccrual']/form[@id='BirthDateCountryAccrualForm']/div[@id='BirthDateCountryAccrualInputPane']/div[@class='row'][2]/div[@class='form-group form-control force-padding']/div[@id='BirthDayContainer']/select[@id='BirthDay']/option[20]").click()
del login_form
login_form = driver.find_element_by_xpath("/html[@class='m_ul']/body[@class='ltr  Chrome _Win _M89 _D0 Full Win81 RE_WebKit hide-cookie-banner']/div[@id='iPageElt']/div[@id='c_base']/div[@id='c_content']/div[@class='outer']/div[@class='middle ']/div[@id='inner']/div[@class='win-scroll']/div[@id='pageContent']/div[@id='maincontent']/div[@id='pageControlHost']/div[@class='pagination-view has-identity-banner']/div[@id='BirthDateCountryAccrual']/form[@id='BirthDateCountryAccrualForm']/div[@id='BirthDateCountryAccrualInputPane']/div[@class='win-button-pin-bottom']/div[@class='row']/div[@class='button-container no-margin-bottom']/div[@class='inline-block']/input[@id='iSignupAction']").click()
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
def send_verification_code():
    htmlcookie = requests.get('https://xxjc.vip',headers=headers)
    c = {'email':email_name}
    requests.post('https://xxjc.vip/auth/send',data=c,headers=headers,cookies=htmlcookie.cookies)
print('OK!')
keyboard.wait(']')
send_verification_code()
'''
bbox = (392,491,485,519)
img = ImageGrab.grab(bbox)
text = image_to_string(img,lang='chi_sim')
'''
z = input('emailcode:')
'''
if text == '小小机场' :
    pyautogui.click(485,519)
'''
def login():
    d = {'email':email_name,'name':email_name,'passwd':email_name,'repasswd':email_name,'wechat':email_name,'imtype':'1','code':'0','emailcode':z}
    requests.post('https://xxjc.vip/auth/register',headers=headers,data=d)
    s = {'email':email_name,'passwd':email_name,'code':''}
    f = requests.post('https://xxjc.vip/auth/login',headers=headers,data=s)
    i = requests.get('https://xxjc.vip/user',headers=headers,cookies=f.cookies)
    html = i.text
    url = re.findall('<button class="copy-text btn btn-subscription col-xx-12 col-sm-3 col-lg-2" type="button" data-clipboard-text="(.*?)">',html)
    ssrjson = url[0]
    a = '{\"configs\" : [ 			{ 				\"remarks\" : \"\", 				\"id\" : \"7DD53D24B7DA27E51453A9FD81EEF215\", 				\"server\" : \"server host\", 				\"server_port\" : 8388, 				\"server_udp_port\" : 0, 				\"password\" : \"0\", 				\"method\" : \"aes-256-cfb\", 				\"protocol\" : \"origin\", 				\"protocolparam\" : \"\", 				\"obfs\" : \"plain\", 				\"obfsparam\" : \"\", 				\"remarks_base64\" : \"\", 				\"group\" : \"FreeSSR-public\", 				\"enable\" : true, 				\"udp_over_tcp\" : false 			} 		], 		\"index\" : 0, 		\"random\" : true, 		\"sysProxyMode\" : 3, 		\"shareOverLan\" : true, 		\"localPort\" : 1080, 		\"localAuthPassword\" : \"o3-VjtCQCBLlVletTSc2\", 		\"dnsServer\" : \"\", 		\"reconnectTimes\" : 2, 		\"balanceAlgorithm\" : \"LowException\", 		\"randomInGroup\" : false, 		\"TTL\" : 0, 		\"connectTimeout\" : 5, 		\"proxyRuleMode\" : 2, 		\"proxyEnable\" : false, 		\"pacDirectGoProxy\" : false, 		\"proxyType\" : 0, 		\"proxyHost\" : \"\", 		\"proxyPort\" : 0, 		\"proxyAuthUser\" : \"\", 		\"proxyAuthPass\" : \"\", 		\"proxyUserAgent\" : \"\", 		\"authUser\" : \"\", 		\"authPass\" : \"\", 		\"autoBan\" : false, 		\"sameHostForSameTarget\" : false, 		\"keepVisitTime\" : 180, 		\"isHideTips\" : false, 		\"nodeFeedAutoUpdate\" : true, 		\"serverSubscribes\" : [ 			{ 				\"URL\" : \"'+ssrjson+'\", 				\"Group\" : \"\", 				\"LastUpdateTime\" : 0 			} 		], 		\"token\" : {  		}, 		\"portMap\" : {  		} 	}'
    with open('gui-config.json', 'w') as f:
        f.write(a)
login()
driver.quit()