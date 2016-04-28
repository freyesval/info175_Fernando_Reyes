# -*- coding: utf -8 -*-

LOGIN = False

def autenticado(f):
    def inner(*args, **kwargs):
        if LOGIN:
            f(*args,**kwargs)
        else:
            raise Exception
    return inner
    

def avisar(f):
    # Función decoradora
    def inner(*args, **kwargs):
        f(*args, **kwargs)
        print "Se ha ejecutado %s" % f.__name__
    return inner


@autenticado
@avisar
def abrir_puerta():
    print "Abrir puerta"

@autenticado
@avisar
def cerrar_puerta():
    print "Cerrar puerta"


#keywords eje
        #abrir_puerta(numero=5, letra = "c")

