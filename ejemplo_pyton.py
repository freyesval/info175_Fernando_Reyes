def divisible(x,y):
    return True if x % y == 0 else False


if __name__ == "__main__":
    x=input("Ingrese un numero entero: ")
    y=input("Ingrese otro numero entero: ")
    print(divisible(x,y))
