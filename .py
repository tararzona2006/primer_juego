from tkinter import*
import random
#----------------------------------------
#----------variables globales------------
#----------------------------------------

BASE = 760
ALTURA = 566
radio= 10
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2



centro_x = random.randint(radio, BASE)
centro_y = random.randint(radio, ALTURA)

def mover_carros():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = c.coords(carro1,carro2)
    if x0 < 0 or x1 > BASE: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > ALTURA: 
        desplazamiento_y = -desplazamiento_y
    c.move(carro2,carro1 ,desplazamiento_x, desplazamiento_y)
    iniciar = ventana_principal.after(intervalo, mover_carros)

    if x0 > 300:
        desplazamiento_x = 0






#----------------------------------------
#----------VENTANA PRINCIPAL-------------
#----------------------------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("800x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

#----------------------------------------
#----------frame de graficacion----------
#----------------------------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="red", width=780 , height=580 )
frame_graficacion.place(x=10 , y=10)

#creacion canvas

c = Canvas (frame_graficacion , width=BASE, height=ALTURA)
c.config(bg="white")
c.place(x=10,y=10)



# img
carro1 = PhotoImage(file="img/carro1.png")
Car = c.create_image(100/2, 390/2, image = carro1)

carro2 = PhotoImage(file="img/carro2.png")
Car = c.create_image(100/2, ALTURA/2, image = carro2)



# dibujar lineas
rect_1 = c. create_rectangle(BASE/2-280,ALTURA/2+170,BASE/2-200,30/2, fill="dark gray")
rect_2 = c. create_rectangle(BASE/2+280,ALTURA/2+170,BASE-20,30/2, fill="dark gray")
rect_3 = c. create_rectangle(BASE/2-200,ALTURA/2-160,BASE-100,ALTURA/2+90, fill="BLACK")
rect_4 = c. create_rectangle(BASE/2-180,ALTURA/2-30,BASE/2-80,ALTURA/2-60, fill="white")
rect_5 = c. create_rectangle(BASE/2-70,ALTURA/2-30,BASE/2+30,ALTURA/2-60, fill="white")
rect_6 = c. create_rectangle(BASE/2+40,ALTURA/2-30,BASE/2+140,ALTURA/2-60, fill="white")
rect_7 = c. create_rectangle(BASE/2+150,ALTURA/2-30,BASE/2+260,ALTURA/2-60, fill="white")


# texto
nombre_1 = c. create_text(BASE/2-240,ALTURA/2-190,anchor="center",text="S",font=("arial",25, "bold"),fill="blue")
nombre_2 = c. create_text(BASE/2-240,ALTURA/2-130,anchor="center",text="A",font=("arial",25, "bold"),fill="blue")
nombre_3 = c. create_text(BASE/2-240,ALTURA/2-70,anchor="center",text="L",font=("arial",25, "bold"),fill="blue")
nombre_4 = c. create_text(BASE/2-240,ALTURA/2-10,anchor="center",text="I",font=("arial",25, "bold"),fill="blue")
nombre_5 = c. create_text(BASE/2-240,ALTURA/2+50,anchor="center",text="D",font=("arial",25, "bold"),fill="blue")
nombre_6 = c. create_text(BASE/2-240,ALTURA/2+110,anchor="center",text="A",font=("arial",25, "bold"),fill="blue")
nombre_7 = c. create_text(BASE/2+320,ALTURA/2-120,anchor="center",text="F",font=("arial",25, "bold"),fill="blue")
nombre_8 = c. create_text(BASE/2+320,ALTURA/2-60,anchor="center",text="I",font=("arial",25, "bold"),fill="blue")
nombre_9 = c. create_text(BASE/2+320,ALTURA/2,anchor="center",text="N",font=("arial",25, "bold"),fill="blue")

# boton
bandera=PhotoImage(file="img/an.png")
bt_bandera =Button(ventana_principal)
bt_bandera.config(image=bandera, width=100, height=100)
bt_bandera.place(x=400, y=400)






# desplegar ventana
ventana_principal.mainloop()
mover_carros()