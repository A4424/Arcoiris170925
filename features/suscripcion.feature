Feature: Gestion del perfil y suscripcion en el sitio PuntosPremiumPlus
  Como usuario del sitio
  Se desea gestionar el perfil de usuario
  Para poder ver informacion y administrar promociones

  @login @perfil
  Scenario: Acceso al perfil de usuario
    Given Se tiene una sesion iniciada
    When Se hace clic en el menu hamburguesa
    And Se hace clic en el enlace "PERFIL"
    Then Se muestra el contenido del perfil de usuario

  @login @suscripcion
  Scenario: Activar la suscripcion a promociones en el perfil
    Given Se tiene una sesion iniciada
    When Se hace clic en el menu hamburguesa
    And Se hace clic en el enlace "PERFIL"
    Then Se muestra el contenido del perfil de usuario
    When Se activa la suscripcion para recibir promociones
    Then Se verifica que la suscripcion esté activada

  @login @suscripcion @desactivar
  Scenario: Desactivar la suscripcion a promociones en el perfil
    Given Se tiene una sesion iniciada
    When Se hace clic en el menu hamburguesa
    And Se hace clic en el enlace "PERFIL"
    Then Se muestra el contenido del perfil de usuario
    When Se desactiva la suscripcion para recibir promociones
    Then Se verifica que la suscripcion esté desactivada

  @hamburguesa
  Scenario: Comprobar el comportamiento de mostrar y ocultar el menu hamburguesa
    Given Se tiene una sesion iniciada
    When Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos
    Then Se permanece en la pagina de inicio