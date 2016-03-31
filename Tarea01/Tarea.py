from Tkinter import*
import string

#Encriptacion Cesar 
def encrypt(palabra,salto): #palabra a encriptar mas su salto
    jump = int(salto)
    abc = string.ascii_lowercase #abcdefghijklmnopqrstuwxyz
    pal = ""  #palabra de retorno
    
    for car in palabra:
        if car != " ":
            index = ((abc.index(car.lower()) + jump)%len(abc))
            pal = pal + abc[index]
        else:
            pal = pal + car
                     
    salida.insert(INSERT, pal +"\n")

#Encriptacion Cenit Polar
def cenit_polar(palabra):
    p = palabra
    pal = ""    #palabra de retorno
    for i in range(len(p)):
        if p[i] in "cenit":
            if p[i] == "c":
                pal = pal + "p"
            if p[i] == "e":
                pal = pal + "o"
            if p[i] == "n":
                pal = pal + "l"
            if p[i] == "i":
                pal = pal + "a"
            if p[i] == "t":
                pal = pal + "r"
                
        elif p[i] in "polar":
            if p[i] == "p":
                pal = pal + "c"
            if p[i] == "o":
                pal = pal + "e"
            if p[i] == "l":
                pal = pal + "n"
            if p[i] == "a":
                pal = pal + "i"
            if p[i] == "r":
                pal = pal + "t"
        else:
            pal = pal + p[i]
            
    salida.insert(INSERT, pal +"\n")



def selecciona():
    if var.get() == 1:
        cenit_polar(entrada.get())
    elif var.get() == 2:
        encrypt(entrada.get(),entrada2.get())

def activar():
    entrada2.configure(state=NORMAL)
    entrada2.update()
    

        
ventana = Tk()
ventana.title("Encriptacion")
ventana.geometry("500x400") #Dimensiones

var = IntVar() 

frame = Frame(ventana)  
frame.pack()

bottomframe = Frame(ventana)
bottomframe.pack(side=BOTTOM)

label1 = Label(frame, text="Ingrese alguna frase:")
label1.pack()

entrada = Entry(frame,width=50)
entrada.pack()

label2 = Label(frame, text="Seleccione un metodo de encriptacion:")
label2.pack()



botoncesar = Radiobutton(frame,text="Cesar", variable=var, value=2, command=activar)
botoncesar.pack(side=LEFT)

botoncepol = Radiobutton(frame,text="Cenit Polar", variable=var, value=1)
botoncepol.pack(side=RIGHT)



label3 = Label(bottomframe, text="Especifique el salto para la encriptacion cesar:")
label3.pack()

entrada2 = Entry(bottomframe,width=5, state=DISABLED)
entrada2.pack()

botonencrypt = Button(bottomframe, text="Encriptar",command=selecciona)
botonencrypt.pack()

salida = Text(bottomframe)
salida.pack(side=BOTTOM)

ventana.mainloop()
