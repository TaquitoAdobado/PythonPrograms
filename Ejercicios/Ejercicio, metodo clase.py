'''Crea un metodo de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador,
estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False. '''

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print("El jugador se ha revivido.", cls.vivo)

Jugador.revivir()