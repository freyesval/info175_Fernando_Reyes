def mayor(x,y)
    if(x>y)
        print("El numero ", x, " es mayor")
    elif(x<y)
        print("El numero ", y, " es mayor")
    else print("Los dos numeros son iguales")

if __name__ == "__main__":
   x=input("Ingrese un numero entero: ")
   y=input("Ingrese otro numero entero: ") 
   mayor(x,y)
   
