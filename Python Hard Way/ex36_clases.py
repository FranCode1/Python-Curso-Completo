from sys import exit  # Permite cerrar el programa de forma inmediata
from random import randint  # Permite generar números aleatorios
from textwrap import dedent  # Elimina espacios innecesarios en los textos multilínea


class Scene(object):

    def enter(self):
        # Método que deben sobreescribir todas las subclases.
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)  # Termina el programa si se llama esta escena directamente


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map  # El mapa contiene las escenas

    def play(self):
        current_scene = self.scene_map.opening_scene()  # Escena inicial
        last_scene = self.scene_map.next_scene('finished')  # Escena final

        # Bucle principal: ir de escena en escena
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()  # Ejecuta la escena actual
            current_scene = self.scene_map.next_scene(next_scene_name)  # Pasa a la siguiente

        # Ejecutar la última escena (ganar el juego)
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        # Muestra una frase aleatoria de muerte y termina el juego
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            (Descripción de la situación con el enemigo)
        """))
        
        action = input("> ")  # Jugador elige una acción

        if action == "shoot!":
            # El disparo falla, el enemigo te mata
            print(dedent("..."))
            return 'death'

        elif action == "dodge!":
            # Intentas esquivar, pero fallas y mueres
            print(dedent("..."))
            return 'death'

        elif action == 'tell a joke':
            # Cuentas un chiste, el enemigo se distrae, lo matas
            print(dedent("..."))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'  # Repite escena


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            (Tienes que adivinar un código de 3 dígitos en 10 intentos)
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"  # Código aleatorio
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")  # Fallo
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            # Aciertas, tomas la bomba y sigues
            print(dedent("..."))
            return 'the_bridge'
        else:
            # Fallas 10 veces, la bomba queda bloqueada, mueres
            print(dedent("..."))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            (Estás en el puente con enemigos y una bomba)
        """))
        
        action = input("> ")

        if action == "throw the bomb":
            # Lanzas la bomba y mueres
            print(dedent("..."))
            return 'death'

        elif action == "slowly place the bomb":
            # Colocas la bomba con cuidado, escapas
            print(dedent("..."))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            (Debes elegir una cápsula correcta entre 5)
        """))
        
        good_pod = randint(1,5)  # Cápsula ganadora
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            # Cápsula dañada, mueres
            print(dedent(f"""
                You jump into pod {guess}...
                """))
            return 'death'
        else:
            # Cápsula buena, ganas el juego
            print(dedent(f"""
                You jump into pod {guess}...
                """))
            return 'finished'

        
class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('central_corridor')  # Comienza en el pasillo central
a_game = Engine(a_map)
a_game.play()  # Ejecuta el juego
