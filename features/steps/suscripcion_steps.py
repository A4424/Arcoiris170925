#Steps
from behave import given, when, then
from pages.suscripcion_page import SuscripcionPage
from features.steps.login_steps import access_system_with_valid_credentials
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time


@given("Se tiene una sesion iniciada")
def step_impl(context):
    """
    Se reutiliza el login con credenciales válidas y se inicializa la página de suscripción.
    """
    access_system_with_valid_credentials(context)
    context.suscripcion_page = SuscripcionPage(context.browser)


@when("Se hace clic en el menu hamburguesa")
def step_impl(context):
    """
    Se hace clic en el ícono de menú hamburguesa y se espera a que aparezca el enlace PERFIL.
    """
    context.suscripcion_page.click_hamburger_menu()
    # Se espera que el enlace de PERFIL sea visible tras abrir el menú
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]"))
    )


@when('Se hace clic en el enlace "PERFIL"')
def step_impl(context):
    """
    Se hace clic en el enlace PERFIL.
    """
    context.suscripcion_page.click_profile_link()


@then("Se muestra el contenido del perfil de usuario")
def step_impl(context):
    """
    Se verifica que el contenido del perfil sea visible.
    """
    profile_content_locator = (By.ID, "Perfil")
    try:
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(profile_content_locator)
        )
        print("El contenido del perfil es visible.")
    except TimeoutException:
        assert False, "No se visualizó el contenido del perfil de usuario."


@when('Se actualiza la suscripcion a promociones a "{estado}"')
def step_impl(context, estado):
    """
    Se edita el perfil y se activa o desactiva el toggle de suscripción según el estado deseado.
    Este paso solo gestiona el toggle y la interacción con el botón de Edición.
    """
    activar = True if estado.lower() == "activada" else False

    # 1. Click en Editar
    context.suscripcion_page.click_edit_button()
    # Se añade una pequeña pausa para asegurar que el DOM se prepare tras la edición
    time.sleep(1)

    # 2. Loop para manejar posibles StaleElementReference (se mantiene el reintento)
    for attempt in range(3):
        try:
            # Localizar checkbox y slider (usando el ID del checkbox)
            checkbox = WebDriverWait(context.browser, 10).until(
                lambda driver: driver.find_element(By.ID, "FProCheck")
            )
            # Localizar el elemento visible al que se debe hacer clic (el slider/toggle)
            slider_locator = (By.CSS_SELECTOR, "#FProCheck + span.slider.round")
            slider = context.browser.find_element(*slider_locator)

            # Scroll al slider para asegurar visibilidad antes del clic
            context.browser.execute_script("arguments[0].scrollIntoView(true);", slider)

            # Click solo si el estado no coincide con el deseado
            if checkbox.is_selected() != activar:
                # Se utiliza ActionChains para el clic, lo que a menudo es más robusto para sliders
                ActionChains(context.browser).move_to_element(slider).click().perform()
                # Se añade una pausa corta tras el clic para permitir que la interfaz reaccione
                time.sleep(1)

                # Si el clic fue exitoso, se sale del bucle
            break

        except StaleElementReferenceException:
            print(f"Intento {attempt + 1}: Elemento desactualizado, reintentando...")
            time.sleep(1)
        except Exception as e:
            # Captura cualquier otra excepción (como Timeout) para que no se oculte
            print(f"Ocurrió un error al interactuar con el slider: {e}")
            raise

            # Se lanza una excepción si el bucle falla después de 3 intentos
    if attempt == 2 and checkbox.is_selected() != activar:
        assert False, f"Fallo al cambiar el estado del slider a '{estado}' después de 3 intentos."


@when("Se hace click en el boton aceptar")
def step_impl(context):
    """
    Se hace clic en el botón Aceptar para guardar los cambios, usando la lógica del Page Object.
    """
    # Se hace uso del método encapsulado en el Page Object.
    # El Page Object maneja la espera, el localizador correcto (CSS Selector) y el manejo de TimeoutException.
    context.suscripcion_page.click_accept_button()
    time.sleep(1)  # Pequeña pausa para permitir que la página reaccione al guardado


@then('Se verifica que la suscripcion esté activada')
def step_impl(context):
    """
    Se valida que el checkbox esté marcado (activado).
    """
    # Se utiliza el localizador del Page Object para el checkbox
    checkbox_locator = context.suscripcion_page.subscription_checkbox
    try:
        # Se espera hasta 20 segundos para la selección
        WebDriverWait(context.browser, 20).until(
            EC.element_located_selection_state_to_be(checkbox_locator, True)
        )
        print("La suscripcion se ha activado correctamente.")
    except TimeoutException:
        assert False, "La suscripcion no se activó. El checkbox no está seleccionado."


@then('Se verifica que la suscripcion esté desactivada')
def step_impl(context):
    """
    Se valida que el checkbox esté desmarcado (desactivada).
    """
    # Se utiliza el localizador del Page Object para el checkbox
    checkbox_locator = context.suscripcion_page.subscription_checkbox
    try:
        # Se espera hasta 20 segundos para la deselección
        WebDriverWait(context.browser, 20).until(
            EC.element_located_selection_state_to_be(checkbox_locator, False)
        )
        print("La suscripcion se ha desactivado correctamente.")
    except TimeoutException:
        assert False, "La suscripcion no se desactivó. El checkbox sigue seleccionado."


@when("Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos")
def step_impl(context):
    """
    Se abre el menú hamburguesa, espera 10 segundos y se vuelve a presionar.
    """
    context.suscripcion_page.click_hamburger_menu()
    print("Esperando 10 segundos...")
    time.sleep(10)
    context.suscripcion_page.click_hamburger_menu()