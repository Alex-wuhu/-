# -*- coding:utf-8 -*-
#没做输入错误的exception,别乱输入就行
#b站的方法类似就不再重复了
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
import pickle
plat=1
dic=["国玉帅的翘jiojio","国玉真是绝绝子啊","骂国玉的弹幕真下头啊","卡莎哥哥好瘤呀","主播真是准的翘jiojio","今天又是在逃公主的一天呢"]
def login(url,plat):
    driver.get(url)
    print(driver.title)
    time.sleep(1)
    if(plat==1):
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-header > div > div > div.Header-right > div.Header-login-wrap")))
    # driver.find_element_by_link_text("登录").click()
    # 点击登录按钮
        login_button.click()

    # 这个时候我们用二维码登录，设置最多等待3分钟，如果登录那个区域是可见的，就登录成功
        WebDriverWait(driver, 180).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "UserInfo-link")))

    # 保存cookie到cookies.pkl文件
        session = requests.Session()
        # 获取cookie
        cookies = driver.get_cookies()
        # 把cookie写入文件
        if not os.path.exists("cookie"):
            os.mkdir("cookie")
        pickle.dump(cookies, open("./cookie/douyu_cookies.pkl", "wb"))
    elif(plat==2):

        #第一次手动登录，记录cookies  后面就能自动登录
        
        login_button=wait.until(
                EC.element_to_be_clickable((By.XPATH,"//*[@id=\"J_duyaHeaderRight\"]/div/div[2]/a")))
        login_button.click()
        WebDriverWait(driver,180).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"UserHd--2DND8QhAwGaVTH6yTa5Jeh"))
        )
        print("check 1 2 12")
        session = requests.Session()
        # 获取cookie
        cookies = driver.get_cookies()
        # 把cookie写入文件
        if not os.path.exists("cookie"):
            os.mkdir("cookie")
        pickle.dump(cookies, open("./cookie/huya_cookies.pkl", "wb"))
      

    print("登录成功")


def login_with_cookie(url,plat):
   
    driver.get(url)
  
    # 把cookie文件加载出来
    if(plat==1):
        with open("./cookie/douyu_cookies.pkl", "rb") as cookiefile:
            cookies = pickle.load(cookiefile)
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)
        time.sleep(3)
        driver.refresh()
        # 如果登录成功那个区域不可见的，说明cookie没有登录成功，重新用二维码登录
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "UserInfo-link")))
        except:
            print("对不起，使用cookie登录失败，请重新扫描二维码登录")
            login(url,plat)
    elif(plat==2):
        with open("./cookie/huya_cookies.pkl", "rb") as cookiefile:
            cookies = pickle.load(cookiefile)
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)
        time.sleep(3)
        driver.refresh()
        try:
            WebDriverWait(driver,10).until(
                EC.visibility_of_element_located((By.CLASS_NAME,"UserHd--2DND8QhAwGaVTH6yTa5Jeh"))
            )
        except:
            print("cookie登录失败，请重新扫描二维码")
            login(url,plat)
        # 如果登录成功那个区域不可见的，说明cookie没有登录成功，重新用二维码登录
        
       
    print("登录成功")
    
    print(driver.title)
def waiting(times):
        #倒计时一下
    for x in range(times,-1,-1):
        
        mystr = "请再等待" + str(x) + "秒后系统会再次发送弹幕"
        if x==0:
            print(mystr)
        else:
            print(mystr,end = "")
            print("\b" * (len(mystr)*2),end = "",flush=True)
            time.sleep(1)


def send_barrage_huya(times):
    global dic
    if(modle==1):
        with open("./danmu/weicheng.txt","r",encoding='utf-8')  as F:
            while(True):
                for i in range(3):
                    sentence=F.readline(30)
                    s="".join(sentence.split())
                    while(len(s)<20):
                        s=s+"".join((F.readline(5)).split())
                    time.sleep(5)
                    wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#pub_msg_input"))).send_keys(s)
                    wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#msg_send_bt"))).click()
                    print(s)    
                    # 清空输入框信息
                    wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#pub_msg_input"))).clear()
                waiting(times)
    elif(modle==2):
        while(True):
            for i in range(3,6):
                time.sleep(5)
                wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#pub_msg_input"))).send_keys(dic[i])
                wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#msg_send_bt"))).click()
                print(dic[i])    
                # 清空输入框信息
                wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#pub_msg_input"))).clear()
            waiting(times)
       


   
        

def send_barrage_douyu(times,modle):
    global dic
    if(modle==1):
        with open("./danmu/weicheng.txt","r",encoding='utf-8')  as F:
            while(True):
                for i in range(3):
                    sentence=F.readline(30)
                    s="".join(sentence.split())
                    while(len(s)<20):
                        s=s+"".join((F.readline(5)).split())
                    time.sleep(5)
                    wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea"))).send_keys(s)
                    wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > div.ChatSend-button"))).click()
                    print(s)    
                    # 清空输入框信息
                    wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea"))).clear()
                waiting(times)
    elif(modle==2):
        while(True):
            for i in range(3):
                time.sleep(5)
                wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea"))).send_keys(dic[i])
                wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > div.ChatSend-button"))).click()
                print(dic[i])    
                # 清空输入框信息
                wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea"))).clear()
            waiting(times)
       

     

if __name__ == "__main__":


    output=input('每隔多少秒发送一套弹幕？？？（默认是60s）')

    plat=int(input("选择平台：1.斗鱼，2.虎牙，3.批站 "))
    modle=int(input("选择弹幕模式：1.独轮车模式（记得放入文本），2.自动弹幕"))
    if output=='':
        times=60
    else:
        times= int(output)   
    
    options = webdriver.ChromeOptions()
    #设置prefs加快爬取速度
    prefs = {
        "profile.default_content_setting_values.plugins": 1,
        "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
        #"PluginsAllowedForUrls": "https://www.douyu.com"
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=options)
    
    #driver = webdriver.Chrome()
    # 隐式等待是全局性的，只要用了driver.findxx没有第一时间找到元素，就会等待5s，当然一般都被用wait覆盖掉了
    driver.implicitly_wait(5)
    # 显示等待是定向性的，最大等待时间10s,每次检测元素有没有生成的时间间隔300ms，过了最大等待时间抛出异常
    wait = WebDriverWait(driver, timeout=10, poll_frequency=300)
    if(plat==1):
        url = 'https://www.douyu.com/12306'
        if os.path.exists("./cookie/douyu_cookies.pkl"):
            print("当前目录下存在斗鱼登录的cookie文件，将为您自动登录")
            login_with_cookie(url,plat)
        else:
            print("当前目录下不存在斗鱼登录的cookie文件")
            login(url,plat)
        send_barrage_douyu(times,modle)
    elif(plat==2):
        url = 'https://www.huya.com/kasha233'
        if os.path.exists("./cookie/huya_cookies.pkl"):
            print("当前目录下存在huya登录的cookie文件，将为您自动登录")
            login_with_cookie(url,plat)
        else:
            print("当前目录下不存在虎牙登录的cookie文件")
            login(url,plat)
        send_barrage_huya(times)
