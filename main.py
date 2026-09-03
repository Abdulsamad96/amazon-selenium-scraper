from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


file = 0
driver = webdriver.Chrome()
query = "laptop"


for i in range(1,5):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1NZ8DE921VF75&qid=1788430832&sprefix=laptop%2Caps%2C269&xpid=tWmKT_suSqpRq&ref=sr_pg_2")
    elems = driver.find_elements(By.CLASS_NAME,"puisg-col-inner")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w", encoding="utf-8" ) as f:
            f.write(d)
            file += 1

time.sleep(2)
#print(len(elems))
driver.close()


