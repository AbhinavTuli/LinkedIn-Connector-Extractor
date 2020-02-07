from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
stime=int(input('Sleep time? '))
pages=int(input('Pages? '))
chromedriver_path = '/Users/abhinav/Downloads/chromedriver' #change this to your own path
driver = webdriver.Chrome(executable_path=chromedriver_path) 
sleep(2)
home = 'https://www.linkedin.com/feed/'
driver.get(home)
sleep(5)
driver.find_element_by_link_text("Sign in").click()
sleep(5)
username = driver.find_element_by_xpath("//input[@id='username']")
username.send_keys('//Put your email id here')
pwd = driver.find_element_by_xpath("//input[@id='password']")
pwd.send_keys('//Put your password here')
driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()
sleep(5)
driver.find_element_by_xpath("//input[@class='search-global-typeahead__input']").click()
driver.find_element_by_xpath("//input[@class='search-global-typeahead__input']").send_keys(Keys.ENTER)
sleep(5)
driver.find_element_by_xpath("//button[@aria-label='View only People results']").click()
sleep(5)
driver.find_element_by_xpath("//button[@data-control-name='all_filters']").click()
sleep(1)
# driver.find_element_by_xpath("//label[@for='sf-network-F']").click()
# # driver.find_element_by_xpath("//label[@for='sf-network-S']").click()
# driver.find_element_by_xpath("//input[@placeholder='Add a country/region']").send_keys(region)
# sleep(1)
# driver.find_element_by_xpath("//input[@placeholder='Add a country/region']").send_keys(Keys.DOWN)
# driver.find_element_by_xpath("//input[@placeholder='Add a country/region']").send_keys(Keys.ENTER)

# driver.find_element_by_xpath("//input[@placeholder='Add a current company']").send_keys(company)
# sleep(1)
# driver.find_element_by_xpath("//input[@placeholder='Add a current company']").send_keys(Keys.DOWN)
# driver.find_element_by_xpath("//input[@placeholder='Add a current company']").send_keys(Keys.ENTER)

# # driver.find_element_by_xpath("//input[@placeholder='Add an industry']").send_keys(industry)
# sleep(1)
# driver.find_element_by_xpath("//input[@placeholder='Add an industry']").send_keys(Keys.DOWN)
# driver.find_element_by_xpath("//input[@placeholder='Add an industry']").send_keys(Keys.ENTER)

# driver.find_element_by_xpath("//input[@placeholder='Add a school']").send_keys(school)
# sleep(1)
# driver.find_element_by_xpath("//input[@placeholder='Add a school']").send_keys(Keys.DOWN)
# driver.find_element_by_xpath("//input[@placeholder='Add a school']").send_keys(Keys.ENTER)
sleep(stime)
driver.find_element_by_xpath("//button[@data-control-name='all_filters_apply']").click()
sleep(5)
final=[]
for i in range(2):
    scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
    sleep(1)
sleep(2)
l=driver.find_elements_by_xpath(".//a[@class='search-result__result-link ember-view']")
#print(len(l))

urls=[]
for i in range(len(l)):
    if i%2==0:
        continue
    urls.append(l[i].get_attribute('href'))

for p in range(pages-1):
    try:
        li=driver.find_elements_by_xpath("//span[@class='artdeco-button__text']")
        f=0
        for i in range(len(li)):
            if li[i].text=='Next':
                li[i].click()
                f=1
        if f==0:
            break
        sleep(5)
        for i in range(2):
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            sleep(1)
        sleep(2)
        l=driver.find_elements_by_xpath(".//a[@class='search-result__result-link ember-view']")
        for i in range(len(l)):
            if i%2==0:
                continue
            urls.append(l[i].get_attribute('href'))
    except Exception as e:
        print(e)
        break

#print(urls)

for i in urls:
    driver.get(i)
    sleep(2)
    getName=driver.find_element_by_xpath("//li[@class='inline t-24 t-black t-normal break-words']").text
    try:
        getDesignation=driver.find_element_by_xpath("//h2[@class='mt1 t-18 t-black t-normal']").text
    except:
        getDesignation='Not mentioned'
    try:
        driver.find_element_by_link_text("Contact info").click()
        sleep(1)
        getEmail=driver.find_element_by_xpath("//a[starts-with(@href, 'mailto')]").text
        print(getEmail)
    except Exception as e:
        #print(e)
        getEmail='Not Found'
    row=[]
    row.append(getName)
    row.append(getDesignation)
    row.append(getEmail)
    row.append(i)
    final.append(row)

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(final)
