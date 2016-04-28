# -*- coding: utf-8 -*-

# Crear una función recursiva que calcule el n-esimo elemento
# de la susecion de fibonacci

''' Fn={0       if n==0;
        1       if n==1;
        Fn-1 + Fn-2 if n>1
        }'''

def fibonacci(n):
    i=0
    
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)





