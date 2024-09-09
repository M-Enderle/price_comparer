from bs4 import BeautifulSoup
import requests

def search(term):
    base_url = "https://www.dm.de/search?query={term}&searchType=product"
    url = base_url.format(term=term.replace(" ", "%20"))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
    results = soup.find_all("div", {"data-dmid": "product-tile-container"})
    return results

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=s, options=chrome_options)

# Get the response and print title
driver.get("https://www.python.org")
print(driver.title)
driver.close()