import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

def get_actual_file_url(landing_page_link):
    url = landing_page_link
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        print("Page fetched successfully. Extracting XSLX URL...")
        for file_link in soup.find_all("a"):
            file_url = file_link.get("href")
            
            if file_url and file_url.endswith(".xlsx"):
                print(f"✅ Found exact match: '{element_text}' -> {file_url} -> Success")  
                return(file_url)

    else:
        print(f"Failed to retrieve page: {response.status_code}")

try:
    elements_df = pd.read_csv("elements.csv", sep=";")

    target_names = set(elements_df["Name"].str.strip())
    print(f"Loaded {len(target_names)} element names to search for.")
except FileNotFoundError:
    print("Could not find elements.csv. Make sure you are in the right folder!")
    target_names = set()

element_links = {}
website_url = "https://www.usgs.gov/centers/national-minerals-information-center/historical-statistics-mineral-commodities-united"

response = requests.get(website_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print("Page fetched successfully. Scanning for matches...")
        
    for element in soup.find_all("a"):
            
        element_text = element.get_text().strip()
        if element_text in target_names:
            element_row = element.find_parent("tr")
            element_xlsx = element_row.find("a", string= "XLSX")
            element_url = element_xlsx.get('href')
            if not element_url.startswith('https'): 
                        element_url = "https://www.usgs.gov" + element_url 
            else:    
                pass

            actual_file = get_actual_file_url(element_url)
            element_links[element_text] = actual_file
            time.sleep(1)
    print(f"Successfully collected {len(element_links)} download links.")
else:
        print(f"Failed to retrieve page: {response.status_code}")

with open("element_links.json", "w") as file:
    json.dump(element_links, file)