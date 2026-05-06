# Escenario B – Análisis de Ventas de una Pequeña Empresa

import csv
import os
from collections import defaultdict

ruta_entrada = os.path.join("..", "datos", "ventas.csv")
ventas = []

try:
    with open(ruta_entrada, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Tipos numéricos para poder sumar y calcular promedios
            fila["quantity"] = int(fila["quantity"])
            fila["unit_price"] = float(fila["unit_price"])
            ventas.append(fila)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{ruta_entrada}'.")
    exit()
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

if not ventas:
    print("No se encontraron datos.")
    exit()


def calcular_promedio(lista):
    if not lista:
        return 0.0
    return sum(lista) / len(lista)


# Ingresos totales: suma de (cantidad × precio) por cada fila
ventas_totales = 0.0
for v in ventas:
    ventas_totales += v["quantity"] * v["unit_price"]

# Acumulado de unidades por producto para hallar el más vendido (por cantidad, no por monto)
ventas_por_producto = defaultdict(int)
for v in ventas:
    ventas_por_producto[v["product"]] += v["quantity"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_maxima = ventas_por_producto[producto_mas_vendido]

# Mes como YYYY-MM desde date (se asume fecha tipo YYYY-MM-DD)
ventas_por_mes = defaultdict(float)
for v in ventas:
    mes = v["date"][:7]
    ventas_por_mes[mes] += v["quantity"] * v["unit_price"]

# Promedio del monto de cada transacción (línea del CSV)
montos_transaccion = [v["quantity"] * v["unit_price"] for v in ventas]
promedio_transaccion = calcular_promedio(montos_transaccion)

print("=== RESULTADOS DEL ANÁLISIS DE VENTAS ===")
print(f"Ventas totales: ${ventas_totales:,.2f}")
print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_maxima} unidades)")
print(f"Promedio por transacción: ${promedio_transaccion:,.2f}")
print("\nVentas por mes:")
for mes, total in sorted(ventas_por_mes.items()):
    print(f"  {mes}: ${total:,.2f}")

os.makedirs(os.path.join("resultados"), exist_ok=True)
ruta_resumen = os.path.join("resultados", "resumen_ventas.csv")

with open(ruta_resumen, mode="w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Indicador", "Valor"])
    escritor.writerow(["Ventas totales", f"${ventas_totales:,.2f}"])
    escritor.writerow(["Producto más vendido", producto_mas_vendido])
    escritor.writerow(["Cantidad producto más vendido", cantidad_maxima])
    escritor.writerow(["Promedio por transacción", f"${promedio_transaccion:,.2f}"])
    # Misma hoja: una fila por mes para no generar otro archivo
    for mes, total in sorted(ventas_por_mes.items()):
        escritor.writerow([f"Ventas {mes}", f"${total:,.2f}"])

print(f"\nResumen guardado en: {ruta_resumen}")

try:
    import matplotlib.pyplot as plt

    meses = sorted(ventas_por_mes.keys())
    totales = [ventas_por_mes[m] for m in meses]

    plt.figure(figsize=(8, 5))
    plt.bar(meses, totales, color="skyblue")
    plt.title("Evolución de ventas por mes")
    plt.xlabel("Mes")
    plt.ylabel("Ventas totales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guarda en la carpeta resultados de la raíz del repo (un nivel arriba de scripts/)
    ruta_grafico = os.path.join("..", "resultados", "ventas_por_mes.png")
    plt.savefig(ruta_grafico)
    plt.close()  # Evita que se muestre la figura en el notebook innecesariamente
    print(f"Gráfico guardado en: {ruta_grafico}")
except ImportError:
    print("No se pudo generar el gráfico (matplotlib no disponible).")
