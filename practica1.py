import tkinter as tk 
from tkinter import scrolledtext
from tkinter import messagebox as mBox
from tkinter import Menu
from tkinter import ttk

#Funcion click
def click():
	ventana=tk.Tk()
	ventana.title("Datos registrados")
	nombre_click=nombre.get()
	apellidoP_click=apellidoP.get()
	apellidoM_click=apellidoM.get()
	direccion_click=direccion.get()
	colonia_click=colonia.get()
	ciudad_click=ciudad.get()
	municipio_click=municipio.get()
	#Espacios de llenado
	ttk.Label(ventana, text= nombre_click).grid (column=0,row=0)
	ttk.Label(ventana, text= apellidoP_click).grid (column=1,row=0)
	ttk.Label(ventana, text= apellidoM_click).grid (column=2,row=0)
	ttk.Label(ventana, text= direccion_click).grid (column=0,row=1)
	ttk.Label(ventana, text= colonia_click).grid (column=1,row=1)
	ttk.Label(ventana, text= ciudad_click).grid (column=0,row=2)
	ttk.Label(ventana, text= municipio_click).grid (column=1,row=2)
	#Radio Botton
	selector=opcion.get()
	ttk.Label(ventana, text="Estado civil:").grid (column=0,row=3)
	if selector==1: ttk.Label(ventana, text="soltero").grid (column=1,row=3)
	elif selector==2: ttk.Label(ventana, text="casado").grid (column=1,row=3)
	elif selector==3: ttk.Label(ventana, text="viudo").grid (column=1,row=3)
	#Botones de Control
	opcion_3_click=opcion_3.get()
	opcion_2_click=opcion_2.get()
	opcion_1_click=opcion_1.get()
	ttk.Label(ventana, text= "hobies:").grid (column=0,row=4)
	if opcion_1_click==1: ttk.Label(ventana, text="leer").grid (column=1,row=4)
	if opcion_2_click==1: ttk.Label(ventana, text="peliculas").grid (column=2,row=4)
	if opcion_3_click==1: ttk.Label(ventana, text="redes sociales").grid (column=3,row=4)
	#Caja de texto
	caja_click=caja.get()
	ttk.Label(ventana, text= "Comentarios:").grid (column=1,row=5)
	ttk.Label(ventana, text=caja_click).grid (column=0, row=1)

#funcion salir
def salir():
	ventana.quit()
	ventana.destroy()
	exit()

#duncion acerca de
def acerca():
	ventana1=tk.Tk()
	ventana1.title("Imprimir")
	ttk.Label(ventana1,text="Gilberto Anguiano Bastien").grid(column=0,row=0)
	ttk.Label(ventana1,text="Col.Indeco, andador de la union #71A").grid(column=0,row=1)
	
ventana=tk.Tk()
ventana.title("Practica 1")

#Menu

barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)

opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Imprimir",command=click)
opciones_menu.add_command(label="Salir",command=salir)
barra_menu.add_cascade(label="Sistema",menu=opciones_menu)

opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Acerca de",command=acerca)
barra_menu.add_cascade(label="Ayuda",menu=opciones_menu)

#Pestaña 1
tabControl = ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text="Datos Gnral")
tabControl.grid(column=0, row=0)

	#ttk.Label(tap1, text= "Captura de alumnos").grid (column=1,row=1)

nombre= tk.StringVar()
nombreCapturado = ttk.Entry(tab1, width=12, textvariable=nombre)
ttk.Label(tab1, text= "Nombre:").grid (column=0,row=2)
nombreCapturado.grid(column=1,row=2)

apellidoP= tk.StringVar()
apellidoPCapturado = ttk.Entry(tab1, width=12, textvariable=apellidoP)
ttk.Label(tab1, text= "Apellido Paterno:").grid (column=0,row=3)
apellidoPCapturado.grid(column=1,row=3)

apellidoM= tk.StringVar()
apellidoMCapturado = ttk.Entry(tab1, width=12, textvariable=apellidoM)
ttk.Label(tab1, text= "Apellido Materno:").grid (column=0,row=4)
apellidoMCapturado.grid(column=1,row=4)

direccion= tk.StringVar()
direccionCapturado = ttk.Entry(tab1, width=12, textvariable=direccion)
ttk.Label(tab1, text= "Direccion :").grid (column=0,row=5)
direccionCapturado.grid(column=1,row=5)

colonia=tk.StringVar()
ttk.Label(tab1, text="Colonia:").grid(column=0,row=6)
coloniaSeleccionado=ttk.Combobox(tab1,width=5, textvariable=colonia)
coloniaSeleccionado['values'] =("Tecnologico","Ventura","Indeco","Torremolinos")
coloniaSeleccionado.grid(column=1,row=6)
coloniaSeleccionado.current(0)

ciudad=tk.StringVar()
ttk.Label(tab1, text="Ciudad:").grid(column=0,row=7)
ciudadSeleccionado=ttk.Combobox(tab1,width=5, textvariable=ciudad)
ciudadSeleccionado['values'] =("Michoacan","Guerrero","Guanajuato","DF")
ciudadSeleccionado.grid(column=1,row=7)
ciudadSeleccionado.current(0)

municipio=tk.StringVar()
ttk.Label(tab1, text="Mucipio:").grid(column=0,row=8)
municipioSeleccionado=ttk.Combobox(tab1,width=5, textvariable=municipio)
municipioSeleccionado['values'] =("Silao","Morelia","Uruapan","Patzcuaro")
municipioSeleccionado.grid(column=1,row=8)
municipioSeleccionado.current(0)

#Pestaña 2
tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text="Inf Pers")

	#Funcion_radio
def funcion_radio():
	selector=opcion.get()
	if selector==1: tab2.congure(background=red)
	
	#Botones de control

ttk.Label(tab2, text= "Pasatiempo:").grid (column=1,row=0)

opcion_1= tk.IntVar()
casilla_1 = tk.Checkbutton(tab2,text="leer", variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=0,row=1,sticky=tk.W)

opcion_2= tk.IntVar()
casilla_2 = tk.Checkbutton(tab2,text="peliculas",variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=1,row=1,sticky=tk.W)

opcion_3= tk.IntVar()
casilla_3 = tk.Checkbutton(tab2,text="Redes sociales", variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=2,row=1,sticky=tk.W)

	#RadioBoton

ttk.Label(tab2, text= "Estado civil:").grid (column=1,row=2)

opcion=tk.IntVar()
radio1=tk.Radiobutton(tab2,text="soltero",variable=opcion,value=1,command=funcion_radio)
radio1.grid(column=0,row=3,sticky=tk.W)

radio2=tk.Radiobutton(tab2,text="casado",variable=opcion,value=2,command=funcion_radio)
radio2.grid(column=1,row=3,sticky=tk.W)

radio3=tk.Radiobutton(tab2,text="viudo",variable=opcion,value=3,command=funcion_radio)
radio3.grid(column=2,row=3,sticky=tk.W)

	#Caja de comentario
scrol_ancho=10
scrol_alto=30

ttk.Label(tab2, text= "Objetivo de la vida").grid (column=1,row=4)

caja = scrolledtext.ScrolledText(tab2, width=scrol_ancho, height=scrol_ancho, wrap=tk.WORD)
caja.grid(column=0, columnspan=1)

accion=ttk.Button(tab2, text="Registrar",command=click)
accion.grid(column=3,row=5)

ventana.mainloop()
