# Ruta: suscription_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os


class SuscripcionPage:
    def __init__(self, browser):
        self.browser = browser

        # Localizadores para el menú y el enlace de perfil
        self.hamburger_menu = (By.CSS_SELECTOR, 'div.menu-wrap input.toggler')
        self.profile_link = (By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]")

        # Localizador para el checkbox de suscripción usando el label.switch
        self.subscription_checkbox = (By.CSS_SELECTOR, "label.switch")

    def click_hamburger_menu(self):
        """
        Se hace clic en el ícono del menú hamburguesa utilizando JavaScript
        para evitar problemas de elementos cubiertos o de visibilidad.
        """
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.hamburger_menu)
        )
        self.browser.execute_script("arguments[0].click();", element)

    def click_profile_link(self):
        """
        Se hace clic en el enlace "PERFIL" utilizando JavaScript para evitar
        problemas de elementos interceptados o de sincronización.
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.profile_link)
        )
        self.browser.execute_script("arguments[0].click();", element)

    def click_subscription_checkbox(self):
        """
        Se hace clic en el checkbox de suscripción.
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.subscription_checkbox)
        )
        element.click()
