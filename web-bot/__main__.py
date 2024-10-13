from selenium import webdriver
import time 
DRIVER = webdriver.Firefox()


def main():
    try:
        DRIVER.get("https://www.youtube.com/")  
        time.sleep(2)
        DRIVER.find_element()
    except Exception as e:
        raise e



if __name__=="__main__":
    main()