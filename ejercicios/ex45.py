# =====================================================================
# EJERCICIO 45: Sistema de votos
# ---------------------------------------------------------------------
# En una elección escolar participan 3 listas (A, B y C). Los alumnos votan ingresando A, B o C
# (no distinguir mayúsculas/minúsculas). El proceso termina cuando se ingresa "FIN".
# El sistema debe:
# - Contar los votos de cada lista.
# - Validar votos incorrectos.
# - Mostrar el total de votos y cuál lista ganó o si hubo empate.
# =====================================================================

# ---------- Forma 1: if-elif clásico ----------
def votacion_1():
    votosA = votosB = votosC = 0

    while True:
        voto = input("Ingresa tu voto (A, B, C o FIN): ")
        if voto.upper() == "FIN":
            break
        elif voto.upper() == "A":
            votosA += 1
        elif voto.upper() == "B":
            votosB += 1
        elif voto.upper() == "C":
            votosC += 1
        else:
            print("Voto inválido.")

    print(f"A: {votosA}, B: {votosB}, C: {votosC}")
    if votosA == votosB == votosC:
        print("Empate total.")
    else:
        max_votos = max(votosA, votosB, votosC)
        if votosA == max_votos:
            print("Lista A gana.")
        elif votosB == max_votos:
            print("Lista B gana.")
        elif votosC == max_votos:
            print("Lista C gana.")

# ---------- Forma 2: lista y diccionario ----------
def votacion_2():
    listas = {"A":0, "B":0, "C":0}
    while True:
        voto = input("Ingresa tu voto (A, B, C o FIN): ").strip().upper()
        if voto == "FIN":
            break
        elif voto in listas:
            listas[voto] += 1
        else:
            print("Voto inválido.")
    print("Resultados:", listas)
    max_votos = max(listas.values())
    ganadores = [k for k,v in listas.items() if v == max_votos]
    if len(ganadores) == 1:
        print(f"🎉 Lista ganadora: {ganadores[0]}")
    else:
        print(f"🤝 Empate entre: {', '.join(ganadores)}")

# ---------- Forma 3: usando collections.Counter ----------
from collections import Counter
def votacion_3():
    votos = []
    while True:
        voto = input("Ingresa tu voto (A, B, C o FIN): ").strip().upper()
        if voto == "FIN":
            break
        elif voto in ("A","B","C"):
            votos.append(voto)
        else:
            print("Voto inválido.")
    conteo = Counter(votos)
    print("Resultados:", conteo)
    if len(set(conteo.values())) <= 1 and len(conteo) == 3:
        print("Empate total.")
    else:
        max_votos = max(conteo.values())
        ganadores = [k for k,v in conteo.items() if v==max_votos]
        if len(ganadores)==1:
            print(f"🎉 Lista ganadora: {ganadores[0]}")
        else:
            print(f"🤝 Empate entre: {', '.join(ganadores)}")

# ---------- Forma 4: con función de verificación ----------
def votacion_4():
    def validar(v):
        return v.upper() in ("A","B","C")
    votos = {"A":0,"B":0,"C":0}
    while True:
        voto = input("Voto (A,B,C o FIN): ").strip().upper()
        if voto == "FIN":
            break
        if validar(voto):
            votos[voto] +=1
        else:
            print("Voto inválido")
    print("Resultados:", votos)
    max_votos = max(votos.values())
    ganadores = [k for k,v in votos.items() if v==max_votos]
    print(f"Ganador(es): {', '.join(ganadores)}" if len(ganadores)>1 else f"Ganador: {ganadores[0]}")

# ---------- Forma 5: simplificada con ternarios ----------
def votacion_5():
    votos = {"A":0,"B":0,"C":0}
    while True:
        voto = input("Voto (A,B,C o FIN): ").strip().upper()
        if voto=="FIN":
            break
        votos[voto] = votos[voto]+1 if voto in votos else votos.get(voto,0)
    print("Resultados:", votos)
    max_v = max(votos.values())
    ganadores = [k for k,v in votos.items() if v==max_v]
    print(f"Ganador(es): {', '.join(ganadores)}" if len(ganadores)>1 else f"Ganador: {ganadores[0]}")

# =====================================================
# Ejecución del programa
# =====================================================
if __name__ == "__main__":
    # Descomentar la forma que quieras probar
    # votacion_1()
    # votacion_2()
    # votacion_3()
    # votacion_4()
    votacion_5()
