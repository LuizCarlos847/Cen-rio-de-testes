from selenium import webdriver
from pages.registration_page import RegistrationPage
from utils.config import BASE_URL_WEB

def test_registration_all_fields():
    driver = webdriver.Chrome()
    driver.get(f"{BASE_URL_WEB}/register")
    
    page = RegistrationPage(driver)
    page.fill_name("João Silva")
    page.fill_email("joao@example.com")
    page.fill_password("Senha@123")
    page.fill_phone("123456789")
    page.click_register_button()
    
    assert page.get_success_message() == "Cadastro realizado com sucesso"
    driver.quit()