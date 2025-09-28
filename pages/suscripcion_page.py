#
# # suscripcion_page.py
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
#
# class SuscripcionPage:
#     def __init__(self, browser):
#         self.browser = browser
#         # Localizadores de la página de perfil y suscripción
#         self.hamburger_menu = (By.CSS_SELECTOR, 'div.menu-wrap input.toggler')
#         self.profile_link = (By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]")
#         self.subscription_checkbox = (By.ID, "FProCheck")
#
#         self.edit_button = (By.ID, "boton-editar")
#
#         #self.accept_button = (By.ID, "BtnAcepta")
#         # Alternativa robusta (Selector CSS por valor del input)
#         self.accept_button = (By.CSS_SELECTOR, 'input[value="Aceptar"]')
#
#
#     def click_hamburger_menu(self):
#         """
#         Se hace clic en el ícono del menú hamburguesa utilizando JavaScript
#         para evitar problemas de elementos cubiertos o de visibilidad.
#         """
#         element = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located(self.hamburger_menu)
#         )
#         self.browser.execute_script("arguments[0].click();", element)
#
#     def click_profile_link(self):
#         """
#         Se hace clic en el enlace "PERFIL" utilizando JavaScript para evitar
#         problemas de elementos interceptados o de sincronización.
#         """
#         element = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located(self.profile_link)
#         )
#         self.browser.execute_script("arguments[0].click();", element)
#
#
#     def click_subscription_checkbox(self):
#         """
#         Se hace clic en el checkbox de suscripción.
#         """
#         element = WebDriverWait(self.browser, 10).until(
#             EC.element_to_be_clickable(self.subscription_checkbox)
#         )
#         element.click()
#
#
#     def click_edit_button(self):
#         """
#         Hace clic en el botón de edición.
#         """
#         try:
#             edit_btn = WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(self.edit_button)
#             )
#             edit_btn.click()
#         except TimeoutException:
#             raise TimeoutException("El botón 'Editar' no se encontró a tiempo.")
#
#     def click_accept_button(self):
#         """
#         Hace clic en el botón de aceptar.
#         """
#         try:
#             accept_btn = WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(self.accept_button)
#             )
#             accept_btn.click()
#         except TimeoutException:
#             raise TimeoutException("El botón 'Aceptar' no se encontró a tiempo.")
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SuscripcionPage:
    def __init__(self, browser):
        self.browser = browser
        # Localizadores de la página de perfil y suscripción
        self.hamburger_menu = (By.CSS_SELECTOR, 'div.menu-wrap input.toggler')
        self.profile_link = (By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]")
        self.subscription_checkbox = (By.ID, "FProCheck")

        self.edit_button = (By.ID, "boton-editar")

        # Localizador del botón Aceptar principal
        self.accept_button = (By.CSS_SELECTOR, 'input[value="Aceptar"]')

        # LOCALIZADORES ACTUALIZADOS PARA EL MODAL DE CONFIRMACIÓN (SweetAlert2 o similar):
        # Se actualiza el localizador del botón del modal a la clase más específica
        self.modal_accept_button = (By.CSS_SELECTOR, 'button.swal2-confirm')
        # Localizador del mensaje del modal para verificar su aparición
        #self.modal_message = (By.XPATH, "//div[contains(text(), 'Confirmado!')]")
        self.modal_message = (By.CLASS_NAME, "swal2-popup")

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
        Se hace clic en el checkbox de suscripción (slider/toggle).
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.subscription_checkbox)
        )
        element.click()

    def click_edit_button(self):
        """
        Hace clic en el botón de edición.
        """
        try:
            edit_btn = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.edit_button)
            )
            edit_btn.click()
        except TimeoutException:
            raise TimeoutException("El botón 'Editar' no se encontró a tiempo.")

    def click_accept_button(self):
        """
        Hace clic en el botón de aceptar principal y luego maneja el modal de confirmación
        que aparece después.
        """
        try:
            # 1. Clic en el botón Aceptar principal (Guarda los cambios)
            accept_btn = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.accept_button)
            )
            accept_btn.click()

            # 2. Esperar la aparición del modal de confirmación
            try:
                # Se espera a que el mensaje de "Confirmado!" sea visible
                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located(self.modal_message)
                )
            except TimeoutException:
                # Si el modal no aparece, se lanza una excepción específica
                raise TimeoutException("El modal 'Confirmado!' no apareció a tiempo tras el primer clic en Aceptar.")

            # 3. Clic en el botón Aceptar dentro del modal para cerrarlo
            # Se usa el nuevo selector específico para SweetAlert2
            modal_btn = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.modal_accept_button)
            )
            modal_btn.click()

        except TimeoutException as e:
            # Se relanza el error para indicar la causa del fallo
            raise TimeoutException(f"Fallo durante la interacción con el botón Aceptar o el modal: {e}")