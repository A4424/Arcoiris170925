# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\steps\login_steps.py
# 150925 -14:50
from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
import time

@given("Se esta en la pagina de inicio de sesion")
def step_impl(context):
    """
    Se inicializa la pagina de login y se navega a la URL.
    """
    context.login_page = LoginPage(context.browser)
    context.login_page.navigate()

@when('Se ingresan las credenciales validas')
def step_impl(context):
    """
    Se obtienen las credenciales desde el archivo .env y se ingresan.
    """
    username = os.getenv("VALID_USERNAME")
    password = os.getenv("VALID_PASSWORD")
    context.login_page.enter_credentials(username, password)

@when('Se ingresa el usuario "{username}" y la contrasena "{password}"')
def step_impl(context, username, password):
    """
    Se ingresan el usuario y la contrasena proporcionados en el escenario.
    """
    user = os.getenv(username) if username in os.environ else username
    passw = os.getenv(password) if password in os.environ else password

    context.login_page.enter_credentials(user, passw)

@when("Se hace clic en el boton de Ingresar")
def step_impl(context):
    """
    Se hace clic en el botón de ingreso.
    """
    context.login_page.click_login_button()

@then("Se es redirigido a la pagina de inicio")
def step_impl(context):
    """
    Se verifica que la URL actual sea la de la página de inicio.
    """
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.invisibility_of_element_located(context.login_page.login_button))

        print(f"Redireccion exitosa. URL actual: {context.browser.current_url}")

    except TimeoutException:
        assert False, "No se produjo una redireccion a la pagina de inicio."

@then("Se muestra un mensaje de error de credenciales invalidas")
def step_impl(context):
    """
    Se verifica la visibilidad y el contenido del mensaje de error.
    Luego se hace clic en el botón 'Aceptar' del modal para volver al login.
    """
    error_message_locator = (By.ID, "swal2-html-container")
    accept_button_locator = (By.CSS_SELECTOR, "button.swal2-confirm")

    try:
        wait = WebDriverWait(context.browser, 10)
        error_message_element = wait.until(
            EC.visibility_of_element_located(error_message_locator)
        )

        actual_text = error_message_element.text
        expected_messages = ["Clave Usuario Invalida.!!", "Usuario Inexistente.!!"]

        if any(msg in actual_text for msg in expected_messages):
            print(f"Mensaje de error validado: {actual_text}")
        else:
            assert False, f"El mensaje de error no es el esperado. Se encontró: {actual_text}"

        accept_button = wait.until(EC.element_to_be_clickable(accept_button_locator))
        accept_button.click()
        print("Se hizo clic en el botón 'Aceptar' y se volvió a la pantalla inicial.")

    except TimeoutException:
        assert False, "El mensaje de error o el botón 'Aceptar' no fueron visibles en el tiempo de espera."

@when("Se hace clic en el icono de usuario")
def step_impl(context):
    """
    Se hace clic en el icono de usuario para mostrar el modal de cerrar sesión.
    """
    context.login_page.click_logout_arrow()

@then("Se muestra la ventana modal de cerrar sesion")
def step_impl(context):
    """
    Se verifica que la ventana modal de cerrar sesión sea visible.
    """
    modal_locator = (By.CLASS_NAME, "swal2-modal")
    try:
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(modal_locator)
        )
        print("La ventana modal de cerrar sesión es visible.")
    except TimeoutException:
        assert False, "La ventana modal de cerrar sesión no se hizo visible."

@when("Se hace clic en el boton Aceptar del modal")
def step_impl(context):
    """
    Se hace clic en el botón 'Aceptar' del modal de cerrar sesión.
    """
    context.login_page.accept_logout()

@when("Se hace clic en el boton Cancelar del modal")
def step_impl(context):
    """
    Se hace clic en el botón 'Cancelar' del modal de cerrar sesión.
    """
    context.login_page.cancel_logout()

@then("Se es redirigido a la pagina de inicio de sesion")
def step_impl(context):
    """
    Se verifica que la URL actual sea la de la página de inicio de sesión.
    """
    expected_url = context.login_page.url + "Login.php"
    try:
        WebDriverWait(context.browser, 10).until(
            EC.url_to_be(expected_url)
        )
        print(f"Redireccion exitosa. La URL actual es: {context.browser.current_url}")
    except TimeoutException:
        assert False, f"No se produjo una redireccion a la pagina de inicio de sesion. La URL actual es: {context.browser.current_url}"

@then("Se permanece en la pagina de inicio")
def step_impl(context):
    """
    Se verifica que la URL actual no haya cambiado.
    """
    current_url = context.browser.current_url
    expected_url_part = "Home.php"

    if expected_url_part not in current_url:
        assert False, f"No se permaneció en la página de inicio. Se redirigió a: {current_url}"
    else:
        print("Se permaneció en la página de inicio.")
