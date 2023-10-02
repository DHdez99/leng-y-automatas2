texto = "SON LAS 7 DE LA NOCHE Y YA ME QUIERO IR"

# Buscar la posición del número 7 en el texto
posicion_7 = texto.find('7')

# Verificar si se encontró el número 7 y si es menor a 8
if posicion_7 != -1 and int(texto[posicion_7]) < 8:
    numero_7 = int(texto[posicion_7])
    mensaje = f"ES HORA DE IRNOS SON LAS: {numero_7}"
    print(numero_7)
    print(mensaje)