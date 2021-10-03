from helium import *
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.carrefour.es/"

def get_data(url_sample):
    Browser = start_chrome(url, headless=True)
    browser_ = Browser.page_source
    soup  = BeautifulSoup(browser_,"html.parser")
    return soup

def link_library(soup):
    href_list = []
    hrefs = soup.find_all("a", {"class":"text-banner__link track-click"})
    w = "https://www.carrefour.es"
    for i in hrefs:
        i = i.get("href")
        href_list.append(i)
    href_list_remove = []
    for y in href_list:
        href_list_remove.append(y.replace(w,""))
    perfect_href_list = []
    for adds in href_list_remove:
        perfect_href_list.append(w + adds)
    return perfect_href_list

a = get_data(url)
print(link_library(a))
