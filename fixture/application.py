
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.chrome.options import Options


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            opts = Options()
            # opts.add_argument("--headless")
            # opts.add_argument("disable-infobars")
            self.wd = webdriver.Chrome(chrome_options=opts)
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']"))):
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']"))):
            wd.find_element_by_link_text("home page").click()

    def destroy (self):
        self.wd.quit()