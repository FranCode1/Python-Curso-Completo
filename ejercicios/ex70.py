# =====================================================================
# EJERCICIO 70: Bubble Sort
# ---------------------------------------------------------------------
# • Alturas = [180, 195, 172, 200, 176, 190]
# • Ordenar de mayor a menor (sin sort() ni sorted())
# • Mostrar el más alto y más bajo
# =====================================================================

alturas = [180, 195, 172, 200, 176, 190]

# ---------- Forma 1: Bubble sort clásico ----------
for i in range(len(alturas) - 1):
    for j in range(len(alturas) - 1 - i):
        if alturas[j] < alturas[j + 1]:
            alturas[j], alturas[j + 1] = alturas[j + 1], alturas[j]

print("Forma 1 -> Ordenadas:", alturas)
print("Más alto:", alturas[0])
print("Más bajo:", alturas[-1])

# ---------- Forma 2: Bubble sort con bandera (optimización) ----------
alturas2 = [180, 195, 172, 200, 176, 190]

n = len(alturas2)
for i in range(n - 1):
    cambiado = False
    for j in range(n - 1 - i):
        if alturas2[j] < alturas2[j + 1]:
            alturas2[j], alturas2[j + 1] = alturas2[j + 1], alturas2[j]
            cambiado = True
    if not cambiado:  # Si no hubo cambios, ya está ordenado
        break

print("\nForma 2 -> Ordenadas:", alturas2)
print("Más alto:", alturas2[0])
print("Más bajo:", alturas2[-1])

# ---------- Forma 3: Bubble sort con while ----------
alturas3 = [180, 195, 172, 200, 176, 190]

n = len(alturas3)
ordenado = False
while not ordenado:
    ordenado = True
    for i in range(n - 1):
        if alturas3[i] < alturas3[i + 1]:
            alturas3[i], alturas3[i + 1] = alturas3[i + 1], alturas3[i]
            ordenado = False

print("\nForma 3 -> Ordenadas:", alturas3)
print("Más alto:", alturas3[0])
print("Más bajo:", alturas3[-1])
