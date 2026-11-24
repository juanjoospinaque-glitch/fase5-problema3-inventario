# Matriz de inventario
inventario = [
    ["A001", "Arroz", 5, 20],
    ["A002", "Aceite", 10, 10],
    ["A003", "Azúcar", 50, 15],
    ["A004", "Leche", 0, 8],
    ["A005", "Café", 3, 12],
    ["A006", "Harina", 30, 10]
]


# Funcion para calcular la cantidad que se debe pedir
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Mostrar el reporte de inventario
print("REPORTE DE REABASTECIMIENTO")
print("---------------------------")

for articulo in inventario:
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

    print(nombre, "- Cantidad a pedir:", cantidad)