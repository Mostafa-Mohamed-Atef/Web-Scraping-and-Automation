from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
DRIVER = webdriver.Firefox()

def searching_song(search_bar, search_btn):
    try:
        # Wait for the search bar to be visible and interactable
        WebDriverWait(DRIVER, 10).until(
            EC.visibility_of(search_bar)
        )
        
        # Clear any existing text (if needed) and enter the search query
        search_bar.clear()  # Clear any existing input (optional)
        search_bar.send_keys("Never Gonna Give You Up")
        
        # Wait for the search button to be clickable and click it
        WebDriverWait(DRIVER, 10).until(
            EC.element_to_be_clickable(search_btn)
        )
        search_btn.click()
        
        # Define the XPath for the video title
        video_xpath = '//a[@id="video-title" and @title="Rick Astley - Never Gonna Give You Up (Official Music Video)"]'
        
        # Wait for the video to appear and then click it
        video_element = WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located((By.XPATH, video_xpath))
        )
        print("Video located.")

        # Click the video
        video_element.click()
        print("Clicked on the video.")

    except Exception as e:
        print(f"An error occurred during search: {e}")

def main():
    try:
        # Open YouTube
        DRIVER.get("https://www.youtube.com/")
        
        # Locating the search bar and button
        search_bar = WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="search"]'))
        )
        print("Search bar located.")

        search_btn = WebDriverWait(DRIVER, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@id="search-icon-legacy"]'))
        )
        print("Search button located.")
        
        # Perform the search
        searching_song(search_bar, search_btn)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
