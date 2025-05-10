"""

¿Que es un decorador en Python y para que se utiliza comunmente?

Es una funcion que modifica o extiende el comportamiento de otras funciones sin modificar el codigo
Se usa para reutilizar codigo
separacion de preocupaciones haciendo el codigo mḿas limpio y con acoplamiento más bajo
"""

def decorator(func):
    def envoltorio(*args, **kwargs):
        print("Decorating")
        func()
        print("Stop decoration")
    return envoltorio    


@decorator
def mensaje():
    print("CQ, CQ PROBRANDO")
mensaje()


