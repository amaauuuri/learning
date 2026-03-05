# Autor: Amau - Unidad 3 

from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 1) DATOS DEL PROYECTO (EDITA SOLO ESTA SECCIÓN)

tareas = {
    "A": {"dur": 5, "pred": []},
    "B": {"dur": 2, "pred": []},
    "C": {"dur": 3, "pred": ["B"]},
    "D": {"dur": 4, "pred": []},
    "E": {"dur": 2, "pred": ["D","J"]},
    "F": {"dur": 3, "pred": ["B"]},
    "G": {"dur": 6, "pred": ["F"]},
    "H": {"dur": 1, "pred": ["G"]},
    "I": {"dur": 4, "pred": ["H"]},
    "J": {"dur": 5, "pred": ["C"]},
}

FECHA_INICIO = date.today()  

# 2) CPM 
sucesoras = {k: [] for k in tareas}
for act, info in tareas.items():
    for p in info["pred"]:
        sucesoras[p].append(act)

in_deg = {k: len(v["pred"]) for k,v in tareas.items()}
orden = []
cola = [k for k,d in in_deg.items() if d==0]
while cola:
    u = cola.pop(0)
    orden.append(u)
    for v in sucesoras[u]:
        in_deg[v] -= 1
        if in_deg[v]==0:
            cola.append(v)

if len(orden) != len(tareas):
    raise ValueError("La red tiene un ciclo. Revisa las dependencias.")

ES, EF = {}, {}
for u in orden:
    if not tareas[u]["pred"]:
        ES[u] = 0
    else:
        ES[u] = max(EF[p] for p in tareas[u]["pred"])
    EF[u] = ES[u] + tareas[u]["dur"]

dur_total = max(EF.values())

LF, LS = {}, {}
# actividades sin sucesoras: LF = duración total
finales = [k for k in tareas if len(sucesoras[k])==0]
for u in reversed(orden):
    if u in finales:
        LF[u] = dur_total
    else:
        LF[u] = min(LS[s] for s in sucesoras[u])
    LS[u] = LF[u] - tareas[u]["dur"]

# Holgura y estado crítico
SLACK = {k: LS[k]-ES[k] for k in tareas}
critico = {k: (abs(SLACK[k]) < 1e-9) for k in tareas}  

# Intento de ruta crítica:
# empezamos con actividades críticas sin predecesoras críticas y encadenamos
ruta = []
candidatos_inicio = [k for k in orden if critico[k] and not any(critico[p] for p in tareas[k]["pred"])]
if candidatos_inicio:
    cur = candidatos_inicio[0]
    ruta.append(cur)
    while True:
        # buscar sucesora crítica cuyo ES == EF de la actual
        nxt = None
        for s in sucesoras[cur]:
            if critico[s] and abs(ES[s]-EF[cur])<1e-9:
                nxt = s; break
        if nxt is None:
            break
        ruta.append(nxt)
        cur = nxt


# 3) Construccion de calendario
rows = []
for k in orden:
    inicio = FECHA_INICIO + timedelta(days=ES[k])
    fin    = FECHA_INICIO + timedelta(days=EF[k])
    rows.append({
        "Tarea": k,
        "Inicio": inicio,
        "Fin": fin,
        "Duración (días)": tareas[k]["dur"],
        "ES": ES[k], "EF": EF[k],
        "LS": LS[k], "LF": LF[k],
        "Holgura": SLACK[k],
        "Status": "Ruta Crítica" if critico[k] else "Actividad Normal"
    })

df = pd.DataFrame(rows).sort_values(by=["ES","Tarea"]).reset_index(drop=True)

print("\n=== CRONOGRAMA (CPM) ===")
print(df[["Tarea","Inicio","Fin","Duración (días)","ES","EF","LS","LF","Holgura","Status"]])
print("\nDuración total del proyecto (días):", dur_total)
print("Ruta crítica (una posible):", " → ".join(ruta) if ruta else "(múltiples rutas críticas)")


# 4) Gráfico de Gantt (críticas en rojo)
df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"]    = pd.to_datetime(df["Fin"])
base = pd.Timestamp(FECHA_INICIO)
df["dias_inicio"]     = (df["Inicio"] - base).dt.days
df["dias_fin"]        = (df["Fin"]    - base).dt.days
df["dias_inicio_fin"] = df["dias_fin"] - df["dias_inicio"]

def color(row):
    return "#E64646" if row["Status"]=="Ruta Crítica" else "#4F81BE"

df = df.sort_values("ES", ascending=True)

fig, ax = plt.subplots(1, figsize=(12,6))
ax.barh(
    df["Tarea"],
    df["dias_inicio_fin"],
    left=df["dias_inicio"],
    color=[color(r) for _,r in df.iterrows()],
    edgecolor="black"
)

from matplotlib.patches import Patch
leyenda = [Patch(facecolor="#E64646", label="Ruta crítica"),
           Patch(facecolor="#4F81BE", label="Actividad normal")]
plt.legend(handles=leyenda, loc="lower right")

ax.set_xlabel("Días desde el inicio del proyecto")
ax.set_ylabel("Tareas")
ax.set_title("Diagrama de Gantt – CPM (Unidad 3)")
plt.tight_layout()
plt.show()
