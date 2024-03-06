from tkinter import * #* es para importar todo
from tkinter.font import Font
import tkinter as tk

#validate_entry = lambda text: text.isdecimal() # Para que sólo acepte números

ventana = Tk()

ventana.configure(bg="#7C7979")
ventana.title("Calculadora") #Título de la ventana
#ventana.geometry("520x440") # Ancho x Alto
ventana.resizable(height=0, width=0) # Para que no cambie de tamaño

fuente = Font(family="Helvetica", size=10)

i = 0

#Entrada
e_texto = Entry(ventana, background="grey", foreground="black", font= ("Calibri 30")) #Caja de texto
e_texto.grid(row = 0, columnspan= 4, padx= 60, pady= 9) # Grid es para posicionar. Columnspan indica cuántas columnas ocupa el cuadro
e_texto.configure(bg="#CFC8C8")

#Funciones
def click_boton(valor):
    global i #Accedo a la variable global i
    e_texto.insert(i, valor) #Inserto el valor del botón en la caja de texto, el primer parámetro (i) es el Index(índice), donde va a estar ubicado el segundo parámetro (valor)
    i += 1 #Probar con len(e_texto.get()) para usar la longitud del input en vez de la variable global !!!

def borrar():
    e_texto.delete(len(e_texto.get())-1)

def borrar_todo():
    e_texto.delete(0,END) #Borra desde el inicio hasta el final.

def operaciones():
    try: # Primero pruebo esto, y paso a except en caso de que trate de dividir por 0
        ecuacion = e_texto.get() #.get me sirve para guardar en la variable ecuación todo lo que esté en la caja de texto.
        resultado = eval(ecuacion)
        e_texto.delete(0, END) #Borro lo que esta en el cuadro de texto , si no lo hago aparece el resultado junto con la operación
        e_texto.insert(0, resultado) #Inserto en el cuadro de texto lo que esta guardado en resultado, en la posición 0
    except (ZeroDivisionError, NameError, TypeError, SyntaxError):
        e_texto.delete(0, END)
        e_texto.insert(0,"Error")

#Botones
boton1 = Button(ventana, text= "1", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(1)) #command para conectar un botón a una función, se le agrega lambda para poder ponerle parametros, con command no se ponen paréntesis
boton2 = Button(ventana, text= "2", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(2))
boton3 = Button(ventana, text= "3", height= 4, width= 9, font=fuente,bg="#5A5A5A", fg="white", command= lambda: click_boton(3))
boton4 = Button(ventana, text= "4", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(4))
boton5 = Button(ventana, text= "5", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(5))
boton6 = Button(ventana, text= "6", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(6))
boton7 = Button(ventana, text= "7", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(7))
boton8 = Button(ventana, text= "8", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(8))
boton9 = Button(ventana, text= "9", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(9))
boton0 = Button(ventana, text= "0", height= 4, width= 9, font=fuente, bg="#5A5A5A", fg="white", command= lambda: click_boton(0))

boton_borrar = Button(ventana, text= "C", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white",command= borrar)
boton_borrarTodo = Button(ventana, text= "CA", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= borrar_todo)
boton_parentesis1 = Button(ventana, text= "(", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text= ")", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= lambda: click_boton(")"))
boton_punto = Button(ventana, text= ".", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= lambda: click_boton("."))

boton_div = Button(ventana, text= "/", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= lambda: click_boton("/"))
boton_mult = Button(ventana, text= "*", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= lambda: click_boton("*"))
boton_sum = Button(ventana, text= "+", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= lambda: click_boton("+"))
boton_rest = Button(ventana, text= "-", height= 4, width= 9, font=fuente, bg="#3B3838", fg="white", command= lambda: click_boton("-"))
boton_igual = Button(ventana, text= "=", height= 4, width= 9, font=fuente, bg="#107CCB", fg="white", command= operaciones)

#Agregar botones en pantalla

boton_borrar.grid(row= 1, column= 0)
boton_borrarTodo.grid(row= 1, column= 1)
boton_parentesis1.grid(row= 1, column= 2)
boton_parentesis2.grid(row= 1, column= 3)


boton7.grid(row= 2, column= 0, padx=0, pady=0)
boton8.grid(row= 2, column= 1, padx=0, pady=0)
boton9.grid(row= 2, column= 2, padx=0, pady=0)
boton_sum.grid(row= 2, column= 3, padx=0, pady=0)

boton4.grid(row= 3, column= 0)
boton5.grid(row= 3, column= 1)
boton6.grid(row= 3, column= 2)
boton_rest.grid(row= 3, column= 3)

boton1.grid(row= 4, column= 0)
boton2.grid(row= 4, column= 1)
boton3.grid(row= 4, column= 2)
boton_mult.grid(row= 4, column= 3)

boton0.grid(row= 5, column= 0)
boton_punto.grid(row= 5, column= 2)
boton_igual.grid(row= 5, column= 1)
boton_div.grid(row= 5, column= 3)

ventana.mainloop() #El mainloop va a reconocer todos los eventos que ocurran