from selenium import webdriver

search = input("Enter the search: ")
search = search.replace(' ', '+')

browser = webdriver.Chrome('chromedriver.exe')

for i in range(1):
    browser.get('https://www.google.com/search?q='+search+'&start'+str(i))