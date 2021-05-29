# Module to download website into hostable package
import requests
import re

from bs4 import BeautifulSoup

def download_website(root_url):
    # Download and package website
    resp = requests.get(root_url)
    domain = [url for url in resp.cookies.list_domains() if url in root_url][0]
    soup = BeautifulSoup(resp.text)

    relative_url_regex = re.compile(r'^(/){1}.*')
    url_regex = re.compile(r'^(http|https|(/){2}).*')

    # Local files
    root_styles = soup.find_all('style', attrs={'src': relative_url_regex})
    root_scripts = soup.find_all('script', attrs={'src': relative_url_regex})
    
    # External files
    external_styles = soup.find_all('style', attrs={'src': url_regex})
    external_scripts = soup.find_all('script', attrs={'src': url_regex})
    
    # Find all links via tags: href, src
    

    return soup


