from bs4 import BeautifulSoup
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
from datetime import date
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




def page_scrap_1(url,driver):
    driver.get(url) 
    cur_page_none_elements = 0
    cur_page_found_elements = 0
    print("Loading page 1...")
    time.sleep(random.randint(3,5)) 
    HTML_Source = driver.page_source
    print("Successfully loaded Page 1.")
    Soup = BeautifulSoup(HTML_Source,"html.parser")
    Soup_sorted = Soup.find_all("div",{"role":"listitem","data-asin": True,"data-component-type":"s-search-result"})
    print("Processing page 1...")

    for product_soup in Soup_sorted:
        try:
            data[product_soup.get("data-asin")] = {str(date.today()) : int(product_soup.find("span",{"class":"a-price-whole"}).text.strip().replace(",","")) }
            cur_page_found_elements+=1
        except:
            data[product_soup.get("data-asin")] = {str(date.today()) : None }
            cur_page_none_elements+=1
    print("Page 1 complete.")
    return int(Soup.find("span",{"role":"button","class":"s-pagination-item s-pagination-disabled"}).text)

def pages_scrap(url,pg_max,driver):
    cur_page = 2
    while cur_page <= pg_max:
        time.sleep(random.randint(5,9)) 
        driver.get(url+"&page="+str(cur_page))
        cur_page_none_elements = 0
        cur_page_found_elements = 0
        print(f"Loading page {cur_page}...")
        time.sleep(random.randint(2,5)) 
        HTML_Source = driver.page_source
        print(f"Successfully loaded Page {cur_page}.")

        Soup_sorted = BeautifulSoup(HTML_Source,"html.parser").find_all("div",{"role":"listitem","data-asin": True,"data-component-type":"s-search-result"})
        print(f"Processing page {cur_page}...")

        for product_soup in Soup_sorted:
            try:
                data[product_soup.get("data-asin")] = {str(date.today()) : int(product_soup.find("span",{"class":"a-price-whole"}).text.strip().replace(",","")) }
                cur_page_found_elements+=1
            except:
                data[product_soup.get("data-asin")] = {str(date.today()) : None }
                cur_page_none_elements+=1
        print(f"Page {cur_page} complete.")
        cur_page+=1




filename = input("Enter File Name (deafult data.json):")
if filename=="":
    filename="data.json"
try:
    with open(filename) as f:
        data = json.load(f)
except:
    print("File not Found,Creating New file") 
    data = {}


url = "https://www.amazon.in/s?k=" + input("Enter your search query:").strip()
initial_pg_max = input("How many pages? Press Enter for all:")
if initial_pg_max == "" or (not initial_pg_max.isdigit()):
    pass
elif int(initial_pg_max) <= 0:
    print("Pages must be at least 1. Try again")
    initial_pg_max = input("How many pages? Press Enter for all: ")


    
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
pg_max = page_scrap_1(url,driver)
if initial_pg_max=="" or (not initial_pg_max.isdigit()):
    pass
elif int(initial_pg_max)<pg_max:
    pg_max = int(initial_pg_max)
print("Scraping for",pg_max)
pages_scrap(url,pg_max,driver)
with open(filename,"w") as f:
    json.dump(data,f,indent=3)
print("Dataset Updated")