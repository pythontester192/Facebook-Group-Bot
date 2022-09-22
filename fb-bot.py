from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

# Set up Facebook groups to post, you must be a member of the group
groups_links_list = [
    "https://web.facebook.com/groups/440155481477202"
]

# Set up text content to post
message = """I Found the Easiest Way to Make Money on Instagram Using This Free Bot | Make Money Online 2022 !!.
Link: https://youtu.be/q_PZ5z7H2Hc"""

# Set up paths of images to post
photo = 'C:/Users/python/Desktop/Facebook-Group-Bot/image.jpg'

# Login Facebook
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("user-data-dir=C:\\Users\\python\\AppData\\Local\\Google\\Chrome Beta\\User Data")
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options = options)

driver.get('https://www.facebook.com/')

def main():

    # Post on each group
    for group in groups_links_list:
        driver.get(group)
        time.sleep(3)
        driver.find_element(By.XPATH,'//span[text()="Photo/video"]').click()
        time.sleep(2)
        photo_element = driver.find_element(By.XPATH,'//input[@type="file" and @accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
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
