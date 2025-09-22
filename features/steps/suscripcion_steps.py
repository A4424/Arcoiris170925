# # # suscripcion_steps.py
# # #Codigo refactorizado, quita de sleep
# #
# # from behave import given, when, then
# # from pages.suscripcion_page import SuscripcionPage
# # from pages.login_page import LoginPage
# # from features.steps.login_steps import access_system_with_valid_credentials
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.common.by import By
# # from selenium.common.exceptions import TimeoutException
# #
# #
# # @given("Se tiene una sesion iniciada")
# # def step_impl(context):
# #     """
# #     Se reutiliza el paso de inicio de sesion con credenciales validas
# #     y se inicializa la pagina de suscripcion.
# #     """
# #     access_system_with_valid_credentials(context)
# #     context.suscripcion_page = SuscripcionPage(context.browser)
# #
# #
# # @when("Se hace clic en el menu hamburguesa")
# # def step_impl(context):
# #     """
# #     Se hace clic en el ícono del menú hamburguesa para desplegar las opciones.
# #     """
# #     context.suscripcion_page.click_hamburger_menu()
# #     WebDriverWait(context.browser, 10).until(
# #         EC.visibility_of_element_located((By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]"))
# #     )
# #
# #
# # @when('Se hace clic en el enlace "PERFIL"')
# # def step_impl(context):
# #     """
# #     Se hace clic en el enlace "PERFIL".
# #     """
# #     context.suscripcion_page.click_profile_link()
# #
# #
# # @then("Se muestra el contenido del perfil de usuario")
# # def step_impl(context):
# #     """
# #     Se verifica que el contenido del perfil se haya hecho visible.
# #     """
# #     profile_content_locator = (By.ID, "Perfil")
# #     try:
# #         wait = WebDriverWait(context.browser, 10)
# #         wait.until(EC.visibility_of_element_located(profile_content_locator))
# #         print("El contenido del perfil es visible.")
# #     except TimeoutException:
# #         assert False, "No se visualizó el contenido del perfil de usuario."
# #
# #
# # @when("Se activa la suscripcion para recibir promociones")
# # def step_impl(context):
# #     """
# #     Se hace clic en el checkbox de suscripción para activarlo.
# #     """
# #     context.suscripcion_page.click_subscription_checkbox()
# #     # Se agrega una espera para que el cambio de estado se refleje
# #     # antes de continuar con el siguiente paso.
# #     WebDriverWait(context.browser, 10).until(
# #         EC.element_located_selection_state_to_be(context.suscripcion_page.subscription_checkbox, True)
# #     )
# #
# #
# # @when("Se desactiva la suscripcion para recibir promociones")
# # def step_impl(context):
# #     """
# #     Se hace clic en el checkbox de suscripción para desactivarlo.
# #     """
# #     context.suscripcion_page.click_subscription_checkbox()
# #     # Se agrega una espera para que el cambio de estado se refleje
# #     # antes de continuar con el siguiente paso.
# #     WebDriverWait(context.browser, 10).until(
# #         EC.element_located_selection_state_to_be(context.suscripcion_page.subscription_checkbox, False)
# #     )
# #
# #
# # @then("Se verifica que la suscripcion esté desactivada")
# # def step_impl(context):
# #     """
# #     Se valida que el checkbox de suscripcion no este seleccionado.
# #     """
# #     subscription_checkbox = context.suscripcion_page.subscription_checkbox
# #     try:
# #         # Se verifica que el elemento no esté seleccionado
# #         assert not context.browser.find_element(*subscription_checkbox).is_selected()
# #         print("La suscripcion se ha desactivado correctamente.")
# #     except AssertionError:
# #         assert False, "La suscripcion no se desactivo. El checkbox sigue seleccionado."
# #
# #
# # @when("Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos")
# # def step_impl(context):
# #     """
# #     Se hace click en el menú hamburguesa, se espera 10 segundos
# #     y se lo vuelve a presionar para ocultar las opciones.
# #     """
# #     context.suscripcion_page.click_hamburger_menu()
# #     # Se reemplaza la espera "dura" por una espera explícita
# #     WebDriverWait(context.browser, 10).until(
# #         EC.invisibility_of_element_located((By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]"))
# #     )
# #     context.suscripcion_page.click_hamburger_menu()

# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\steps\suscripcion_steps.py

from behave import given, when, then
from pages.suscripcion_page import SuscripcionPage
from pages.login_page import LoginPage
from features.steps.login_steps import access_system_with_valid_credentials
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


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
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]"))
    )


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
    # Se agrega una espera para que el cambio de estado se refleje
    # antes de continuar con el siguiente paso.
    WebDriverWait(context.browser, 10).until(
        EC.element_located_selection_state_to_be(context.suscripcion_page.subscription_checkbox, True)
    )


@when("Se desactiva la suscripcion para recibir promociones")
def step_impl(context):
    """
    Se hace clic en el checkbox de suscripción para desactivarlo.
    """
    context.suscripcion_page.click_subscription_checkbox()
    # Se agrega una espera para que el cambio de estado se refleje
    # antes de continuar con el siguiente paso.
    WebDriverWait(context.browser, 10).until(
        EC.element_located_selection_state_to_be(context.suscripcion_page.subscription_checkbox, False)
    )


@then("Se verifica que la suscripcion esté activada")
def step_impl(context):
    """
    Se valida que el checkbox de suscripcion este seleccionado.
    """
    subscription_checkbox = context.suscripcion_page.subscription_checkbox
    try:
        # Se verifica que el elemento esté seleccionado
        assert context.browser.find_element(*subscription_checkbox).is_selected()
        print("La suscripcion se ha activado correctamente.")
    except AssertionError:
        assert False, "La suscripcion no se activo. El checkbox no esta seleccionado."


@then("Se verifica que la suscripcion esté desactivada")
def step_impl(context):
    """
    Se valida que el checkbox de suscripcion no este seleccionado.
    """
    subscription_checkbox = context.suscripcion_page.subscription_checkbox
    try:
        # Se verifica que el elemento no esté seleccionado
        assert not context.browser.find_element(*subscription_checkbox).is_selected()
        print("La suscripcion se ha desactivado correctamente.")
    except AssertionError:
        assert False, "La suscripcion no se desactivo. El checkbox sigue seleccionado."


@when("Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos")
def step_impl(context):
    """
    Se hace click en el menú hamburguesa, se espera 10 segundos
    y se lo vuelve a presionar para ocultar las opciones.
    """
    context.suscripcion_page.click_hamburger_menu()
    # Se reemplaza la espera "dura" por una espera explícita
    WebDriverWait(context.browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]"))
    )
    context.suscripcion_page.click_hamburger_menu()
