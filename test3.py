
def scrapping():
    from requests import get
    from requests.exceptions import RequestException
    from contextlib import closing
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver
    import pandas as pd
    import webbrowser
    import time

    driver = webdriver.Chrome("E:\Tester\selenium\chromedriver.exe")
    From_addr = []
    re = []

    url = "https://www.thestylistgroup.com"
    #url1 = url+"="+str(i)

    driver.get(url)
    content = driver.page_source
    soup = bs(content,features='lxml')
    for divclass in soup.findAll('div', attrs={'class': 'css-1csq14c'}):
        for second in divclass.findAll('div', attrs={'class': 'css-1ulnjuj'}):
            for third in second.findAll('div', attrs={'class': 'css-lnxfag'}):

                for fourth in third.findAll('div', attrs={'class': 'css-y2uk4n'}):

                    '''for fifth in fourth.findAll('div', attra={'class': 'css-1b0o2qe'}):'''
                    for heading in fourth.findAll('h2',attrs={'class':'css-6r2li'}):
                        print(heading.text)
                        for desc in fourth.findAll('div',attrs={'class':'css-1bytni4'}):
                            print(desc.text)

scrapping()