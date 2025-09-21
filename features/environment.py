#environment.py

from behave.fixture import fixture, use_fixture
from selenium import webdriver
import os
from dotenv import load_dotenv

@fixture
def browser_instance(context, browser_name, headless_mode):
    """
    Se crea una instancia del navegador de forma dinámica.
    """
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
    elif browser_name == 'edge':
        options = webdriver.EdgeOptions()
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError(f"Navegador no soportado: {browser_name}")

    if headless_mode:
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")

    drivers = {
        "chrome": webdriver.Chrome,
        "edge": webdriver.Edge,
        "firefox": webdriver.Firefox
    }

    context.browser = drivers[browser_name](options=options)

    # Se maximiza la ventana del navegador si no está en modo headless
    if not headless_mode:
        context.browser.maximize_window()

    yield context.browser
    # Se cierra la instancia del navegador al finalizar
    context.browser.quit()

def before_all(context):
    """
    Se cargan las variables de entorno y se obtiene la configuración del navegador.
    """
    load_dotenv()
    context.base_url = os.getenv("BASE_URL", "http://localhost:8080")

    # Se obtienen los valores de behave.ini o línea de comandos
    context.browser_name = context.config.userdata.get('browser', 'chrome').lower()
    headless_value = context.config.userdata.get('headless', 'false').lower()
    context.headless_mode = headless_value in ("true", "1", "yes")

def before_scenario(context, scenario):
    """
    Se utiliza el fixture del navegador antes de cada escenario.
    """
    context.browser = use_fixture(
        browser_instance,
        context,
        browser_name=context.browser_name,
        headless_mode=context.headless_mode
    )

def after_scenario(context, scenario):
    """
    Se ejecutan acciones después de cada escenario.
    """
    if scenario.status == "failed":
        screenshot_name = f"screenshot_{scenario.name}.png".replace(" ", "_")
        context.browser.save_screenshot(screenshot_name)
        print(f"La prueba {scenario.name} ha fallado. Captura guardada: {screenshot_name}")

def after_all(context):
    """
    Se limpian los recursos después de todas las pruebas.
    """
    print("La ejecución de las pruebas ha finalizado.")

