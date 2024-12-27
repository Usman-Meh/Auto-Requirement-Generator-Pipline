from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set up Selenium WebDriver (this example uses Chrome)
# Make sure to replace the path with where your chromedriver is located
driver_path = 'path_to_your_chromedriver'
driver = webdriver.Chrome()

# URL of the page to scrape
url = "https://you.ubc.ca/programs/#mode=by-program&viewMode=list"

# Open the page using Selenium
driver.get(url)

# Wait for the JavaScript to load the content (you may need to adjust the sleep time)
time.sleep(5)

# Get the page source after JavaScript has rendered the content
page_source = driver.page_source

# Use BeautifulSoup to parse the dynamically loaded content
soup = BeautifulSoup(page_source, 'html.parser')


name=[]
link=[]
# Find all program sections
program_sections = soup.find_all('li', class_='program-section-control')

# Extracting program names and links
for section in program_sections:
    
    program_name_tag = section.find('span', class_='program-name').find('a')
    print(program_name_tag)
    if program_name_tag:
        
        program_name = program_name_tag.get_text(strip=True)
        program_link = program_name_tag['href']
        print(f"Program Name: {program_name}")
        print(f"Program Link: {program_link}\n")
        name.append(program_name)
        link.append(program_link)
        

# Close the Selenium WebDriver
driver.quit()
dic={'Program Name':program_name,'Links':program_link}
df =pd.DataFrame(dic)
df.to_csv("British Columbia.csv")