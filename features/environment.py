# Archivo environment.py

from selenium import webdriver
from behave import fixture, use_fixture
import os
from dotenv import load_dotenv
import time

@fixture
def browser_chrome(context):
    """
    Se crea una instancia del navegador Chrome.
    """
    context.browser = webdriver.Chrome()

    # Se maximiza la ventana del navegador
    context.browser.maximize_window()

    yield context.browser
    # Se cierra la instancia del navegador al finalizar el escenario.
    context.browser.quit()

def before_all(context):
    """
    Se cargan las variables de entorno desde el archivo .env.
    """
    load_dotenv()
    context.base_url = os.getenv("BASE_URL")

def before_scenario(context, scenario):
    """
    Se utiliza el fixture del navegador antes de cada escenario.
    """
    use_fixture(browser_chrome, context)

def after_scenario(context, scenario):
    """
    Se limpian los recursos después de cada escenario.
    """
    pass

def after_scenario(context, scenario):
    """
    Se ejecuta despues de cada escenario.
    """
