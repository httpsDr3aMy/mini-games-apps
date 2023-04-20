from selenium import webdriver
import time

browse = webdriver.Chrome()

def finding_by_xpath(method, path):
    global browse
    finder = browse.find_element(method, path)
    return finder
        

browse.get('https://steamcommunity.com/market/?l=polish')

'''btn = finding_by_xpath('xpath','//*[@id="browseItems"]/div/a[2]')
btn.click()
browse.get(finding_by_xpath('xpath', '//*[@id="resultlink_0"]').get_attribute('href'))

price = finding_by_xpath('xpath', '//*[@id="market_commodity_forsale"]/span[2]').get_attribute('innerText')
print(f'Oto cena pierwszej skrzynki {price}.')'''
browse.quit()