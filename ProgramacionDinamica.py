import time
import matplotlib.pyplot as plt

def count_bst_dp(n):
    """
    Versión optimizada con Programación Dinámica (Bottom-Up).
    """
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Casos base
    
    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]
    
    return dp[n]

def measure_dp_execution_time(n_values):
    """
    Mide tiempos de ejecución para múltiples valores de n.
    """
    time_data = {}
    for n in n_values:
        start_time = time.time()
        count_bst_dp(n)
        end_time = time.time()
        time_data[n] = (end_time - start_time) * 1000  # ms
        print(f"n = {n}: {time_data[n]:.2f} micro s")
    return time_data

def plot_dp_times(time_data):
    """
    Genera una gráfica de tiempos de ejecución.
    """
    n_values = list(time_data.keys())
    times = list(time_data.values())
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, 'ro--', linewidth=2, markersize=8)
    plt.title('Tiempo de ejecución (Programación Dinámica)')
    plt.xlabel('Número de nodos (n)')
    plt.ylabel('Tiempo (milisegundos)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(n_values)
    plt.savefig('tiempos_dp_PrograDinámica.png')
    plt.show()

# Configuración de prueba (valores mucho más altos que en Divide and Conquer)
n_values = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500] 
print("⚡ Iniciando pruebas de Programación Dinámica...\n")
dp_times = measure_dp_execution_time(n_values)
print("\n📊 Generando gráfica...")
plot_dp_times(dp_times)