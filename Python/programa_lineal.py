
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

FECHA_INICIO = date(2025, 10, 26)

tareas = {
    "A": {"dur": 5, "pred": []},       # no tiene precedentes(es la primera)
    "B": {"dur": 2, "pred": ["A"]},
    "C": {"dur": 3, "pred": ["B"]},
    "J": {"dur": 5, "pred": ["C"]},
    "D": {"dur": 4, "pred": ["C"]},
    "E": {"dur": 2, "pred": ["D", "J"]},
    "F": {"dur": 3, "pred": ["B"]},
    "G": {"dur": 6, "pred": ["F"]},
    "H": {"dur": 1, "pred": ["G"]},
    "I": {"dur": 4, "pred": ["H"]},
}

ruta_critica = ["A", "B", "F", "G", "H", "I"]


for nombre, info in tareas.items():
    pred = info["pred"]

    if not pred:
        ES = 0
    else:
        ES = max(tareas[p]["EF"] for p in pred)

    EF = ES + info["dur"]

    info["ES"] = ES
    info["EF"] = EF
    info["Inicio"] = FECHA_INICIO + timedelta(days=ES)
    info["Fin"] = FECHA_INICIO + timedelta(days=EF)

duracion_total = max(info["EF"] for info in tareas.values())


filas = []
for nombre, info in tareas.items():
    filas.append({
        "Tarea": nombre,
        "Inicio": info["Inicio"],
        "Fin": info["Fin"],
        "Status": "Ruta Crítica" if nombre in ruta_critica else "Actividad Normal",
        "dias_inicio": info["ES"],
        "dias_fin": info["EF"],
        "dias_inicio_fin": info["dur"],   # duración de la tarea
    })

df = pd.DataFrame(filas).sort_values("dias_inicio").reset_index(drop=True)

print("=== CRONOGRAMA (CPM) ===")
print(df)
print()
print(f"Duración total del proyecto (días): {duracion_total}")
print("Ruta crítica (una posible): " + " -> ".join(ruta_critica))

def color(row):
    return "#E64646" if row["Status"] == "Ruta Crítica" else "#4F81BE"
df["color"] = df.apply(color, axis=1)

fig, ax = plt.subplots(1, figsize=(16, 6))

ax.barh(
    df["Tarea"],
    df["dias_inicio_fin"],
    left=df["dias_inicio"],
    color=df["color"],
    edgecolor="black"
)
ax.set_xlabel("Días desde el inicio del proyecto")
ax.set_ylabel("Tareas")
ax.set_title("Diagrama de Gantt — CPM (Unidad 3)")

c_dict = {"Ruta Crítica": "#E64646", "Actividad Normal": "#4F81BE"}
leyenda = [Patch(facecolor=c_dict[nombre], label=nombre) for nombre in c_dict]
ax.legend(handles=leyenda, loc="lower right")

plt.tight_layout()
plt.show()
