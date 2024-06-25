import random
import time
import matplotlib.pyplot as plt

def busqueda_lineal(array, numero):
    inicio = time.time()
    iteraciones = 0
    for i in range(len(array)):
        iteraciones += 1
        if array[i] == numero:
            fin = time.time()
            return i, inicio, fin, iteraciones
    fin = time.time()
    return -1, inicio, fin, iteraciones


resultados = []
tamaño_inicial = 100
incremento = 100

for i in range(50):
    tamaño_array = tamaño_inicial + (i * incremento)
    array = [random.randint(0, 100) for _ in range(tamaño_array)]
    numero_a_buscar = random.randint(0, 100)
    
    resultado, inicio, fin, iteraciones = busqueda_lineal(array, numero_a_buscar)
    
    resultados.append((i + 1, tamaño_array, iteraciones, fin))


print(f"{'1) Numero de Ensayo':<20} {'2) Tamaño de Volumen':<20} {'3) Veces de (for)':<20} {'4) Tiempo (s)':<20}")
print("="*80)
for resultado in resultados:
    print(f"{resultado[0]:<20} {resultado[1]:<20} {resultado[2]:<20} {resultado[3]:<20}")


inicios = [resultado[1] for resultado in resultados]  
fines = [resultado[3] for resultado in resultados]    


inicios_ordenados, fines_ordenados = zip(*sorted(zip(inicios, fines)))


plt.plot(inicios_ordenados, fines_ordenados, marker='o', linestyle='-', color='b')
plt.xlabel('Tamaño del Array')
plt.ylabel('Tiempo de Fin (s)')
plt.title('Tiempos de Fin vs Tamaño del Array')
plt.grid(True)
plt.show()
