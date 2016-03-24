#Escriba una funcion que se llame "encrypt" en python que reciba
#como parametro una palabra y a cada caracter( solo letras) lo 
#modifique por la letra que esta a n posiciones de distancia
#en el abecedario. Se debe poder especificar el numero n de 
#posiciones quie se desea correr cada caracter (parametro de la funcion)

#Se omite la ñ

#utilizar 
#String.ascii_lowecase

import os, sys

def encrypt(palabra, n):
    p = string.ascii_lowercase
    for i in range(1,lend(palabra)):
        for j in range(1,25):
            if(paralabra[i]==p[j]):
                if j+n>=26:
                    palabra[i]=p[j-n]
                else:
                    palabra[i]=p[j+n]
    return palabra


if __name__== "__main__":
    pal=input("Ingrese una palabra: ")
    n=input("Ingrese un numero del 1 al 26")
    while(y>26 or y<0)
	y=input("Ingrese un numero valido e.e (Entre 0 y 26): ")
    palabra_mod=encrypt(pal,n)
    print palabra_mod
