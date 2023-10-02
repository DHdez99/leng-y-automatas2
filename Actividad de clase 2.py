# 0. CREAR UNA LISTA: 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
lista_numeros = [1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9]

# 1. CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
set_numeros = set(lista_numeros)

# 2. CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
suma_lista = sum(lista_numeros)

# 3. CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
suma_set = sum(set_numeros)
# 4. CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS #    NUMEROS UNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET,
#    MAXIMO VALOR, MINIMO VALOR

estadisticas = {
    "numeros_unicos": len(set_numeros),
    "suma_total_lista": suma_lista,
    "suma_total_set": suma_set,
    "maximo_valor": max(lista_numeros),
    "minimo_valor": min(lista_numeros)
}
# 5. IMPRIMIR LAS ESTADISTICAS
for clave, valor in estadisticas.items():
    print(f"{clave}: {valor}")