Feature: Buscar producto
    Scenario: Credenciales incorrectas intu   
        Given el usuario se encuentra en la pagina de MercadoLibre
        When el usuario escribe el nombre de un producto
        Then muestra productos