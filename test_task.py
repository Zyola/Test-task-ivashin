from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    service = Service(executable_path='/home/zyola/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_task(driver):
    driver.get('https://demoqa.com/')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    locator_01 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]')
    ActionChains(driver).move_to_element(locator_01)
    sleep(1)
    locator_01.click()
    sleep(1)
    locator_02 = driver.find_element(By.ID, 'item-1')
    locator_02.click()
    sleep(1)
    locator_03 = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label')
    locator_03.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    locator_04 = driver.find_element(By.ID, 'item-2')
    locator_04.click()
    sleep(1)
    locator_05 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label')
    locator_05.click()
    sleep(1)
    locator_06 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
    locator_06.click()
    sleep(1)
    assert 'yes' == 'yes'
