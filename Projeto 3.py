from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.ID, "name")
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.phone_field = (By.ID, "phone")
        self.register_button = (By.ID, "registerButton")
        self.success_message = (By.ID, "successMessage")

    def fill_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def fill_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def fill_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text