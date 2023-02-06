from selenium import webdriver
from time import sleep
import yaml
from yaml.loader import SafeLoader

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

class MinervaBot:

    TIME_INTERVAL = 300
    TIME_WAIT = 2

    def __init__(self): 
        # start driver
        self.driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/redha/webdrivers/chromedriver.exe')
        # get info from yaml config
        with open("password.yml") as f:
            conf = yaml.load(f, Loader=SafeLoader)
            self.minerva_email = conf['minerva_user']['email']
            self.minerva_pass = conf['minerva_user']['password']
            # CRNS
            self.crn = []
            self.crn.append(conf['CRN']["lecture"])
            self.crn.append(conf['CRN']["lab_t"])
            self.crn.append(conf['CRN']["lab_w"])
            
    def login(self):
        self.driver.get("https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin")
        self.driver.implicitly_wait(10)
        user = self.driver.find_element_by_xpath('//*[@id="mcg_un"]')
        passw = self.driver.find_element_by_xpath('//*[@id="mcg_pw"]')
        enter = self.driver.find_element_by_xpath('//*[@id="mcg_un_submit"]')
        user.send_keys(self.minerva_email)
        passw.send_keys(self.minerva_pass)
        enter.click()
    
    def goToQuickAdd(self):
        '''
        Go to quick add page from the home page
        '''
        student_menu = self.driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a')
        student_menu.click()
        sleep(MinervaBot.TIME_WAIT)

        registration_menu = self.driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a')
        registration_menu.click()
        sleep(MinervaBot.TIME_WAIT)

        quick_add = self.driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a')
        quick_add.click()
        sleep(MinervaBot.TIME_WAIT)

        term = self.driver.find_element_by_xpath('/html/body/div[3]/form/input')
        term.click()
        sleep(MinervaBot.TIME_WAIT)
    
    def register(self):
        while True:
            self.register_crns()
            sleep(MinervaBot.TIME_WAIT)
            self.submit_changes()
            sleep(MinervaBot.TIME_INTERVAL)

    def submit_changes(self): 
        submit_changes = self.driver.find_element_by_xpath('/html/body/div[3]/form/input[19]')
        submit_changes.click()

    def register_crns(self):
        crn_id = 1
        doLoop = True
        if doLoop:
            for crn_course_id in self.crn:
                crn_xpath = f'/html/body/div[3]/form/table[3]/tbody/tr[2]/td[{crn_id}]/input[2]'
                crn_selector = f'#crn_id{crn_id}'
                crn_box = self.driver.find_element_by_xpath(crn_xpath)
                #crn_box = self.driver.find_element_by_css_selector(crn_selector)
                crn_box.send_keys(str(crn_course_id))
                crn_id += 1
        
        submit_changes = self.driver.find_element_by_xpath('/html/body/div[3]/form/input[19]')
        submit_changes.click()