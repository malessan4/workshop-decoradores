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

import time
def tiempo_calculado(func):
    def envoltorio(*args, **kwargs):
        inicio = time.time()
        func(*args, **kwargs)
        final = time.time()
        print(f'Tiempo transcurrido: {final-inicio}')
    return envoltorio
    
@tiempo_calculado
@decorator
def mensaje():
    print("CQ, CQ PROBRANDO")
mensaje()


def authorize(func):
    def envoltorio(user, *args, **kwargs):
        if user.is_admin:
            return func(user, *args, **kwargs)
        else:
            print(f'{user.name} no tiene permisos')
    return envoltorio

class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin
    
    
    @authorize 
    @tiempo_calculado   
    def escribirMensaje(self):
        mensaje = input(f'{self.name}: que mensaje quiere enviar: ')
        print(f'{self.name} envio un mensaje ')

persona1 = User("Nacho",True)       
persona1.escribirMensaje()

persona2 = User("Marcos", False)
persona2.escribirMensaje()

