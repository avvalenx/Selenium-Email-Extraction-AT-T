from locator import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

#pass the driver in from main so that I can get things from the page
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class login(BasePage):
    def login(self):
        username = self.driver.find_element(*LoginLocators.attuid)
        password = self.driver.find_element(*LoginLocators.password)
        log_on_button = self.driver.find_element(*LoginLocators.log_on)
        username.send_keys()#username and password removed
        password.send_keys()
        log_on_button.click()
        try:
            continue_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(LoginLocators.continue_button))
            continue_button.click()
        except Exception:
            print('unable to login')
        

class PonderPage(BasePage):
    def campaign_selection(self):
        #State Selection
        try:
            time.sleep(5)
            print('start')
            state = Select(WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PonderLocators.state_dropdown)))
            print('state identified')
            #select state
            state.select_by_value('MN')
            print('state clicked')
        except Exception as err:
            print('error selecting state')
            print(err)

        #Campaign Selection
        try:
            #depending on how many zip codes a state has will affect this loading time
            #ex california has the most amount of zips and 10 seconds is not enough time
            #had to up wait time from 10 seconds to 20 because Ponder is very slow for states with large zip codes like CA
            campaign = Select(WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(PonderLocators.campaign_dropdown)))
            #select campaign
            campaign.select_by_value('1-33735165693')
        except Exception as err:
            print('error selecting zip code:')
            print('zip code: ')
            print(err)
        
        #find number of zip codes to iterate through
        #return that number
    
    def number_of_zips(self):
        try:
            #can not wait for zip selector to be clickable or on page because it is clickable even when campaign is loaded
            time.sleep(10)
            #that is why this wait time must be hardcoded
            num_zips = self.driver.find_elements(*PonderLocators.num_zips)
            return len(num_zips)
        except Exception:
            print('error finding number of zip codes')

    def zip_email_extract_loop(self, zip_code):
        #Zip code selection     
        time.sleep(.5)       
        try:
            zips = Select(WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(PonderLocators.zip_dropdown)))
            zips.select_by_index(zip_code)
        except Exception as err:
            print('error selecting zip code:')
            print('zip code: ', zip_code)
            print(err)
        
        #clicking the submit button
        time.sleep(2)
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PonderLocators.submit))
            submit_button.click()
        except Exception as err:
            try:
                submit_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(PonderLocators.submit))
                submit_button.click()
            except Exception as err:
                print('error clicking submit button')
                print('zip code: ', zip_code)
                print(err)
        
        #clicking Blue 500 Table Button
        time.sleep(.5)
        try:
            table_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(PonderLocators.top500_button))
            table_button.click()
        except Exception as err:
            try:
                table_button = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable(PonderLocators.top500_button))
                table_button.click()
            except Exception as err:
                print('error clicking blue 500 table button')
                print('zip code: ', zip_code)
                print(err)
        
        #getting emails from table
        time.sleep(.5)
        try:
            detect_email_table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PonderLocators.email_table))
            emails = [email.text for email in WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(PonderLocators.emails))]
        except Exception as err:
            print('error getting emails from table')
            print('zip code: ', zip_code)
            print(err)
        
        #close the email table
        time.sleep(.5)
        try:
            close_table = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PonderLocators.close_button))
            close_table.click()
        except Exception as err:
            print('error closing email table')
            print('zip code: ', zip_code)
            print(err)
        
        #return email list
        try:
            return emails
        except Exception:
            print('email list empty')
