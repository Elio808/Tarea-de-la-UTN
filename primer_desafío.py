print("(•Ejercicio C)","\n")
print("► PRODUCTOS TEXTILES.","\n\n")
print("•Por favor usar solamente números y el ( . ) pera separa los decimales.","\n")
Camisa=float(input("•Ingrse el precio de la camisa: "))
Pantalon=float(input("•Ingrese el preio de el pantalon: "))
Gorra=float(input("•Ingrese el preio de la gorra: "))
print("\n")
print("► PRECIOS.","\n")
print("•El precio de el camisa es:",Camisa)
print("•El precio de el pantalon es:",Pantalon)
print("•El precio de el gorra es:",Gorra)
print("\n")
print("► SUMA TOTAL MÁS IVA.","\n")
Suma_total_PT= Camisa+Pantalon+Gorra
IVA= Suma_total_PT/100*21
Suma_total_PT_mas_IVA= Camisa+Pantalon+Gorra+IVA
print(Suma_total_PT_mas_IVA)