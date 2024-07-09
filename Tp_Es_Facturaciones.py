#Tp Facturaciones
#fecha: 06/07/2024

#Enunciado:
#Para el departamento de facturación:


#A. Ingresar tres precios de productos y mostrar la suma de los mismos.
print("\n")
print("♦-----------------------------------------------------------------------------------------------♦")
print("(•Ejercicio A)","\n")
print("► PRODUCTOS ORGANICOS.","\n\n")
print("•Por favor usar solamente números y el ( . ) para separa los decimales.","\n")
Arroz=float(input("•Ingrse el precio de el arroz: "))
Tomate=float(input("•Ingrese el preio de el tomante: "))
Cebolla=float(input("•Ingrese el preio de la cebolla: "))
print("\n")
print("► PRECIOS.","\n")
print("•El precio de el arroz es:",Arroz)
print("•El precio de el tomate es:",Tomate)
print("•El precio de la cebolla es:",Cebolla)
print("\n")
print("► SUMA TOTAL.","\n")
Suma_total=Arroz+Tomate+Cebolla
print(Suma_total)
print("\n")
print("♦-----------------------------------------------------------------------------------------------♦")
#B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
print("(•Ejercicio B)","\n")
print("► PRODUCTOS ANIMALES.","\n\n")
print("•Por favor usar solamente números y el ( . ) para separa los decimales.","\n")
Pollo=float(input("•Ingrse el precio de el pollo: "))
Res=float(input("•Ingrese el preio de la res: "))
Cerdo=float(input("•Ingrese el preio de el cerdo: "))
print("\n")
print("► PRECIOS.","\n")
print("•El precio de el pollo es:",Pollo)
print("•El precio de la res es:",Res)
print("•El precio de el cerdo es:",Cerdo)
print("\n")
print("► PROMEDIO DE PREICIOS.","\n")
Promedio=((Pollo+Res+Cerdo)/3)
print(Promedio)
print("\n")
print("♦-----------------------------------------------------------------------------------------------♦")
#C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
print("(•Ejercicio C)","\n")
print("► PRODUCTOS TEXTILES.","\n\n")
print("•Por favor usar solamente números y el ( . ) para separa los decimales.","\n")
Camisa=float(input("•Ingrse el precio de la camisa: "))
Pantalon=float(input("•Ingrese el preio de el pantalon: "))
Gorra=float(input("•Ingrese el preio de la gorra: "))
print("\n")
print("► PRECIOS.","\n")
print("•El precio de la camisa es:",Camisa)
print("•El precio de el pantalon es:",Pantalon)
print("•El precio de la gorra es:",Gorra)
print("\n")
print("► SUMA TOTAL MÁS IVA.","\n")
Suma_total_PT= Camisa+Pantalon+Gorra
IVA= Suma_total_PT/100*21
Suma_total_PT_mas_IVA= Camisa+Pantalon+Gorra+IVA
print(Suma_total_PT_mas_IVA)
print("\n")
print("♦-----------------------------------------------------------------------------------------------♦")