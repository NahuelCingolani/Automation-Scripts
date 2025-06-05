import csv

def analizar_ventas(nombre_archivo):
    ventas_totales = 0
    por_categoria = {}
    producto_top = ("", 0)

    with open(nombre_archivo, newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            monto = int(fila["Monto"])
            categoria = fila["Categoria"]
            producto = fila["Producto"]

            ventas_totales += monto

            if categoria in por_categoria:
                por_categoria[categoria] += monto
            else:
                por_categoria[categoria] = monto

            if monto > producto_top[1]:
                producto_top = (producto, monto)

    categorias_ordenadas = sorted(por_categoria.items(), key=lambda x: x[1], reverse=True)

    # Mostrar en consola
    print(f"Ventas totales: ${ventas_totales}")
    print("\nVentas por categoría (ordenadas):")
    for categoria, total in categorias_ordenadas:
        print(f"  {categoria}: ${total}")

    print("\nPorcentaje por categoría:")
    for categoria, total in categorias_ordenadas:
        porcentaje = (total / ventas_totales) * 100
        print(f"  {categoria}: {porcentaje:.2f}%")

    print(f"\nProducto más vendido: {producto_top[0]} (${producto_top[1]})")

    # Exportar a archivo .txt
    with open("resumen_ventas.txt", "w") as resumen:
        resumen.write(f"Ventas totales: ${ventas_totales}\n\n")
        resumen.write("Ventas por categoría (ordenadas):\n")
        for categoria, total in categorias_ordenadas:
            resumen.write(f"  {categoria}: ${total}\n")

        resumen.write("\nPorcentaje por categoría:\n")
        for categoria, total in categorias_ordenadas:
            porcentaje = (total / ventas_totales) * 100
            resumen.write(f"  {categoria}: {porcentaje:.2f}%\n")

        resumen.write(f"\nProducto más vendido: {producto_top[0]} (${producto_top[1]})\n")

# Ejecutar
analizar_ventas("C:/Users/nahue/OneDrive/Desktop/Progreso en 1 mes/ventas.csv")

