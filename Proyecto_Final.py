import time
import sys

class Juego:

    def _init_(self):
        vidas = 3

    def introduccion(self):

        art = '''
                       .|
                       | |
                       |'|            .___
               _    |  |            |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  .|  |    ||   '-_  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 _|  '-'     '    ""       '-'   '-.'    '`      |__
 '''
        
        print(art)

        print("Te encuentras de viaje en una ciudad grande y desconocida para ti...")
        #time.sleep(5)
        
        print("Elige tu personaje:")
        #time.sleep(1)

        print("1. Personaje -> Mujer turista en un viaje por Paris")
        print("2. Personaje -> Hombre historiador en una aventura en Egipto")
        personaje = input("Selecciona 1 o 2 ").lower()
        self.switch_personaje(personaje)

    def switch_personaje(self, personaje):
        switch_dict = {
            '1': self.personaje1,
            '2': self.personaje2,
            
        }
        selected_personaje = switch_dict.get(personaje, self.personaje_default)
        selected_personaje()



#               PERSONAJE 1

    def personaje1(self):
        print("")
        print("Has elegido el personaje 1, una mujer turista.\n ")
        nombre = input("Ingresa nombre del personaje: ")
        print(f"Hola {nombre}! Bienvenida, aquí inicia el trayecto...")
        time.sleep(2)
        
        # Lógica del Personaje 1
        self.p_lugar()

    def p_lugar(self):
        art = '''
                |
                |
                A
              /X\
              \/X\/
               |V|
               |A|
               |V|
              /XXX\
              |\/\|
              |/\/|
              |\/\|
              |/\/|
              |\/\|
              |/\/|
             IIIIIII
             |\/_\/|
            /\// \\/\
            |/|   |\|
           /\X/_\X/\
          IIIIIIIIIIIII
         /`-\/XXXXX\/-`\
       /`.-'/\|/I\|/\'-.`\
      /`\-/.-"` `"-. \-/\
     /.-'.'           '.'-.\
    /`\-/               \-/`\
 /`-'/`               `\'-`\
`"""""""`                `""""""` 
'''
        print(art)
        print("Estás en Francia, el país de los sueños. El tour que pagaste recién comienza, y estás emocionado. El guía pregunta a qué lugar quieren ir todos, pero tu voto es el decisivo.")
        eleccion = input("¿Ir al museo de Louvre (escribe 'Louvre') o ir a la Torre Eiffel (escribe 'Torre')? ").lower()

        if eleccion == 'louvre':
            print("\nEl camión del tour se dirige hacia allá. Para, y todos bajan para empezar el recorrido")
            self.p1_lou1()
           
        elif eleccion == 'torre':
            print("\nEl camión del tour se dirige hacia allá. Para, y todos bajan para empezar el recorrido")
            self.p1_tor1()
        else:
            print("Opción no válida. Por favor, escribe 'Louvre' o 'Torre'.")
            # Puedes manejar opciones no válidas de la manera que desees

    #                                                   LOUVRE
    def p1_lou1(self):
        print("El museo está muy lleno y te da flojera esperar en la fila con el resto del grupo, así que te alejas a tomar unas fotos de la calle y prometes volver. Una local se te acerca a pedir firmas para una protesta ")    
        eleccion = input("La ignoras (escribe ignorar) / La escuchas y firma(escribe firmar)").lower()
        
        if eleccion == 'ignorar':
            print("\nContinuas tomando fotos de todo. Y de repente se ensucia el lente de tu cámara y te das cuenta que le cayó popo de paloma.")
            self.p1_lou2a()
            
        elif eleccion == 'firmar':
            print("\nLuego de toda la platica y la firma. Intentas volver con el tour pero ya no estan. Desaparecieron.")   
            print("No dejas que el miedo te gane asi que te propones caminar hasta encontrarlos.")  
            self.camino_hasta_encontrar()
        else:
            print("Opción no válida.")
            
    def p1_lou2a(self):
        eleccion = input(" La intentas limpiar(escribe limpiar)/ No le das importancia y regresas con los del tour(escribe regresar)").lower()
        if eleccion == 'limpiar':
            print("\nBuscas y encuentras una banca donde sentarte para  tallar el lente con una toallita húmeda. Una señora sentada ahi muy amable te ofrece darte el tour ella misma por la ciudad.")
            self.limpiar()
            
        elif eleccion == 'regresar':
            print("\nRegresas justo a tiempo para entrar al museo con el resto del grupo. Entran todos juntos y empiezan  a ver las obras atentamente. Luego de varias horas en el museo, escuchas a otros turistas hablar sobre una obra ultra secreta, a la que se ingresa por una puerta detrás de un cuadro del museo. ")
            self.regresar()
        else:
            print("Opción no válida.")
            
    def limpiar(self):
        eleccion= input("Aceptas el tour de la señora(Aceptar)/Rechazas la oferta y regresas con los del tour(Rechazar)").lower()
        if eleccion == 'aceptar':
            print("\nEmpiezan a recorrer varios lugares hasta que anochece,  y de repente te das cuenta que no sabes donde estas, y la senora tampoco porque tiene alzheimer y ya no recuerda ni siquiera que haces con ella .")
            print("La señora se nego a seguir avanzando y pidio que te fueras, que ella llamaria alguien para que la recogiera pero que tu volvieras por donde veniste porque no te conocia")
            print("Te entra panico por estar sola, pero a aun asi decides intentar encontrar a los del tour. Te diriges hacia un callejon que parece un atajo de regreso al Louvre porque parece seguro.")
            print("Cometiste un error...")
            time.sleep(2)
            self.parada()
                       
        elif eleccion == 'rechazar':
            print("\nRegresas justo a tiempo para entrar al museo con el resto del grupo. Entran todos juntos y empiezan  a ver las obras atentamente. Luego de varias horas en el museo, escuchas a unos trabajadores del museo susurrar acerca de una obra ultra secreta, a la que se ingresa por una puerta detrás de un cuadro del museo. ")
            self.entrar()
        else:
            print("Opción no válida.")
            
    def regresar(self):
        eleccion=input("\nDecides buscar la puerta(buscar)/ Admirar obras no secretas(admirar)").lower()
        if eleccion == 'buscar':
            self.entrar()
            
        elif eleccion == 'admirar':
            print("\nRegresas justo a tiempo para entrar al museo con el resto del grupo. Entran todos juntos y empiezan  a ver las obras atentamente. Luego de varias horas en el museo, escuchas a otros turistas hablar sobre una obra ultra secreta, a la que se ingresa por una puerta detrás de un cuadro del museo. ")
            self.entrar()
        else:
            print("Opción no válida.")
            
    def entrar(self):
        print ("\nEscuchaste el nombre del cuadro asi que te diriges hacia ahi. Revisas que no venga nadie y lo quitas para descubrir la puerta.")
        time.sleep(2)
        print("Entras y te das cuenta que no va a ser tan fácil, hay otra puerta que se desbloquea solamente si se encuentran los 4 numeros de una contrasenia. ¿Que decides?")
        eleccion=input("\nTe arrepientes e intentas regresar(arrepentir)  o  Lo intentas resolver(resolver)").lower()
        if eleccion == 'arrepentir':
            print("\nTe das cuenta que la puerta por la que entraste se bloqueó y no hay salida. Te da un ataque de pánico y claustrofobia. Tu corazón se altera por el pánico.")
            time.sleep(2)
            print("Mueres por un ataque al corazón. La curiosidad te costo la vida, y tu cuerpo no será encontrado hasta una semana después.")
            self.fin_del_juego()
            
        elif eleccion == 'resolver':
            print("\nHay una serie de acertijos para encontrar los digitos de la contrasenia. Las instrucciones solicitan resolver las preguntas para descubir los numeros")
            self.resolver()
        else:
            print("Opción no válida.")
            
    def resolver(self):
        art = '''
            ooo,    .---.
 o`  o   /    |\______
o`   'oooo()  | ____   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|
  '''
        print(art)
        print("La instruccion dice: Debes resolver correctamente cada pregunta para continuar a la siguiente.")
        print("Asi que inicias el juego y las pistas para encontrar los números son:")
        preguntas_respuestas = [
                ("\nRedondo soy y es cosa anunciada que a la derecha algo valgo, pero a la izquierda nada.\nRespuesta: ", '0'),
                ("Puesto que de una manera soy un número par, pasó a ser otro si la vuelta me das.\nRespuesta: ", '9'),
                ("El número de cuántos ladrillos se necesitan para completar un edificio de ladrillo.\nRespuesta: ", '1'),
                ("Soy un número par y primo a la vez, solo me dividen uno y yo y a este le sumas 5.\nRespuesta: ", '7')
            ]

        respuestas_correctas = 0

        for pregunta, respuesta_correcta in preguntas_respuestas:
            while True:
                respuesta_usuario = input(pregunta)
                if respuesta_usuario == respuesta_correcta:
                        
                    respuestas_correctas += 1
                    break
                else:
                    print("Incorrecto. Inténtalo de nuevo.")
        self.respuestas_correctas()

    def respuestas_correctas(self):
        print("---------------La puerta ha sido abierta------------------")
        art='''
                    ______
            |\ _____ /|
            | |  _ _ _ _  | |
            | | | | | | | | |
            | | |-+-+-+-| | |
            | | |-+-+-+-| | |
            | | ||||| | |
            | |     _   | |
            | |    /__/   | |
            | |   [%==] ()| |
            | |         ||| |
            | |         ()| |
            | |           | |
            | |           | |
            | |           | |
            ||___|| '''
        print(art)
        print("\nAl entrar a la habitacion secreta te das cuenta que hay muchos bocetos y pinturas de artistas famosos. Hay algunos preciosos que quisieras llevar contigo. Parece tan sencillo tomarlos, no parece haber nada de proteccion antirobo.")
        eleccion=input("\nTe llevas unas cuantas (Escribe llevar) o Tomas fotos y regresas a la salida antes de que alguien te descubra(Escribe salida)  ").lower()
        
        if eleccion == 'llevar':
            print("\nAl intentar tomar una obra de la pared, suena una alarma, y el piso sobre el que te parabas se abre, por lo que caes y resulta ser una jaula.")
            print("\nLuego de unos minutos ahi la policia llega y te arresta por ladrona. No saldras de la carcel en muuucho tiempo.")
            self.fin_del_juego()
            
        elif eleccion == 'salida':
            print("\nEres honesto. Al regresar por donde entraste te das cuenta que ambas puertas que atravesaste estan abiertas asi que sales de ese cuarto secreto como si nada hubiera pasado.")
            print("\nAcomodas el cuadro que cubre el acceso al cuarto secreto para que nadie note lo que hiciste y regresas a buscar al tour.")
            print("Los encuentras esperandote fuera del museo para dirigirse a su nueva parada. No puedes controlar la emocion que tienes por descubrir mas luagres secretos en cada sitio que visiten.")
            eleccion=input("¿Te animas a una nueva avetura? )si/no").lower()
            if eleccion == 'no':
                self.fin_del_juego()
            if eleccion == 'si':
                self.introduccion()
            
        else:
            print("Opción no válida.")

    #                                     TORRE
    def p1_tor1(self) :
        print("\nSubes a la torre y te quedas maravillada con lo que estás viendo, la vista da a toda la ciudad y contemplas la ciudad entera ante tus ojos.")
        time.sleep(2)
        print("\nEstando ahí observas que se acerca un hombre apuesto hacia ti, al llegar te empieza a hacer preguntas sobre ti y te pide tu número...")
        self.se_lo_das()
                  
    def se_lo_das(self):
        print("\nEl hombre se va y estás entusiasmada por que te llame, sin embargo, volteas hacia abajo y ves al tour en el que te encuentras yéndose hacia el camión. Debes decidir que hacer...")
        eleccion=input("\nIntentas correr y alcanzar al tour (Escribe correr) / Localicas al hombre y pides su ayuda (Escribe localizar) ").lower()
        if eleccion == 'localizar':
            self.localizar()
        elif eleccion == 'correr':
            self.correr()
            
    def correr(self):
        print("\nCorres lo más rápido que puedes bajando las escaleras, pero llegas abajo y el camión ya había salido y tienes que hacer algo.")
        eleccion=input("Caminas hasta encontrar el hotel (Escribe hotel) / Vas a donde recuerdas que era la siguiente parada (Escribe parada) ").lower()
        if eleccion == 'hotel':
            self.camino_hasta_encontrar()
        elif eleccion == 'parada':
            self.parada()
            
    def localizar(self):
        print("“Recurres al hombre apuesto y le comentas lo que pasó, el hombre lo entiende y te ofrece ser tu compañía por el resto del viaje...")
        print("Permaneces con él y te propone ir a otro lugar, al bajar te das cuenta que su vehículo es una moto, tú nunca has subido a una moto y te entran los nervios...")
        eleccion=input("Te arriesgas y subes a la moto (moto)/ Propones tomar el metro (metro) ")
        if eleccion == 'moto':
            self.moto()
        elif eleccion == 'metro':
            self.metro()

    def moto(self):
        print("A pesar de los nervios subes a la moto y él decide decide ser tu guía a lo largo del viaje.")
        eleccion = input("¿Qué quieres que te enseñe primero?” (restaurante, Notre Dame, rio sena) ")
        if eleccion == 'restaurante':
            self.restaurante()
        if eleccion == 'notre dame':
            self.notre_dame()
        if eleccion == "rio sena":
            self.rio_sena()

    def notre_dame(self):
        print("Llegan a Notre Dame, toman unas cuantas fotos y dan una que otra vuelta con su moto por el lugar, pasan a comprar un helado y se dan cuenta que ya se está haciendo un poco tarde, por lo que sabiendo que no cuentas con un lugar para dormir te ofrece ir a su casa, sin embargo, de igual manera pasaste por un hostel que se veía agradable donde podrías pasar la noche")
        eleccion = input("Voy a su casa (Escribe casa) / Voy al hostal (Escribe hostal) ")
        if eleccion == "casa":
            self.conocer_casa()
        if eleccion == "hostal":
            self.descansar()

    def rio_sena(self):
        print("Llegan al río Sena y deciden dar un un caminata por el río para apreciar el lugar, se va la noción del tiempo y se dan cuenta que ya se está haciendo un poco tarde, por lo que sabiendo que no cuentas con un lugar para dormir te ofrece ir a su casa, sin embargo, de igual manera pasaste por un hostel que se veía agradable donde podrías pasar la noche")
        eleccion = input("Voy a su casa (Escribe casa) / Voy al hostal (Escribe hostal) ")
        if eleccion == "casa":
            self.conocer_casa()
        if eleccion == "hostal":
            self.descansar()


    def restaurante(self):
        print("Te lleva a un restaurante bellísimo con vista a toda la ciudad, comparten una buena conversación, pero se dan cuenta que ya está oscureciendo por lo que te ofrece ir a su casa a conocerla y pasar la noche, sin embargo, también viste un pequeño y agradable hostal en el camino")
        eleccion = input("Voy a su casa (Escribe casa) / Voy al hostal (Escribe hostal) ")
        if eleccion == "casa":
            self.conocer_casa()
        if eleccion == "hostal":
            self.descansar()

    def metro(self):
        print("“Prefieres tomar el metro y él está de acuerdo, por lo que decide ser tu guía el resto del viaje e indicarte dónde se encuentra cada sitio, a dónde quieres ir primero? Te pregunta")
        eleccion = input("A un restaurante (Escribe restaurante) / A Notre Dame (Escribe notre dame) / Al Río Sena (Escribe rio) ")
        if eleccion == 'restaurante':
            self.restaurante()
        if eleccion == 'notre dame':
            self.notre_dame()
        if eleccion == 'rio':
            self.rio_sena()

    
    def parada(self):
        print("Estás tratando de recordar dónde era el siguiente lugar, pero no pareces recordar, por lo que sigues caminando sin rumbo, sin darte cuenta te encuentras en un callejón un tanto sospechoso y decides salir de ahí lo más rápido posible, sin embargo, antes de salir llega un asaltante y te pide que le des tus pertenencias")
        eleccion=input("Se las das (Escribe dar) / Te rehusas (Escribe rehusar) ").lower()
        if eleccion == 'dar':
            self.dar()
        elif eleccion == 'rehusar':
            print("Te rehusas a darle tus cosas, pero no te diste cuenta que el asaltante tenía un arma , por lo que para conseguir su objetivo te dispara")
            print("Lo siento, mueres en un asalto")
            self.fin_del_juego()
            
    def camino_hasta_encontrar(self):
        print("“Llevas caminando un buen rato y te das cuenta que te encuentras perdida, justo en ese momento empieza a llover y no sabes qué hacer, la mayoría de los lugares se encuentran cerrados por la hora, sin embargo, ves a lo lejos dos lugares con las luces aún encendidas, te das cuenta que uno es un bar y el otro es un pequeño hostal donde podrías pasar la noche, qué haces?")
        eleccion=input("Vas al bar a tomar algo (Escribe bar)/ Vas al hostal a descansar (Escribe descansar) ")
        if eleccion == 'bar':
            self.bar()
        elif eleccion == 'descansar':
            self.descansar()
            
    def bar(self):
        print ("Entras al bar, te sientas en la barra y pides..." )
        bebida = input("Qué bebida deseas tomar? ")      
        print(f"...te encuentras tomando tu {bebida}, volteas y ves a aquel hombre apuesto que te habías encontrado antes al final de la barra, él te ve y se acerca a saludar, platican y pasan el rato y al término de la noche te invita a conocer su casa...")
        eleccion=input("Vas a concer su casa (Escribe casa) / Vas al hostal a descansa (Escribe descansar) ").lower()
        if eleccion == 'casa':
            self.conocer_casa()
        elif eleccion == 'descansar':
            self.descansar()
            
    def conocer_casa(self):
        print("\nDecides conocer su casa, pero en el camino te sorprende ver que su casa no era algo común, es una mansión inmensa con rejas enormes y guardias en cada puerta, vas entrando a la casa y te das cuenta de todo lo que tiene dentro, y de lo hermosa que es, sin embargo sientes un poco de escalofríos debido al frío que emite.")
        eleccion=input("Mejor regresas al hostal a descansar(Escribe descansar)/Te quedas(Escribe quedar) ").lower()
        if eleccion == 'quedar':
            self.me_quedo()
        elif eleccion == 'descansar':
            self.descansar()

    def me_quedo(self):
        print("Entras a la enorme mansión, inmediatamente el hombre te dirige hacia la habitación donde te hospedarás, en cuanto entras te cierra la puerta y le pone llave...")
        time.sleep(1)
        print("Te asustas y decides buscar la manera de huir inmediatamente...")
        time.sleep(1)
        print("Observas tres alternativas diferentes, una es por la ventana, otra por el conducto del aire y por último por un acceso que está asegurado con código.")
        eleccion = input("¿Cuál escoges? (ventana, conducto, codigo) ")
        if eleccion == 'ventana':
            self.ventana()
        if eleccion == 'conducto':
            self.conducto()
        else:
            self.codigo()

    def ventana(self):
        print("Intentas escapar por la ventana, el problema es que te encuentras en el segundo piso y es grande la distancia hasta el piso...")
        time.sleep(2)
        print("Buscas materiales a tu alrededor para escapar...")
        material = input("¿Qué podrías utilizar para escapar? ")
        print(f"{material} bien pensado! Utilizas la herramienta de escape y logras llegar al suelo sana y salva...")
        print("Corres lo más rápido que puedes y te vas directo al aeropuerto para regresar a casa")
        self.fin_del_juego()

    def conducto(self):
        print("Decides escapar por el conducto de aire...")
        time.sleep(2)
        print("Para abrirlo ocupas un tipo de herramienta punteaguda. ")
        herramienta = input("¿Qué se te ocurre que podrías utilizar? ")
        print(f"{herramienta}, bien pensado! Logras abrir el coducto y subes...")
        time.sleep(2)
        print("No estás segura por dónde es el camino ni adonde vas a salir...")
        time.sleep(1)
        print("El conducto se divide en dos...")
        camino = input("¿Por dónde te vas? Izquierda / Derecha ")
        print(f"Tomas el camino de la {camino}, llegas a una habitación extraña, no sabes dónde estás.")
        decision = input("¿Qué haces? ")
        print("Buena idea! Llevas a cabo lo que pensaste y logras salir de ahí, corres directo al aeropuerto y regresas a casa.")
        self.fin_del_juego()

    def resolver2(self):
        art='''
                    ______
            |\ _____ /|
            | |  _ _ _ _  | |
            | | | | | | | | |
            | | |-+-+-+-| | |
            | | |-+-+-+-| | |
            | | ||||| | |
            | |     _   | |
            | |    /__/   | |
            | |   [%==] ()| |
            | |         ||| |
            | |         ()| |
            | |           | |
            | |           | |
            | |           | |
            ||___|| '''
        print(art)
        print("La instruccion dice: Debes resolver correctamente cada pregunta para continuar a la siguiente.")
        print("Asi que inicias el juego y las pistas para encontrar los números son:")
        preguntas_respuestas = [
            ("\nRedondo soy y es cosa anunciada que a la derecha algo valgo, pero a la izquierda nada.\nRespuesta: ", '0'),
            ("Puesto que de una manera soy un número par, pasó a ser otro si la vuelta me das.\nRespuesta: ", '9'),
            ("El número de cuántos ladrillos se necesitan para completar un edificio de ladrillo.\nRespuesta: ", '1'),
            ("Soy un número par y primo a la vez, solo me dividen uno y yo y a este le sumas 5.\nRespuesta: ", '7')
        ]

        for pregunta, respuesta_correcta in preguntas_respuestas:
            while True:
                respuesta_usuario = input(pregunta)
                if respuesta_usuario == respuesta_correcta:
                    break
                else:
                    print("Incorrecto. Inténtalo de nuevo.")

    def codigo(self):
        print("Te vas por el acceso que está asegurado por código, por lo que tienes que encontrar un código de 4 dígitos para poderla abrir y huir...")
        self.resolver2()

        print("Logras abrirlo y sigilosamente escapas de ahí, vas directo al aeropuerto regresas a casa!")
        self.fin_del_juego()
    
    def descansar(self):
        while True:
            print("\nLlegas al hostal y preguntas si tienen disponibilidad, te comentan que si cuentan con cuartos disponibles, sin embargo, para obtener una llave, has de responder a una adivinanza, la cual te dirá el número de habitación al que has de llegar.")
            adivinanza = input("~Este era un número impar, pero un día la vuelta se dio bocabajo se quedó y en un número par se convirtió.\nRespuesta: ").lower()

            if adivinanza == '9':
                print("¡Correcto! La habitación es la número 9. Aqui tienes la llave...")
                print("Llegas a tu habitación, te instalas y cuando estás a punto de dormir escuchas una alarma sonando dentro del lugar, sales de ahí por si se tratara de una emergencia, al salir de tu habitación te das cuenta que el lugar se está incendiando pero tú te encuentras en el segundo piso del lugar.")
                self.salir_incendio()  
                break 
            else:
                print("Incorrecto. Intenta de nuevo.")
    
    def salir_incendio(self):
        print("Nada más alcanzas a agarrar una cosa...")
        objeto = input("¿Qué agarras? ")
        print(f"Agarras tu {objeto} y ves la manera de salir lo más rápido posible...")
        print("Debes bajar, pero hay dos opciones: " )
        eleccion=input("Bajas por las escaleras (escaleras)/ Vas por el elevador (elevador) ")
        if eleccion == 'escaleras':
            self.escaleras()
        elif eleccion == 'elevador':
            print("Corres al elevador antes de que las llamas del fuego te alcancen, al llegar intentas bajar pero poco antes de que se cerraran las puertas las llamas se esparcen más rápido de lo que pensaste y alcanzan a entrar.")
            time.sleep(2)
            print("Sigue las señales y no uses el elevador en caso de emergencia")
            self.fin_del_juego()
    
    def escaleras(self):
        print("Bajas por las escaleras, alcanzas a desviar las llamas del fuego, y sales...")
        time.sleep(1)
        decision = input("¿Qué es lo primero que debes hacer en este tipo de situación? ")
        if "911" in decision:
            "Correcto, te aseguras de pedir ayuda"
        if "ayudar" in decision:
            "Parcialmente correcto, primero llamas al 911 por ayuda profesional y luego ayudas al resto de la gente"
        else:
            "Lo correcto sería llamar al 911 para pedir ayuda profesional"
        time.sleep(2)
        print("En vista de la mala suerte que has tenido, decides ir al aeropuerto y regresar a casa.")
          
    def dar(self):
        print("\nLe das tus pertenencias y se va, sigues tu rumbo pero no tienes ni dinero ni teléfono para comunicarte por lo que te diriges a la estación policial para reportar tu caso.")
        time.sleep(1)
        print("Llegando a la estación te mandan con el encargado de asaltos, llegando a la oficina te das cuenta que el oficial encargado era el hombre apuesto que conociste antes...")
        time.sleep(1)
        print("Le comentas lo que pasó y decide ayudarte...")
        time.sleep(1)
        print("Se hace tarde y viendo que no tienes lugar donde pasar la noche te ofrece quedarte en su casa o te recomienda un agradable hostal donde pasar la noche...")
        eleccion = input("Voy a su casa (Escribe casa) / Voy al hostal (Escribe hostal) ")
        if eleccion == "casa":
            self.conocer_casa()
        if eleccion == "hostal":
            self.descansar()
        
    def fin_del_juego(self):
        print("FIN DEL JUEGO")
        art='''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣶⣶⣶⣶⣾⣿⣿⣶⣶⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⡿⠿⠛⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠻⢿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⢀⣠⣤⣶⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠶⠛⠛⠋⠉⠉⠛⠛⠳⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⣨⣿⣿⣿⡿⠿⠛⠛⢿⣿⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣄⣠⣤⣶⣶⡿⠿⠟⠛⠉⠁⢀⣀⠀⠀⠘⣿⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣾⣿⠿⠟⠋⠉⠀⢀⣀⣴⡴⣾⣿⣿⣿⣷⡄⠀⢹⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣾⣿⠿⠛⠋⠉⠀⠀⠀⢠⣶⣾⣿⣿⠿⠟⠃⢹⣿⡄⠈⣿⣧⠀⠀⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⢀⣀⣤⣤⣶⣾⡿⠿⠛⠛⠉⠁⢀⣤⣤⣄⠸⣿⣆⠀⠸⣿⡇⢿⣧⠀⢀⣠⠈⣿⣷⣶⣿⡏⠀⠀⠸⣿⣇⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀⣸⣏⣠⣤⣶⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⣾⣿⠻⣿⣧⠹⣿⣆⠀⣿⡇⠸⣿⣿⣿⠿⠇⠸⣿⡏⢻⣿⣆⠀⠀⢿⣿⡀⠀
⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⣀⣠⣴⣶⣿⣿⠿⠟⠋⠉⠀⢀⣠⣤⣶⣾⣧⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⣿⣧⠘⣿⣆⣿⣿⠀⢻⣿⡄⠀⠀⣀⢻⣿⡀⠙⣿⣷⠄⠘⣿⣧⠀
⠀⠀⠀⢀⣀⣾⣿⣷⣾⡿⠿⠛⠋⠉⠀⠀⣤⣤⠀⢸⣿⡌⣿⣿⠋⠉⠁⠀⠀⠀⠀⠀⠀⠸⣿⣇⠀⢸⣿⡇⠘⣿⣾⣿⠀⠈⣿⣷⣾⣿⡿⠮⠛⠃⠀⢀⣀⣠⣤⣾⣿⠄
⣴⣶⣾⡿⠿⠛⠛⠉⠁⠀⠀⠀⣶⣿⣆⠀⢹⣿⣧⣸⣿⣧⠸⣿⣦⣤⣶⣆⠀⠀⠀⠀⠀⠀⢻⣿⣄⢀⣿⡇⠀⠘⣿⣿⡆⠀⠘⠛⠉⠁⣀⣠⣤⣶⣾⣿⠿⠟⠛⠉⠁⠀
⢹⣿⣇⠀⠀⠀⣴⣿⣿⣷⡄⠀⢹⡿⣿⣆⠈⣿⣿⣿⣿⢿⣆⢻⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠃⠀⠀⠀⠀⣀⣠⣴⣶⣿⣿⠿⠟⠋⢩⣿⣿⠀⠀⠀⠀⠀⠀
⠀⢿⣿⡀⠀⠀⣿⣟⠈⠛⠋⠀⢸⣿⠈⣿⣆⠸⣿⣻⣿⡾⣿⡌⣿⣇⣀⣤⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣾⣿⠿⣿⠛⠉⠁⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣧⠀⠀⢻⣿⠀⣶⣾⣧⠘⣿⣷⣾⣿⣆⢿⣧⠉⠁⢻⣧⢹⣿⡿⠿⠛⠃⠀⢀⣀⣤⣴⣶⡾⡿⠟⠋⠛⠉⠁⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⢹⣿⡄⠀⠈⣿⣧⠙⠙⣿⡆⣿⣟⠉⠘⣿⣾⣿⡆⠀⠀⠛⠁⢀⣀⣠⣤⣶⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣷⠀⠀⠘⣿⣷⣴⣿⡏⣿⡿⠀⠀⠈⠉⢀⣀⣠⣴⣶⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⡆⠀⠀⠈⠛⠛⠋⠀⢀⣀⣤⣴⣶⣿⡿⠿⣿⣋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⡄⢀⣀⣤⣴⣶⣿⠿⠿⠛⠋⠉⠀⠀⠀⠈⠙⠳⢦⣤⣀⣀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⣿⡿⠿⠛⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣷⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
        print(art)
        opcion=input("Presiona 's' para salir/ Presiona 'j' para jugar de nuevo")
        if opcion == 's':
            sys.exit()
        else:
            self.introduccion()




    #                             PERSONAJE 2

    def personaje2(self):
        print("")
        print("Has elegido el personaje 2, un hombre historiador.\n ")
        nombre = input("Ingresa nombre del personaje: ")
        print(f"Hola {nombre}! Bienvenido, aquí inicia el trayecto...")
        time.sleep(2)

        self.p2_lugar()

    def p2_lugar(self):
        piramide ='''              
              /=\\
             /===\ \
            /=====\' \
           /=======\'' \
          /=========\ ' '\
         /===========\''   \
        /=============\ ' '  \
       /===============\   ''  \
      /=================\' ' ' ' \
     /===================\' ' '  ' \
    /=====================\' '   ' ' \
   /=======================\  '   ' /
  /=========================\   ' /
 /===========================\'  /
/=============================\/

'''

        print(piramide)
        print("Te encuntras en egipto en busca de una reliquia muy valiosa, según tus datos, este objeto se encuentra dentro de una pirámide y es tu trabajo es encontrarlo.")
        listo = input("¿Estás listo para iniciar la aventura? si/no ")
        if listo == 'si':
            print("Eso es todo! Comenzemos...")
        if listo == 'no':
            print("No estés nervioso, lo lograrás!")

        print("Antes de empezar debemos asegurarnos que tengamos todo lo que necesitamos...")
        lista_verificacion = ["Linterna", "Agua", "Mapa", "Mochila", "Soga"]
        i = 0
        while i < len(lista_verificacion):
            tarea = lista_verificacion[i]
            print("¿Tienes tu '{}'? (si/no)".format(tarea))
            respuesta = input()
            respuesta = respuesta.lower()

            if respuesta == "si":
                lista_verificacion[i] = True
            else:
                lista_verificacion[i] = False

            i += 1

        print("Lista de verificación completada:")
        for tarea in lista_verificacion:
            if tarea is True:
                print("* Listo".format(tarea))
            else:
                print("* Algo nos falta".format(tarea))

        print("")        
        print("Entras a la pirámide...")
        camino = input("¿Qué camino tomas? izquierda / derecha ")
        if camino == 'izquierda':
            self.izq()
        if camino == 'derecha':
            self.der()
            
    #                                                    IZQUIERDA
    def izq(self):
        pass
    #                                                    DERECHA
    def der(self):
        pass
        
        print("Has elegido al Personaje 2. Un hombre turista.")
        self.p_lugar()
        
    def personaje_default(self):
        print("Opcion no valida. Personaje asignado por defecto.")
        self.personaje1()
            
correr = Juego()
correr.introduccion()
correr.introduccion()