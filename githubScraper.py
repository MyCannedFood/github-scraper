from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

repo_paths = []
file_paths = []
sub_page = []

target_url = input("Target url: ")
target_key = input("Target key: ")

def content_page(page):
    driver.get(page)
    
    raw = driver.find_element(By.LINK_TEXT, "Raw") 
    raw.click()
    
    html = driver.page_source
    if target_key in html:
        print(f"Found {target_key} in {page}")
    else:
        return 

def files_page(page):
    
    driver.get(page)
    files = driver.find_elements(By.CLASS_NAME, "react-directory-truncate")
    
    for file in files:
        file_paths.append(file.text)
        print(file_paths)

    for path in file_paths:
        if path != "":
            url = f"{page}/blob/main/{path}"
            print(url)

            content_page(url)

driver.get(target_url)
repos = driver.find_elements(By.CLASS_NAME, "repo")

for repo in repos:
    repo_paths.append(repo.text)
print(repo_paths)

for path in repo_paths:
    url = f"{target_url}/{path}"
    print(url)
    
    sub_page.append(url)

    files_page(url)
     
driver.quit()
