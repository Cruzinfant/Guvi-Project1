from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pytest

# Declaring variables globally
driver = webdriver.Firefox(executable_path=r"C:\WebDriver\geckodriver1.exe")
User_name = 'cruzemperorofbac@gmail.com'
Password = 'Carrot@2318'
Q_Title = 'Guvi Python AT – 1 &2 Automation Project'
Q_Description = 'This is a Project Test Code Running for the Python Automation –1&2 Project Given by mentor Mr. Suman Gangopadhyay.'

# Creating class named Project to run test cases
class Project:
    #function for user login using credtionals
    def Login():
        # Navignating to website
        driver.get("https://www.zenclass.in/login")

        # Finding elements with Locators
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input').send_keys(
            User_name)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input').send_keys(
            Password)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button').click()
        time.sleep(3)

    #Function for Hover over the element to create Query
    def hover():
        hover = driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/nav/ul/div[1]/li/span/div/div[1]')
        hchains = ActionChains(driver)
        hchains.move_to_element(hover).perform()
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div').click()

    # Function for creating query and repeating the process for given number of times
    def query():
        query = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[1]')
        q_query = ActionChains(driver)
        q_query.move_to_element(query).perform()

        # using while loop to running script for Given Number of times
        count = 0
        while count < 5:
        # Selecting Create Query

            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[1]/div[1]/button').click()
            driver.find_element_by_xpath('//html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]').click()

        #selecting a Catogory from a drop down
            category = driver.find_element_by_name('category')
            category_Drop = Select (category)
            category_Drop.select_by_index(1)

        #selecting a Subcategory from drop down
            Sub_Category = driver.find_element_by_name('subcategory')
            Sub_Category_Drop = Select(Sub_Category)
            Sub_Category_Drop.select_by_index(1)
            time.sleep(1)

        # selecting a Language from a drop down
            language = driver.find_element_by_name('language')
            language_Drop = Select(language)
            language_Drop.select_by_index(1)
            time.sleep(2)

        #Scroll downing the page to select elements
            driver.execute_script("window.scrollBy(0,500)","")

        # Keying Query title and Description
            Query_title = driver.find_element_by_name('title').send_keys(Q_Title)
            Query_Description = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea').send_keys(Q_Description)
        #Click on Create Button
            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button').click()
            time.sleep(2)
            count = count + 1


# Calling Functions - Main Program
L1 = Project
L1.Login()
L1.hover()
L1.query()

