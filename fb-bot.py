from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

# Set up Facebook groups to post, you must be a member of the group
groups_links_list = [
    "https://web.facebook.com/groups/440155481477202",
    "https://web.facebook.com/groups/411371393410050",
    "https://web.facebook.com/groups/1054886042023774"
]

# Set up text content to post
message = """Use This Free Python Bot & Make $100/DAY With Affiliate Marketing For Beginners in 2022.
Link: https://youtu.be/S3NRTNU2uQ8"""

# Set up paths of images to post
photo = 'C:/Users/python/Desktop/Facebook-Group-Bot/image.jpg'

# Login Facebook
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("user-data-dir=C:\\Users\\python\\AppData\\Local\\Google\\Chrome Beta\\User Data")
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
driver = webdriver.Chrome(executable_path = "chromedriver.exe", options = options)

driver.get('https://www.facebook.com/')

def main():

    # Post on each group
    for group in groups_links_list:
        driver.get(group)
        time.sleep(3)
        driver.find_element(By.XPATH,'//span[text()="Photo/video"]').click()
        time.sleep(2)
        photo_element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input')
        photo_element.send_keys(photo)
        time.sleep(3)
        driver.find_element(By.XPATH,'//div[@class="mfn553m3"]/div').send_keys(message)
        time.sleep(2)
        post_button = driver.find_element(By.XPATH,'//div/span/span[text()="Post"]')
        post_button.click()
        time.sleep(10)

    # Close driver
    driver.close()
    print("All Data Posted Successfully!")

if __name__ == '__main__':
  main()
