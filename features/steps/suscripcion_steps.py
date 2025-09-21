# # Ruta:suscripcion_steps.py
#
# from behave import given, when, then
# from pages.suscripcion_page import SuscripcionPage
# from pages.login_page import LoginPage
# from features.steps.login_steps import access_system_with_valid_credentials
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# import time
#
#
# @given("Se tiene una sesion iniciada")
# def step_impl(context):
#     """
#     Se reutiliza el paso de inicio de sesion con credenciales validas
#     y se inicializa la pagina de suscripcion.
#     """
#     access_system_with_valid_credentials(context)
#     context.suscripcion_page = SuscripcionPage(context.browser)
#
#
# @when("Se hace clic en el menu hamburguesa")
# def step_impl(context):
#     """
#     Se hace clic en el ícono del menú hamburguesa para desplegar las opciones.
#     """
#     context.suscripcion_page.click_hamburger_menu()
#
#
# @when('Se hace clic en el enlace "PERFIL"')
# def step_impl(context):
#     """
#     Se hace clic en el enlace "PERFIL".
#     """
#     context.suscripcion_page.click_profile_link()
#
#
# @then("Se muestra el contenido del perfil de usuario")
# def step_impl(context):
#     """
#     Se verifica que el contenido del perfil se haya hecho visible.
#     """
#     profile_content_locator = (By.ID, "Perfil")
#     try:
#         wait = WebDriverWait(context.browser, 10)
#         wait.until(EC.visibility_of_element_located(profile_content_locator))
#         print("El contenido del perfil es visible.")
#     except TimeoutException:
#         assert False, "No se visualizó el contenido del perfil de usuario."
#
#
# @when("Se activa la suscripcion para recibir promociones")
# def step_impl(context):
#     """
#     Se hace clic en el checkbox de suscripción para activarlo.
#     """
#     context.suscripcion_page.click_subscription_checkbox()
#
#
# @when("Se desactiva la suscripcion para recibir promociones")
# def step_impl(context):
#     """
#     Se hace clic en el checkbox de suscripción para desactivarlo.
#     """
#     context.suscripcion_page.click_subscription_checkbox()
#
#
# @when("Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos")
# def step_impl(context):
#     """
#     Se hace click en el menú hamburguesa, se espera 10 segundos
#     y se lo vuelve a presionar para ocultar las opciones.
#     """
#     context.suscripcion_page.click_hamburger_menu()
#     print("Esperando 10 segundos...")
#     time.sleep(10)
#     context.suscripcion_page.click_hamburger_menu()


#Codigo con demora, luego quitar el sleep

# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\steps\suscripcion_steps.py

from behave import given, when, then
from pages.suscripcion_page import SuscripcionPage
from pages.login_page import LoginPage
from features.steps.login_steps import access_system_with_valid_credentials
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


@given("Se tiene una sesion iniciada")
def step_impl(context):
    """
    Se reutiliza el paso de inicio de sesion con credenciales validas
    y se inicializa la pagina de suscripcion.
    """
    access_system_with_valid_credentials(context)
    context.suscripcion_page = SuscripcionPage(context.browser)


@when("Se hace clic en el menu hamburguesa")
def step_impl(context):
    """
    Se hace clic en el ícono del menú hamburguesa para desplegar las opciones.
    """
    context.suscripcion_page.click_hamburger_menu()


@when('Se hace clic en el enlace "PERFIL"')
def step_impl(context):
    """
    Se hace clic en el enlace "PERFIL".
    """
    context.suscripcion_page.click_profile_link()


@then("Se muestra el contenido del perfil de usuario")
def step_impl(context):
    """
    Se verifica que el contenido del perfil se haya hecho visible.
    """
    profile_content_locator = (By.ID, "Perfil")
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.visibility_of_element_located(profile_content_locator))
        print("El contenido del perfil es visible.")
    except TimeoutException:
        assert False, "No se visualizó el contenido del perfil de usuario."


@when("Se activa la suscripcion para recibir promociones")
def step_impl(context):
    """
    Se hace clic en el checkbox de suscripción para activarlo.
    """
    context.suscripcion_page.click_subscription_checkbox()
    time.sleep(5)


@when("Se desactiva la suscripcion para recibir promociones")
def step_impl(context):
    """
    Se hace clic en el checkbox de suscripción para desactivarlo.
    """
    context.suscripcion_page.click_subscription_checkbox()
    time.sleep(5)


@when("Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos")
def step_impl(context):
    """
    Se hace click en el menú hamburguesa, se espera 10 segundos
    y se lo vuelve a presionar para ocultar las opciones.
    """
    context.suscripcion_page.click_hamburger_menu()
    print("Esperando 10 segundos...")
    time.sleep(10)
    context.suscripcion_page.click_hamburger_menu()
    time.sleep(10)