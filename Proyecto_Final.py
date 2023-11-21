import time

class Juego:
    def introduccion(self):
        print("Bienvenido")
        time.sleep(1)

        art = '''
                       .|
                       | |
                       |'|            ._____
               ___    |  |            |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  .|  |     ||   '-_  |    |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 _|  '-'     '    ""       '-'   '-.'    '`      |__
 '''
        
        print(art)

        print("Te encuentras de viaje en una ciudad grande y desconocida para ti...")
        time.sleep(5)
        
        print("Elige tu personaje:")
        time.sleep(1)

        print("1. Personaje1\n2. Personaje2\n")
        personaje = input("Selecciona 1 o 2 ").lower()
        self.switch_personaje(personaje)

    def switch_personaje(self, personaje):
        switch_dict = {
            '1': self.personaje1,
            '2': self.personaje2,
            
        }
        selected_personaje = switch_dict.get(personaje, self.personaje_default)
        selected_personaje()

    def personaje1(self):
        print("Has elegido al Personaje 1. Una mujer turista./n ")
        # Lógica del Personaje 1
        self.funcion_personaje1()

    def funcion_personaje1(self):
        # Aquí puedes agregar funciones específicas para el Personaje 1
        print("Función personalizada del Personaje 1.")

    def personaje2(self):
        print("Has elegido al Personaje 2. Un hombre turista.")
        # Lógica del Personaje 2

    def personaje_default(self):
        print("Opcion no valida. Personaje asignado por defecto.")
        self.personaje2() 
        
correr = Juego()
correr.introduccion()