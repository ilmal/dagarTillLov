import os
from bs4 import BeautifulSoup as soup
import lxml
import requests
import array as arr

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from pushbullet import Pushbullet

import asyncio
import json

print("starting...")

async def vklassLoginFunc(uname, psw):
    # setting up selenium
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')

    chrome_driver_binary = "/home/nils/.local/bin/chromedriver"

    browser = webdriver.Chrome(
        options=options, executable_path='/snap/bin/chromium.chromedriver')

    url = "https://auth.vklass.se/credentials"
    
    delay = 5
    
    browser.get(url)

    # accept cookies and stuff
    try:
        button = searchbox = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button")))
    except TimeoutException:
        print("Loading took too much time!")

    button.click()
    
    # login inputs
    # input location 1 (UNAME)
    try:
        searchbox = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/section/div[2]/div/form/div[1]/div/input")))
    except TimeoutException:
        print("Loading took too much time!")

    searchbox.send_keys(uname)

    # input location 2 (PASSWORD)
    try:
        searchbox = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/section/div[2]/div/form/div[2]/div/input")))
    except TimeoutException:
        print("Loading took too much time!")

    searchbox.send_keys(psw)
    
    # pressing login btn 
    try:
        button = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id="auth-credentials-index"]/form/div[4]/button")))
    except TimeoutException:
        print("Loading took too much time!")

    button.click()
    
async def getDaysFunc(endDate):
    # setting up selenium
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')

    chrome_driver_binary = "/home/nils/.local/bin/chromedriver"

    browser = webdriver.Chrome(
        options=options, executable_path='/snap/bin/chromium.chromedriver')

    url = "https://www.vklass.se/schema.aspx"
    
    delay = 5
    
    browser.get(url)

    def analyze_page_func(html):
        
    
    async def next_week_func():
        # press the "next week" tab 
        try:
            button = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/form/div[3]/div[1]/div[1]/div/p/a")))
        except TimeoutException:
            print("Loading took too much time!")

        button.click()

        url = "https://www.vklass.se/ClassCalendar.aspx?id=6a4fe49b-8031-437a-8b02-d8081128b87b"

        r = requests.get(url).text

        html = soup(r, "lxml")
        
        analyze_page_func(html)
    
    
async def getVklassInfoFunc():
  
    def count_kinds_of_tests(elements):
      kinds_of_tests=[
        "prov",
        "seminarium",
        "redovisning",
        "laboration",
        "läxa",
        "inlämningsuppgift"
      ]
      boilerplate_obj = {}
      # creating the boilerplate_obj from kinds_of_tests
      
      
      for element in elements: # looping through array of elements, which are text snippets extracted from calender
        print(element)
        
  
    # setting up selenium
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')

    chrome_driver_binary = "/home/nils/.local/bin/chromedriver"

    browser = webdriver.Chrome(
        options=options, executable_path='/snap/bin/chromium.chromedriver')

    url = "https://www.vklass.se/ClassCalendar.aspx?id=6a4fe49b-8031-437a-8b02-d8081128b87b"
    
    delay = 5
    
    browser.get(url)

    # press the "per vecka" tab in order to get all the test/ assignment info 
    try:
        button = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/form/div[3]/div[1]/div[1]/div/p/a")))
    except TimeoutException:
        print("Loading took too much time!")

    button.click()
    
    url = "https://www.vklass.se/ClassCalendar.aspx?id=6a4fe49b-8031-437a-8b02-d8081128b87b"
    
    r = requests.get(url).text

    html = soup(r, "lxml")
    
    for element in html.find("ctl00_ContentPlaceHolder2_articleContent").find_all("a"):
        print(element.get_text())
        
    count_kinds_of_tests(html.find("ctl00_ContentPlaceHolder2_articleContent").find_all("a"))
        
        


async def travelCalc(location):

    # setting up selenium
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')

    chrome_driver_binary = "/home/nils/.local/bin/chromedriver"

    browser = webdriver.Chrome(
        options=options, executable_path='/snap/bin/chromium.chromedriver')

    url = "https://google.com/maps/dir///"

    delay = 5

    browser.get(url)

    # accept cookies and stuff
    try:
        button = searchbox = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button")))
    except TimeoutException:
        print("Loading took too much time!")

    button.click()

    # function to calculate time to travel, using google maps, insert location
    # input location 1
    try:
        searchbox = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")))
    except TimeoutException:
        print("Loading took too much time!")

    searchbox.send_keys("järfälla")

    # input location 2
    try:
        searchbox = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input")))
    except TimeoutException:
        print("Loading took too much time!")

    searchbox.send_keys(location)

    # pressing the calculate button
    try:
        button = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]")))
    except TimeoutException:
        print("Loading took too much time!")

    button.click()

    def ifInputCorrect():
        delay = 0.1
        try:
            WebDriverWait(browser, delay).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[4]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/h2")))
        except TimeoutException:
            return False
        print("input location not found")
        return True

    if(ifInputCorrect()):
        print("input location not found.")
        return "input location not found."

    # setting transportatino to car

    try:
        transportation_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/button")))
    except TimeoutException:
        print("Loading took too much time!")

    transportation_button.click()

    # getting the time
    try:
        time = WebDriverWait(browser, delay).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[1]/span[1]")))
    except TimeoutException:
        print("Loading took too much time!")
        print("location: ", location)
    return time.text


# getting post with classname of this:


async def blocketScrape():

    # setting up soup

    url = "https://www.blocket.se/annonser/hela_sverige/elektronik/datorer_tv_spel/stationara_datorer?cg=5021&q=station%C3%A4r%20dator"

    url = "https://www.blocket.se/annonser/hela_sverige/elektronik/datorer_tv_spel/stationara_datorer?cg=5021&q=station%C3%A4r%20dator&sort=price"

    r = requests.get(url).text

    html = soup(r, "lxml")

    number_of_posts = 1
    posts = []
    json = {
        "posts": [],
        "number_of_posts": number_of_posts
    }

    for post in html.find_all("div", class_="styled__Wrapper-sc-1kpvi4z-0 gaNDDX"):
        # narrowing the search
        post = post.article.find(
            "div", class_="styled__Content-sc-1kpvi4z-2 diJXLP")

        # getting values
        title = post.find(
            "div", class_="styled__SubjectWrapper-sc-1kpvi4z-14 leTJeS").h2.a.span.text
        location = post.find_all(
            "a", class_="Link-sc-6wulv7-0 TopInfoLink__StyledLink-lzfj8j-0 dcKCyh hNTkPP")[1].text
        time = post.find("p", class_="styled__Time-sc-1kpvi4z-20 gEFkeH").text
        price = post.find(
            "div", class_="Price__StyledPrice-sc-1v2maoc-1 jVOeSj").text
        descriptionLink = post.find(
            "a", class_="Link-sc-6wulv7-0 styled__StyledTitleLink-sc-1kpvi4z-10 dcKCyh evOAPG")["href"]
        descriptionLink = "https://blocket.se" + descriptionLink
        travel = await travelCalc(location)

        # print("")
        # print("TITLE: ", title)
        # print("LOCATION: ", location)
        # print("TIME: ", time)
        # print("price: ", price)
        # print("travel: ", travel)

        data = {
            "title": title,
            "location": location,
            "time": time,
            "price": price,
            "descriptionLink": descriptionLink,
            "travel": travel
        }

        json["posts"].append(data)
        json["number_of_posts"] = number_of_posts

        print("number of posts loaded: ", number_of_posts)

        # limit the amount of posts
        if(number_of_posts >= 10):
            break
        number_of_posts += 1

    return json


def dataHanlder(posts):

    def checkDescription(url):

        keyWords = [
            "i5",
            "i7",
            "I5",
            "I7"
        ]

        keyWordMatch = 0

        r = requests.get(url).text

        html = soup(r, "lxml")

        description = html.find(
            "div", class_="TextBody__TextBodyWrapper-cuv1ht-0 GdRjz BodyCard__DescriptionPart-sc-15r463q-2 kWfegN").text

        for keyWord in keyWords:
            if(description.find(keyWord)):
                keyWordMatch += 1

        return ({
            "keyWordMatch": keyWordMatch,
            "description": description
        })

    def message(data, description):

        API_KEY = "o.RJaoJaqqdVNa5m9I6ng2F5Sh6C8LtzzQ"
        file = "history.txt"
        message = json.dumps(data, indent=3) + "\n" + description
        history = []

        f = open(file, "r")
        # if(f != ""):
        #     history = arr.array(f.read())

        if(len(history) != 0):
            for sentMessage in history:
                if(sentMessage == message):
                    return

        print("history: ", history)
        history.append(message)
        history.append(message)
        history.append(message)

        os.remove(file)

        fileString = ""
        fileString = fileString.join(history)

        print("fileString: ", fileString)
        f = open(file, "a")
        f.write(fileString)

        pb = Pushbullet(API_KEY)
        push = pb.push_note(
            "Blocket Dator Alert", message)

    for data in posts["posts"]:

        time = False
        price = False

        # generating a new price as a int
        disallowed_characters = " kr"
        priceInt = data["price"]

        for character in disallowed_characters:
            priceInt = priceInt.replace(character, "")

        priceInt = int(priceInt)

        # is the distance right?

        if "tim" in data["travel"]:
            print("more than an hour")
        else:
            time = True

        # is the price right?

        if(priceInt > 1000):
            print("to expensive")
        else:
            price = True

        # check the description for keywords

        check_description = checkDescription(data["descriptionLink"])
        keyWordMatch = str(check_description["keyWordMatch"])
        keyWordMatch = int(keyWordMatch)

        if(time and price):
            message(data, check_description["description"])
        elif (keyWordMatch > 0 and priceInt < 1000 and time):
            message(data, check_description["description"])


async def main():
    posts = await blocketScrape()

    dataHanlder(posts)

    print()
    print(posts)
    print(json.dumps(posts, indent=3))
    print("done")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
