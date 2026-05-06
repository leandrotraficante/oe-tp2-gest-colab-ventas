# Retail Sales Insights

Análisis automatizado de ventas a partir de un CSV: calcula totales, producto más vendido (por unidades), promedio por transacción, ventas por mes y exporta un resumen en CSV; opcionalmente genera un gráfico PNG si está instalado `matplotlib`.

---

## Estructura del repositorio

```text
.
├── datos/
│   └── ventas.csv              # Entrada: transacciones
├── scripts/
│   ├── analisis_ventas.py      # Script principal (ver ejecución abajo)
│   └── resultados/             # Salida: resumen_ventas.csv (se crea al ejecutar)
├── resultados/                 # Salida: ventas_por_mes.png (si hay matplotlib)
├── .gitignore
└── README.md
```

---

## Cómo reproducir el análisis

El script usa rutas relativas respecto del **directorio de trabajo actual**: debe ejecutarse **desde la carpeta `scripts/`** (así `..` apunta a la raíz del repo y encuentra `datos/` y `resultados/` del gráfico).

```bash
cd scripts
python analisis_ventas.py
```

> No alcanza con estar en la raíz y llamar `python scripts/analisis_ventas.py`: el proceso sigue teniendo como cwd la raíz y las rutas `..` no coinciden. En Google Colab, tras clonar, usá `%cd nombre-repo/scripts` y luego `!python analisis_ventas.py`.

### Dependencia opcional (gráfico)

Para generar `resultados/ventas_por_mes.png` en la raíz del proyecto:

```bash
pip install matplotlib
```

Si no está instalado, el script igual corre y guarda el CSV de resumen; solo mostrará un aviso sobre el gráfico.

### Formato de datos (`datos/ventas.csv`)

El script espera al menos las columnas `**date**`, `**product**`, `**quantity**`, `**unit_price**`. La fecha debe permitir tomar el mes con los primeros 7 caracteres (`YYYY-MM`).

### Salidas generadas


| Ubicación             | Archivo              | Contenido                                                 |
| --------------------- | -------------------- | --------------------------------------------------------- |
| `scripts/resultados/` | `resumen_ventas.csv` | Indicadores y filas `Ventas YYYY-MM` por mes              |
| `resultados/` (raíz)  | `ventas_por_mes.png` | Gráfico de barras por mes (si matplotlib está disponible) |


---

## Repositorio en GitHub

[https://github.com/leandrotraficante/oe-tp2-gest-colab-ventas](https://github.com/leandrotraficante/oe-tp2-gest-colab-ventas)

---

## Contexto académico (UTN — Organización Empresarial)

- **Institución:** Universidad Tecnológica Nacional (UTN), Tecnicatura Universitaria en Programación a Distancia.  
- **Cátedra:** Organización Empresarial. **Año lectivo:** 2026.  
- **Trabajo práctico:** Gestión colaborativa, control de versiones (Git, GitHub) y planificación con Jira.

**Integrante:** Leandro Traficante (en el enunciato figuran los roles P1/P2/P3; con un solo integrante conviene reflejar las tres tareas en Jira asignadas al mismo usuario).

**Trazabilidad:** los mensajes de commit deben comenzar con el **ID del issue de Jira** (ej. `OE2-1: descripción breve`).

**Entrega:** enlace al repositorio público, proyecto Jira compartido con docentes e **informe en PDF** según las normas del enunciado. No publicar tokens ni credenciales.