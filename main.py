from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller
from time import sleep
chromedriver_autoinstaller.install()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.get("https://deepai.org/art")
sleep(2)

while True:
    imgs = driver.find_elements_by_tag_name("img")
    with open("imagelist.txt", "a") as file:

        for img in imgs:
            src = img.get_attribute("src")
            if (not src.find("https://images.deepai.org/art-image/")):
                file.write(src+"\n")

        file.close()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
