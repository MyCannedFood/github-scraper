from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

target_url = input("Target profile: ").strip()
target_key = input("Target search key: ").strip()

def check_content(file_url):
    try:
        driver.get(file_url)
        # Wait for the Raw button and click it
        raw_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Raw")))
        raw_btn.click()
        
        time.sleep(1) 
        content = driver.page_source
        
        if target_key in content:
            print(f"[!] FOUND: '{target_key}' in {file_url}")
        else:
            print(f"[-] Not found in: {file_url}")
    except Exception as e:
        print(f"[X] Error checking file {file_url}: {e}")

def scrape_repo(repo_url):
    print(f"\n[*] Scanning Repository: {repo_url}")
    driver.get(repo_url)
    
    try:
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.Link--primary")))
        links = driver.find_elements(By.CSS_SELECTOR, "a.Link--primary")
        
        file_urls = []
        for link in links:
            href = link.get_attribute("href")
            # We specifically want files (blobs), not directories (trees) or other links
            if "/blob/" in href:
                file_urls.append(href)
        
        for url in file_urls:
            check_content(url)
            
    except Exception as e:
        print(f"[X] Could not parse file list for {repo_url}: {e}")

def main():
    try:
        # Normalize URL to ensure we start at the repositories tab for profiles
        url = f"https://github.com/{target_url}"
        if "/?tab=" not in url and not url.endswith("/repositories"):
            if "github.com/" in url and len(url.split("/")) <= 5: # Likely a profile or organization
                url = url.rstrip("/") + "?tab=repositories"
        
        print(f"[*] Navigating to: {url}")
        driver.get(url)
        
        print("[*] Discovering repositories...")
        selectors = [
            "a[itemprop='name codeRepository']",
            "h3.wb-break-all > a",
            ".repo"
        ]
        
        repo_urls = []
        for selector in selectors:
            try:
                # Short wait for each attempt
                elements = WebDriverWait(driver, 3).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
                )
                for el in elements:
                    href = el.get_attribute("href")
                    if href and "/repositories" not in href and "/stargazers" not in href:
                        repo_urls.append(href)
                if repo_urls: break
            except:
                continue
        
        repo_urls = list(set(repo_urls)) # Unique URLs
        print(f"[*] Found {len(repo_urls)} repositories.")
        
        if not repo_urls:
            print("[!] No repositories found. Please check if the URL is correct or if the profile is public.")
            return

        for url in repo_urls:
            scrape_repo(url)
            
    except Exception as e:
        print(f"[X] Critical error in main: {e}")
    finally:
        print("\n[*] Search complete. Closing driver.")
        driver.quit()

if __name__ == "__main__":
    main()
