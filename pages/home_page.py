from selenium.webdriver.common.by import By

from base_data.base_page import Page


class HomePageLocators:
    ZIP_CODE_FIELD = (By.XPATH, '//*[@id="lead-gen-zipcode"]')





class HomePage(Page):

    def click_on_zip_code(self):
        self.wait_element(HomePageLocators.ZIP_CODE_FIELD)
        zip_code= self.find_element(HomePageLocators.ZIP_CODE_FIELD)
        zip_code.click()

        return zip_code