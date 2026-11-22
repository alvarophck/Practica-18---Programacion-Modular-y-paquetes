# Versión "notebook": cada bloque corresponde a una celda del .ipynb original

# Celda [1] · Cargar los datos
datos = """id,cliente,ciudad,importe,estado
P001, Ana López ,madrid,45.50,entregado
P002,Luis Pérez,Sevilla,12.00,cancelado
P003,Marta Ruiz,MADRID,30.25,entregado
P004,Jorge Gil,valencia,,entregado
P005,Elena Sanz,sevilla,80.00,entregado
P006,Pablo Ríos,Valencia,22.40,en reparto
P007,Sara Mora,madrid,abc,entregado"""
lineas = datos.split("\n")[1:]
print("Pedidos leídos:", len(lineas))

# Celda [2] · Limpiar y descartar errores
filas = []
rechazados = []
for l in lineas:
    c = [x.strip() for x in l.split(",")]
    try:
        imp = float(c[3])
        filas.append([c[0], c[1].title(), c[2].title(), imp, c[4].lower()])
    except ValueError:
        rechazados.append(c[0])
print("Rechazados por datos erróneos:", rechazados)

# Celda [3] · Quitar cancelados y calcular el IVA
cancelados = [f[0] for f in filas if f[4] == "cancelado"]
filas = [f for f in filas if f[4] != "cancelado"]
for f in filas:
    f.append(round(f[3] * 1.21, 2))
print("Pedidos cancelados:", cancelados)
print("Pedidos procesados:", len(filas))

# Celda [4] · Agregar por ciudad
resumen = {}
for f in filas:
    resumen[f[2]] = round(resumen.get(f[2], 0) + f[5], 2)
resumen = dict(sorted(resumen.items(), key=lambda x: x[1], reverse=True))

# Celda [5] · Mostrar el informe
print("Ventas con IVA por ciudad:")
for ciudad, total in resumen.items():
    print(f"  {ciudad:<9}{total:>8.2f} €")
