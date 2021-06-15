calificacion = float(input("Proporciona un valor entre 0 y 10:"))
valor = None
if 9 <= calificacion <=10:
    valor = "A"
elif  8 <= calificacion < 9:
    valor = "B"
elif  7 <= calificacion < 8:
    valor = "C"
elif  6 <= calificacion < 7:
    valor = "D"
elif  0 <= calificacion < 6:
    valor = "F"
else:
    valor = "Valor desconocido"
print("Su calificacion es: ", valor)
