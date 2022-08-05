from selenium.webdriver.common.by import By

class LoginLocators(object):
    attuid = (By.ID, 'GloATTUID')
    password = (By.ID, 'GloPassword')
    log_on = (By.ID, 'GloPasswordSubmit')
    continue_button = (By.ID, 'successButtonId')

class PonderLocators(object):
    state_dropdown = (By.ID, 'ContentPlaceHolder1_ddlState')
    zip_dropdown = (By.ID, 'ContentPlaceHolder1_ddlZip')
    num_zips = (By.XPATH, '//*[@id="ContentPlaceHolder1_ddlZip"]/option')
    campaign_dropdown = (By.ID, 'ContentPlaceHolder1_ddlCampaign')
    submit = (By.ID, 'ContentPlaceHolder1_SubmitButton')
    top500_button = (By.XPATH, '//*[@id="national_datatable_wrapper"]/div[1]/button[1]')
    email_table = (By.TAG_NAME, 'tbody')
    emails = (By.XPATH, '//*[@id="showDataModal_table"]/tbody/tr/td[16]')
    close_button = (By.XPATH, '//*[@id="m_modal_showData"]/div/div/div[1]/button')

class FastLocators(object):
    search_bar = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/div/div/div[1]/div[2]/input[3]')
    search_button = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/form/div/div/div[2]/button')
    account_link = (By.XPATH, '/html/body/div[2]/div/div/div[3]/div/form/div[2]/table/tbody/tr/td[3]/div/a')
    customer_contacts = (By.XPATH, '/html/body/div[2]/div/div/span/div[1]/ul/li[4]/a')
    contact_name = (By.XPATH, '/html/body/div[2]/div/div/span/div[2]/form[1]/table/tbody/tr/td[1]/div')
    contact_type = (By.XPATH, '/html/body/div[2]/div/div/span/div[2]/form[1]/table/tbody/tr/td[2]/div')
    contact_email = (By.XPATH, '/html/body/div[2]/div/div/span/div[2]/form[1]/table/tbody/tr/td[3]/div')
    contact_phone = (By.XPATH, '/html/body/div[2]/div/div/span/div[2]/form[1]/table/tbody/tr/td[10]/div')
    contact_day = (By.XPATH, '/html/body/div[2]/div/div/span/div[2]/form[1]/table/tbody/tr/td[6]/div')
    home_button = (By.XPATH, '/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a')
