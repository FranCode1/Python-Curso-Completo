# ----------------------------------------------------------
# EJERCICIO 12 - Temperaturas Semanales
# ----------------------------------------------------------
# Ingresar la temperatura de cada día de la semana
# Mostrar:
# - Temperatura promedio
# - Temperatura más alta (y qué día)
# - Temperatura más baja (y qué día)


semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']


# =====================================
# MÉTODO 1: Diccionario y un solo bucle
# =====================================
print("\n🔹 MÉTODO 1: Diccionario, promedio, max y min")

temperaturas = {}
suma = 0

for dia in semana:
    temp = float(input(f"Ingresá la temperatura del {dia}: "))
    temperaturas[dia] = temp
    suma += temp

promedio = suma / len(semana)
dia_max = max(temperaturas, key=temperaturas.get)
dia_min = min(temperaturas, key=temperaturas.get)

print(f"\n🌡️ Promedio semanal: {promedio:.2f}°C")
print(f"🔥 Día más caluroso: {dia_max} ({temperaturas[dia_max]}°C)")
print(f"❄️ Día más frío: {dia_min} ({temperaturas[dia_min]}°C)")


# =====================================
# MÉTODO 2: Tuplas (día, temperatura)
# =====================================
print("\n🔹 MÉTODO 2: Lista de tuplas")

datos = []
for dia in semana:
    temp = float(input(f"Temperatura del {dia}: "))
    datos.append((dia, temp))

suma = sum(t for d, t in datos)
prom = suma / len(datos)
maximo = max(datos, key=lambda x: x[1])
minimo = min(datos, key=lambda x: x[1])

print(f"\n📊 Promedio: {prom:.2f}°C")
print(f"🔥 Máxima: {maximo[1]}°C el {maximo[0]}")
print(f"❄️ Mínima: {minimo[1]}°C el {minimo[0]}")


# =====================================
# MÉTODO 3: Dos listas paralelas
# =====================================
print("\n🔹 MÉTODO 3: Lista de días + lista de temperaturas")

temps = []
for dia in semana:
    temp = float(input(f"Temperatura del {dia}: "))
    temps.append(temp)

promedio = sum(temps) / len(temps)
indice_max = temps.index(max(temps))
indice_min = temps.index(min(temps))

print(f"\n📊 Promedio: {promedio:.2f}°C")
print(f"🔥 Día más caluroso: {semana[indice_max]} ({temps[indice_max]}°C)")
print(f"❄️ Día más frío: {semana[indice_min]} ({temps[indice_min]}°C)")


# =====================================
# MÉTODO 4: Orientado a objetos
# =====================================
print("\n🔹 MÉTODO 4: Usando clases")

class DiaTemp:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temp = temperatura

registros = []
for dia in semana:
    temp = float(input(f"{dia.capitalize()}: "))
    registros.append(DiaTemp(dia, temp))

prom = sum(d.temp for d in registros) / len(registros)
mas_caluroso = max(registros, key=lambda d: d.temp)
mas_frio = min(registros, key=lambda d: d.temp)

print(f"\n📊 Promedio: {prom:.2f}°C")
print(f"🔥 Día más caluroso: {mas_caluroso.dia} ({mas_caluroso.temp}°C)")
print(f"❄️ Día más frío: {mas_frio.dia} ({mas_frio.temp}°C)")


# =====================================
# MÉTODO 5: Función general para reutilizar
# =====================================
print("\n🔹 MÉTODO 5: Función para cargar y analizar")

def analizar_temperaturas():
    dias = []
    temps = []
    for dia in semana:
        temp = float(input(f"Temperatura del {dia}: "))
        dias.append(dia)
        temps.append(temp)

    promedio = sum(temps) / len(temps)
    max_idx = temps.index(max(temps))
    min_idx = temps.index(min(temps))

    print(f"\n📊 Promedio: {promedio:.2f}°C")
    print(f"🔥 Máxima: {temps[max_idx]}°C ({dias[max_idx]})")
    print(f"❄️ Mínima: {temps[min_idx]}°C ({dias[min_idx]})")

analizar_temperaturas()
