from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def take_screenshot(url, output_path="screenshot.png"):
    """Opens a webpage and takes a screenshot."""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (no UI)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    driver.save_screenshot(output_path)
    driver.quit()

    print(f"Screenshot saved as {output_path}")

if __name__ == "__main__":
    url = input("Enter the website URL: ")
    take_screenshot(url)
