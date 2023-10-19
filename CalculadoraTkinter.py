from tkinter import * #* es para importar todo

ventana = Tk()
ventana.title("Calculadora") #Título de la ventana
ventana.geometry("400x300")

i = 0

#Entrada
e_texto = Entry(ventana, font= ("Calibri 30")) #Caja de texto
e_texto.grid(row = 0, column = 0, columnspan= 4, padx= 50, pady= 5) #Columnspan indica cuántas columnas ocupa el cuadro

#Funciones
def click_boton(valor):
    global i #Accedo a la variable global i
    e_texto.insert(i, valor) #Inserto el valor del botón en la caja de texto, el primer parámetro (i) es el Index(índice), donde va a estar ubicado el segundo parámetro (valor)
    i += 1 #Probar con len(e_texto.get()) para usar la longitud del input en vez de la variable global !!!

def borrar():
    e_texto.delete(0,END) #Borra desde el inicio hasta el final.

def operaciones():
    ecuacion = e_texto.get() #.get me sirve para guardar en la variable ecuación todo lo que esté en la caja de texto.
    resultado = eval(ecuacion)
    e_texto.delete(0, END) #Borro lo que esta en el cuadro de texto
    e_texto.insert(0, resultado) #Inserto en el cuadro de texto lo que esta guardado en resultado, en la posición 0
    i = 0 #Reinicio la variable global

#Botones
boton1 = Button(ventana, text= "1", width= 5, height= 2, command= lambda: click_boton(1)) #command para conectar un botón a una función, se le agrega lambda para poder ponerle parametros, con command no se ponen paréntesis
boton2 = Button(ventana, text= "2", width= 5, height= 2, command= lambda: click_boton(2))
boton3 = Button(ventana, text= "3", width= 5, height= 2, command= lambda: click_boton(3))
boton4 = Button(ventana, text= "4", width= 5, height= 2, command= lambda: click_boton(4))
boton5 = Button(ventana, text= "5", width= 5, height= 2, command= lambda: click_boton(5))
boton6 = Button(ventana, text= "6", width= 5, height= 2, command= lambda: click_boton(6))
boton7 = Button(ventana, text= "7", width= 5, height= 2, command= lambda: click_boton(7))
boton8 = Button(ventana, text= "8", width= 5, height= 2, command= lambda: click_boton(8))
boton9 = Button(ventana, text= "9", width= 5, height= 2, command= lambda: click_boton(9))
boton0 = Button(ventana, text= "0", width= 16, height= 2, command= lambda: click_boton(0))

boton_borrar = Button(ventana, text= "AC", width= 5, height= 2, command= borrar)
boton_parentesis1 = Button(ventana, text= "(", width= 5, height= 2, command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text= ")", width= 5, height= 2, command= lambda: click_boton(")"))
boton_punto = Button(ventana, text= ".", width= 5, height= 2, command= lambda: click_boton())

boton_div = Button(ventana, text= "/", width= 5, height= 2, command= lambda: click_boton("/"))
boton_mult = Button(ventana, text= "*", width= 5, height= 2, command= lambda: click_boton("*"))
boton_sum = Button(ventana, text= "+", width= 5, height= 2, command= lambda: click_boton("+"))
boton_rest = Button(ventana, text= "-", width= 5, height= 2, command= lambda: click_boton("-"))
boton_igual = Button(ventana, text= "=", width= 5, height= 2, command= operaciones)
boton = Button(ventana, text= "", width= 5, height= 2)

#Agregar botones en pantalla

boton_borrar.grid(row= 1, column= 0, padx= 5, pady= 5)
boton_parentesis1.grid(row= 1, column= 1, padx= 5, pady= 5)
boton_parentesis2.grid(row= 1, column= 2, padx= 5, pady= 5)
boton_div.grid(row= 1, column= 3, padx= 5, pady= 5)

boton7.grid(row= 2, column= 0, padx= 5, pady= 5)
boton8.grid(row= 2, column= 1, padx= 5, pady= 5)
boton9.grid(row= 2, column= 2, padx= 5, pady= 5)
boton_sum.grid(row= 2, column= 3, padx= 5, pady= 5)

boton4.grid(row= 3, column= 0, padx= 5, pady= 5)
boton5.grid(row= 3, column= 1, padx= 5, pady= 5)
boton6.grid(row= 3, column= 2, padx= 5, pady= 5)
boton_rest.grid(row= 3, column= 3, padx= 5, pady= 5)

boton1.grid(row= 4, column= 0, padx= 5, pady= 5)
boton2.grid(row= 4, column= 1, padx= 5, pady= 5)
boton3.grid(row= 4, column= 2, padx= 5, pady= 5)
boton_mult.grid(row= 4, column= 3, padx= 5, pady= 5)

boton0.grid(row= 5, column= 0, columnspan= 2, padx= 5, pady= 5)
boton_punto.grid(row= 5, column= 2, padx= 5, pady= 5)
boton_igual.grid(row= 5, column= 3, padx= 5, pady= 5)

ventana.mainloop() #El mainloop va a reconocer todos los eventos que ocurran