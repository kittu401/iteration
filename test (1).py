def scrapping():
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    import pandas as pd


    driver = webdriver.Chrome("E:\Tester\selenium\chromedriver.exe",chrome_options=chrome_options)
    From_addr = []
    re = []
    i = 3409
    url = "https://etherscan.io/txs?ps=100&p"
    while i <= 5000:
        url1 = url+"="+str(i)
        print(i)
        driver.get(url1)
        content = driver.page_source
        soup = bs(content,features='lxml')
        table = soup.find('table',class_ = 'table table-hover')
        for row in table.findAll('tr'):

                if row.find('a', class_='hash-tag text-truncate'):
                    link = row.find('a', class_='hash-tag text-truncate')['href']

                    From_addr.append(link)
                else:
                    for td in row.findAll('td'):
                        for span in td.findAll('span',attrs={'class':'hash-tag text-truncate'}):
                            for link in span.findAll('a',href = True):

                                From_addr.append(link.text)
        i = i + 1
        df=pd.DataFrame({'From_Addr':From_addr})
        df.to_csv('trans1.csv',index=False, encoding='utf-8')
scrapping()