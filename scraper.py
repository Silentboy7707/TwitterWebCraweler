import csv
import re
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

data=[]

def extractor(card):
    try:
        name = card.find_element(By.XPATH,'./div/div/div[2]/div[2]/div[1]//span/span').text
        twthandle = card.find_element(By.XPATH,'.//span[contains(text(), "@")]').text
        tweet_text = card.find_element(By.XPATH,'./div/div/div[2]/div[2]/div[2]').text
        # try:
        #     show_more=card.find_element(By.XPATH,'//article[@data-testid="tweet"]//span[@data-testid="tweet-text-show-more-link"]')
        #     show_more.send_keys(Keys.CONTROL + Keys.ENTER)
        #     print("poggers")
        # except:
        #     tweet_text=tweet_text
        data.append((name,twthandle,tweet_text))
    except:
        return

topics=["AI taking jobs","AI art stealing","Is Alexa good","Mahindra car reviews","Honda car reviews","HUman gene editing","Cryptocurrency reliabilty", "Climate change", "Driverless cars legality", "Electric cars", "Marijuana legalisation", "Alcohol ban india"]

topic=input("Enter a topic>>> ")

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
edge_driver_path = './msedgedriver.exe'
edge_service = Service(edge_driver_path)
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')


driver = webdriver.Edge(service=edge_service, options=edge_options)
driver.get('https://www.twitter.com/login')
driver.maximize_window()

sleep(3)
driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys("05Ayushgarg1")
driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()

sleep(3)
driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys('Ayush@9958144502')

sleep(3)
driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
sleep(2)



try:
    driver.get("https://twitter.com/home")
    sleep(3)
    driver.find_element(By.XPATH,'//input[@data-testid="SearchBox_Search_Input"]').send_keys(topic)
    driver.find_element(By.XPATH,'//input[@data-testid="SearchBox_Search_Input"]').send_keys(Keys.ENTER)

    #loop
    num=1
    flag=1
    while num<=50 and flag==1:
        print("On loop no ->>",num)
        sleep(2)
        num+=1
        tries=0
        last_pos = driver.execute_script('return window.pageYOffset;')
        cards=driver.find_elements(By.XPATH,'//article[@data-testid="tweet"]')
        for card in cards[-15:]:
            extractor(card)
        curr_pos=last_pos
        
        with open(topic+'.csv','a',newline='', encoding= 'utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
            data=[]
    


        while(curr_pos==last_pos):
            if(tries>=6):
                flag=0
                break
            else:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(3)
                curr_pos = driver.execute_script('return window.pageYOffset;')
                tries+=1
                print("Current try no. ---> ",tries)

    print(len(data))
except:
    num+=1
    
