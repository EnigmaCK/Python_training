from selenium.webdriver.firefox.webdriver import WebDriver


class ApplicationContact:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)






    def destroy(self):
        self.wd.quit()
