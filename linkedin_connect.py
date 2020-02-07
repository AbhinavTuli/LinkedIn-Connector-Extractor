from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
stime=int(input('Enter Sleep Time on filters page: '))
pages=int(input('Enter number of Pages of search result that you want to reach : '))
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
sleep(stime)
driver.find_element_by_xpath("//button[@data-control-name='all_filters_apply']").click()
sleep(5)
for i in range(2):
    scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
    sleep(1)
l=driver.find_elements_by_xpath("//button[starts-with(@aria-label, 'Connect with')]")
print(len(l))
scroll = driver.find_element_by_tag_name('body').send_keys(Keys.HOME)

for c in l:
    c.location_once_scrolled_into_view
    driver.find_element_by_tag_name('body').send_keys(Keys.UP)
    driver.find_element_by_tag_name('body').send_keys(Keys.UP)
    driver.find_element_by_tag_name('body').send_keys(Keys.UP)
    sleep(1)
    c.click()
    sleep(1)
    li=driver.find_elements_by_xpath("//span[@class='artdeco-button__text']")
    try:
        for i in range(len(li)):
            if li[i].text=='Send now':
                li[i].click()
                break
    except:
        driver.find_element_by_xpath("//button[@aria-label='Dismiss']").click()
    sleep(2)

for y in range(pages-1):
    try:
        li=driver.find_elements_by_xpath("//span[@class='artdeco-button__text']")
        f=0
        for i in range(len(li)):
            if li[i].text=='Next':
                li[i].click()
                f=1
                break
        if f==0:
            break
        sleep(5)
        for i in range(2):
            scroll = driver.find_element_by_tag_name('body').send_keys(Keys.END)
            sleep(1)
        l=driver.find_elements_by_xpath("//button[starts-with(@aria-label, 'Connect with')]")
        print(len(l))
        scroll = driver.find_element_by_tag_name('body').send_keys(Keys.HOME)

        for c in l:
            c.location_once_scrolled_into_view
            driver.find_element_by_tag_name('body').send_keys(Keys.UP)
            driver.find_element_by_tag_name('body').send_keys(Keys.UP)
            driver.find_element_by_tag_name('body').send_keys(Keys.UP)
            sleep(1)
            c.click()
            sleep(1)
            li=driver.find_elements_by_xpath("//span[@class='artdeco-button__text']")
            try:
                for i in range(len(li)):
                    if li[i].text=='Send now':
                        li[i].click()
                        break
            except:
                driver.find_element_by_xpath("//button[@aria-label='Dismiss']").click()
            sleep(1)
        
    except Exception as e:
        print(e)
        break


