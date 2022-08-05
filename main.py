from selenium import webdriver
from locator import PonderLocators
import page
import pandas as pd
import openpyxl

class Ponder_SetUp():
    #open the correct page and log in to ponder
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.driver.get('https://ponder.web.att.com/sales/Sales_National_Wireless_Campaign.aspx')
        self.driver.maximize_window()
        login = page.login(self.driver)
        login.login()
        
class Ponder_Emails():
    def email_campaign(self):
        ponder_set_up = Ponder_SetUp()
        ponder_set_up.setUp()
        ponder = page.PonderPage(ponder_set_up.driver)
        ponder.campaign_selection()
        zip_num = ponder.number_of_zips()
        #zip_num = 3

        #loop to iterate through every zip code
        email_list = []
        for num in range(1, zip_num):
            if num % 100 == 0:
                ponder_set_up.driver.close()
                ponder_set_up.setUp()
                ponder = page.PonderPage(ponder_set_up.driver)
                ponder.campaign_selection()
            try:
                for email in ponder.zip_email_extract_loop(num):
                    if email != 'abc@att.com' and email != '':
                        email_list.append(email)
            except Exception:
                print('error retrieving email list for zip number', num)

        #put into excel
        df = pd.DataFrame(email_list)
        df.to_excel('email_output.xlsx', sheet_name='emails', index='none')
        print('success')

if __name__ == '__main__':
    main = Ponder_Emails()
    main.email_campaign()
