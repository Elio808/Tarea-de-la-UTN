#TP2 While_Reality_Show
#Fecha: viernes/12/07/2024

# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
# Informar:
# a. nombre del candidato con más votos
# b. nombre y edad del candidato con menos votos
# c. el promedio de edades de los candidatos
# d. total de votos emitidos.
# Todos los datos se ingresan mediante input()

#candidatos
print("\n")
print("♦-----------------------------------------------------------------------------------------------♦")
print("\n")
print("► CANDIDATOS.")
print("\n")
a=(input("• Por favor, ingrese el nombre del candidato número 1: "))
print("\n")
b=(input("• Por favor, ingrese el nombre del candidato número 2: "))
print("\n")
c=(input("• Por favor, ingrese el nombre del candidato número 3: "))
print("\n")
print("♦-----------------------------------------------------------------------------------------------♦")
print("\n")
#Edad
print("► EDAD DE LOS CANDIDATOS.")
print("\n")
print("• Solo se permiten candidatos mayores de 25 años.")
print("\n")
edad_a=int(input("• Por favor, ingrese la edad de "+a+": "))
print("\n")
if edad_a>25:
     edad_b=int(input("• Por favor, ingrese la edad de "+b+": "))
     print("\n")
     if edad_b>25:
        edad_c=int(input("• Por favor, ingrese la edad de "+c+": "))
        if edad_c>25:
            print("\n")
        else:
            print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
            print("\n")
            print("• No se permite candidatos menores de 26 años, el programa no funcionara hasta que se cumpla el requisito de edad minima.")
            print("\n")
            print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
            print("\n")
     else:
        print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
        print("\n")
        print("• No se permite candidatos menores de 26 años, el programa no funcionara hasta que se cumpla el requisito de edad minima.")
        print("\n")
        print("♦------------------------------------------------------------------------------------------------------------------------------♦")
        print("\n")
else:
    print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
    print("\n")
    print("• No se permite candidatos menores de 26 años, el programa no funcionara hasta que se cumpla el requisito de edad minima.")
    print("\n")
    print("♦------------------------------------------------------------------------------------------------------------------------------♦")
    print("\n")
 #votos
if edad_a and edad_b and edad_c>25:
 print("► Votos.")
 print("\n")
 votos_a=int(input("• Por favor, ingrese los votos de "+a+": "))
 print("\n")
 if votos_a>=0:
    votos_b=int(input("• Por favor, ingrese los votos de "+b+": "))
    print("\n")
    if votos_b>=0:
        votos_c=int(input("• Por favor, ingrese los votos de "+c+": "))
        if votos_c>=0:
            print("\n")
        else:
            print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
            print("\n")
            print("• El programa solo funcionara si ingresa números iguales o mayores a 0.")
            print("\n")
            print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
    else:
        print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
        print("\n")
        print("• El programa solo funcionara si ingresa números iguales o mayores a 0.")
        print("\n")
        print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
 else:
    print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
    print("\n")
    print("• El programa solo funcionara si ingresa números iguales o mayores a 0.")
    print("\n")
    print("♦-----------------------------------------------------------------------------------------------------------------------------♦")
if votos_a and votos_b and votos_c>=0:
 print("♦-----------------------------------------------------------------------------------------------♦")
 print("\n")
 #resultados
 print("► CANDIDATO CON MÁS VOTOS.")
 print("\n")
 #mayor
 if votos_a<=votos_b:
    if votos_a==votos_b:
        if votos_a<=votos_c:
            if votos_a==votos_c:
                print(a,b,c)
            else:
                print(c)
        else:
            print(a,b)
    else:
        if votos_b<=votos_c:
            if votos_b==votos_c:
                print(b,c)
            else:
                print(c)
        else:
            print(b)
 else:
    if votos_a<=votos_c:
        if votos_a==votos_c:
            print(a,c)
        else:
            print(c)
    else:
        print(a)
 #menor
 print("\n")
 print("♦-----------------------------------------------------------------------------------------------♦")
 print("\n")
 print("► CANDIDATO CON MENOS VOTOS.")
 print("\n")
 if votos_a>=votos_b:
    if votos_a==votos_b:
        if votos_a>=votos_c:
            if votos_a==votos_c:
                print(a,edad_a,"años,",b,edad_b,"años,",c,edad_c,"años.")
            else:
                print(c,edad_c,"años.")
        else:
            print(a,edad_a,"años,",b,edad_b,"años.")
    else:
        if votos_b>=votos_c:
            if votos_b==votos_c:
                print(b,edad_b,"años,",c,edad_c,"años.")
            else:
                print(c,edad_c,"años.")
        else:
            print(b,edad_b,"años.")
 else:
    if votos_a>=votos_c:
        if votos_a==votos_c:
            print(a,edad_a,"años,",c,edad_c,"años.")
        else:
            print(c,edad_c,"años.")
    else:
        print(a,edad_a,"años.")
 #las dos ultimas mariqueras
 print("\n")
 print("♦-----------------------------------------------------------------------------------------------♦")
 print("\n")
 #promedio de votos
 print("► PROMEDIO DE LAS EDADES DE LOS CANDIDATOS.")
 print("\n")
 promedio=(edad_a+edad_b+edad_c)/3
 print(promedio)
 print("\n")
 print("♦-----------------------------------------------------------------------------------------------♦")
 print("\n")
 print("► VOTOS TOTALES.")
 print("\n")
 total=votos_a+votos_b+votos_c
 print(total)
 print("\n")
 print("♦------------------------------------------------------------------------------------------------♦")
 print("\n")
else:
    print("")
