from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com/")
time.sleep(1)
driver.maximize_window()
time.sleep(1)
search_box = driver.find_element(By.XPATH,
                                 '/html/body/ytd-app/div[1]/div/ytd-masthead/'
                                 'div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search_box.send_keys("code basics")
search_click = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div')
search_click.click()
time.sleep(3)
search_video = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/'
                                             'ytd-two-column-search-results-renderer/'
                                             'div/ytd-section-list-renderer/div[2]/'
                                             'ytd-item-section-renderer/div[3]/ytd-shelf-renderer[1]/div[1]/div[2]/'
                                             'ytd-vertical-list-renderer/div[1]/ytd-video-renderer[1]/div[1]/'
                                             'ytd-thumbnail/a/yt-image/img')
search_video.click()
time.sleep(2)

skip_ad = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/'
                                        'div/div[1]/div[2]/div/div/ytd-player/div/div/div[21]/div/div[3]/div/div[2]'
                                        '/span/button')
time.sleep(7)
skip_ad.click()
pause = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]'
                                      '/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video')
time.sleep(5)
pause.click()
