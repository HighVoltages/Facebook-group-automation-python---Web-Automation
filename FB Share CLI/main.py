# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Your Facebook account user and password
    usr = ""
    pwd = ""
    message = " A well written blog on Arduino and ESP based smart farms . \n https://highvoltages.co/tutorial/iot/smart-farms-generating-techno-environmental-awareness/"
    ESP_groups = [
        "https://www.facebook.com/groups/1606743019578078/",
        "https://www.facebook.com/groups/225344424562317/",
        "https://www.facebook.com/groups/1499045113679103/",
        "https://www.facebook.com/groups/esp8266microcontrollers/",
        "https://www.facebook.com/groups/iotkorea/",
        "https://www.facebook.com/groups/sentryrobotic/",
        "https://www.facebook.com/groups/1591467384241011/",
        "https://www.facebook.com/groups/esp32/",
        "https://www.facebook.com/groups/114529885735280/",
        "https://www.facebook.com/groups/1589882334589841/",
        "https://www.facebook.com/groups/2151472251796152/",
        "https://www.facebook.com/groups/1662727464024349/"

    ]
    group_links = [
        "https://www.facebook.com/groups/561180407231568/",
        "https://www.facebook.com/groups/240863119375683/",
        "https://www.facebook.com/groups/454412428335321/",
        "https://www.facebook.com/groups/486047504879195/",
        "https://www.facebook.com/groups/431097293746148/",
        "https://www.facebook.com/groups/131503140828474/",
        "https://www.facebook.com/groups/176893525672427/",
        "https://www.facebook.com/groups/573098119472942/",
        "https://www.facebook.com/groups/269937353205461/",
        "https://www.facebook.com/groups/241505052527689/",
        "https://web.facebook.com/groups/34290916408",
        "https://web.facebook.com/groups/617651401610974/",
        "https://web.facebook.com/groups/915747211849855/",
        "https://web.facebook.com/groups/409479222596652/",





    ]



    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("-headless")
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(15)  # seconds

    # Go to facebook.com
    driver.get("http://www.facebook.com")

    # Enter user email
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    # Enter user password
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    # Login
    elem.send_keys(Keys.RETURN)

    for group in group_links:

        # Go to the Facebook Group
        driver.get(group)

        # Click the post box
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

        # Enter the text we want to post to Facebook
        post_box.send_keys(message)

        sleep(10)
        buttons = driver.find_elements_by_tag_name("button")
        sleep(5)
        for button in buttons:
            if button.text == "Post":
                sleep(10)
                button.click()
                sleep(10)

    # driver.close()


if __name__ == '__main__':
    main()
